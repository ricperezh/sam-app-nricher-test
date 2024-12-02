import json

def lambda_handler(event, context):

    if True:
        raise Exception("This will cause a deployment rollback")

    return {
        "statusCode": 200,
        "body": json.dumps({
            "message": "I'm using canary deployments",
        }),
    }