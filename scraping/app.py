import json
from typing import Optional

from hotels import HOTELS
from hotel import Hotel
from scraping.parser import Parser

# import requests


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

    # eventから検索条件を取得
    body = event["body"]
    stay_year = body["stayYear"]
    stay_month = body["stayMonth"]
    stay_day = body["stayDay"]
    stay_count = body["stayCount"]
    adult_num = body["adultNum"]

    # レイトチェックアウトホテル一覧を取得
    hotels = HOTELS

    result = []
    for h in hotels:
        # ホテルインスタンスを作成
        hotel = Hotel(
            h["hotelName"], h["hotelNo"], h["regionName"],
            stay_year, stay_month, stay_day, stay_count, adult_num)
        # URLからhtmlを取得
        html = hotel.get_html()
        parser = Parser()
        plans = parser.parse(html)
        hotel_result = {
            "hotelNo": hotel.yadNo,
            "hotelName": hotel.hotelName,
            "prefNo": hotel.prefNo,
            "regionNo": hotel.regionNo,
            "regionName": hotel.regionName,
            "planList": plans
        }
        result.append(hotel_result)

    return {
        "statusCode": 200,
        "body": json.dumps({
            "total_count": len(result),
            "items": result,
        }),
    }
