import json


def lambda_handler(event, context):
    # bodyから検索条件を取得
    print(event)
    # body = json.loads(event["body"])

    # 取得した検索条件からDynamoDBのKeyを生成

    # DynamoDBに対して検索
    data = {}

    # 見つかればTrue, 見つからなければFalseを返す
    if data:
        found = True
    else:
        found = False

    return {
        "found": found,
        "data": json.dumps({data}),
    }
