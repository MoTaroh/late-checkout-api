import json
import boto3
from botocore.exceptions import ClientError


def lambda_handler(event, context):
    """DynamoDBからホテルを検索し、結果を返す

    Args:
        event (dict): event
            {
                'input': '{...}',
                'name': 'str',
                'stateMachineArn': 'stepfunction arn'
            }
        context (dict): context

    Returns:
        [type]: [description]
    """
    # bodyから検索条件を取得
    try:
        data = json.loads(event["input"])
        stay_year = data["stayYear"]
        stay_month = data["stayMonth"]
        stay_day = data["stayDay"]
        stay_count = data["stayCount"]
        adult_num = data["adultNum"]
    except json.JSONDecodeError as e:
        print(e)
        raise e
    except KeyError as e:
        print(e)
        raise e

    # 取得した検索条件からDynamoDBのKeyを生成
    db_key = f"{stay_year}-{stay_month}-{stay_day}-{stay_count}-{adult_num}"

    # DynamoDBに対して検索
    dynamodb = boto3.resource("dynamodb", endpoint_url="http://localhost:8000")
    table = dynamodb.Table("LateCheckoutHotels")

    try:
        response = table.get_item(Key={"id": db_key})
    except ClientError as e:
        print(e.response["Error"]["Message"])
    else:
        data = response.get("Item", {})

    # 見つかればTrue, 見つからなければFalseを返す
    found = True if data else False

    return {
        "found": found,
        "data": json.dumps(data),
    }
