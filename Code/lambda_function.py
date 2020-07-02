def my_handler(event, context):
    # See https://aws.amazon.com/premiumsupport/knowledge-center/malformed-502-api-gateway/
    return {
      'isBase64Encoded': False,
      'statusCode': 200,
      'headers': { },
      'body': 'Hello World, This is From Lamda Function'
    }
