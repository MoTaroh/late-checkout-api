import json
import boto3
import aiohttp
import asyncio

from botocore.exceptions import ClientError

from hotels import HOTELS
from hotel import Hotel
from parser import Parser


def lambda_handler(event, context):
    """Sample pure Lambda function

    Parameters
    ----------
    event: dict, required
        API Gateway Lambda Proxy Input Format

        Event doc: https://docs.aws.amazon.com/apigateway/latest/developerguide/set-up-lambda-proxy-integrations.html#api-gateway-simple-proxy-for-lambda-input-format

    context: object, required
        Lambda Context runtime methods and attributes

        Context doc: https://docs.aws.amazon.com/lambda/latest/dg/python-context-object.html

    Returns
    ------
    API Gateway Lambda Proxy Output Format: dict

        Return doc: https://docs.aws.amazon.com/apigateway/latest/developerguide/set-up-lambda-proxy-integrations.html
    """

    # TODO:eventのバリデーション -> とりあえず後回し
    print(event)
    found = event["Payload"]["found"]
    data = json.loads(event["Payload"]["data"])

    if found:
        items = json.loads(data["hotels"])
        return {"statusCode": 200, "body": json.dumps({"totalCount": len(items), "items": items})}
    else:
        # scraping
        search_param = data
        stay_year = search_param["stayYear"]
        stay_month = search_param["stayMonth"]
        stay_day = search_param["stayDay"]
        stay_count = search_param["stayCount"]
        adult_num = search_param["adultNum"]

        # レイトチェックアウトホテル一覧を取得
        hotels = HOTELS
        parser = Parser()
        loop = asyncio.get_event_loop()
        result = loop.run_until_complete(handle_request(hotels, parser, search_param))

        print("== result ==")
        print(result)

        dynamodb = boto3.resource("dynamodb")
        table = dynamodb.Table("LateCheckoutHotels")

        db_id = f"{stay_year}-{stay_month}-{stay_day}-{stay_count}-{adult_num}"
        print(f"Put result to DynamoDB. Key: {db_id}")

        try:
            response = table.put_item(Item={"id": db_id, "hotels": json.dumps(result)})
        except ClientError as e:
            print(e.response["Error"]["Message"])
        else:
            print(response)

        return {
            "statusCode": 200,
            "body": json.dumps(
                {
                    "total_count": len(result),
                    "items": result,
                }
            ),
        }


async def get_hotel(session, url, parser, hotel):
    r = await session.get(url)
    html = await r.text()

    plans = parser.parse(html)
    hotel_result = {
        "hotelNo": hotel.yadNo,
        "hotelName": hotel.hotelName,
        # "prefNo": hotel.prefNo,
        # "regionNo": hotel.regionNo,
        "regionName": hotel.regionName,
        "planList": plans,
    }
    return hotel_result


async def handle_request(hotels: dict, parser, search_param: dict):
    print("start async")
    results = []
    async with aiohttp.ClientSession() as session:
        for h in hotels:
            hotel = Hotel(
                h["hotelName"],
                h["hotelNo"],
                h["regionName"],
                search_param["stayYear"],
                search_param["stayMonth"],
                search_param["stayDay"],
                search_param["stayCount"],
                search_param["adultNum"],
            )
            url = hotel.url
            print(url)
            task = asyncio.create_task(get_hotel(session, url, parser, hotel))
            results.append(task)

        return await asyncio.gather(*results)
