import json

def lambda_handler(event, context):
   return {
        "statusCode": 200,
        "body": json.dumps({
            "message": "I'm using canary deployments",
        }),
    }