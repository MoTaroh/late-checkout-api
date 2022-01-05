import json
import aiohttp
import asyncio

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

    query = event["queryStringParameters"]
    search_param = {
        "stay_year": query["stayYear"],
        "stay_month": query["stayMonth"],
        "stay_day": query["stayDay"],
        "stay_count": query["stayCount"],
        "adult_num": query["adultNum"]
    }

    # レイトチェックアウトホテル一覧を取得
    hotels = HOTELS
    parser = Parser()
    loop = asyncio.get_event_loop()
    result = loop.run_until_complete(
        handle_request(hotels, parser, search_param))

    print("== result ==")
    print(result)

    return {
        "statusCode": 200,
        "body": json.dumps({
            "total_count": len(result),
            "items": result,
        }),
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
        "planList": plans
    }
    return hotel_result


async def handle_request(hotels: dict, parser, search_param: dict):
    print("start async")
    results = []
    async with aiohttp.ClientSession() as session:
        for h in hotels:
            hotel = Hotel(
                h["hotelName"], h["hotelNo"], h["regionName"],
                search_param["stay_year"], search_param["stay_month"], search_param["stay_day"], search_param["stay_count"], search_param["adult_num"])
            url = hotel.url
            print(url)
            task = asyncio.create_task(get_hotel(session, url, parser, hotel))
            results.append(task)

        return await asyncio.gather(*results)
