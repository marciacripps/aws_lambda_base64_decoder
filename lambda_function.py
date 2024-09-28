import base64
import json

def lambda_handler(event, context):
    print("Received event:", event)  
    
    if 'base64' in event:
        base64_string = event['base64']

    elif 'body' in event:
        try:
            body = json.loads(event['body'])
            base64_string = body.get('base64', "")
        except (KeyError, json.JSONDecodeError):
            return {
                'statusCode': 400,
                'headers': {
                    'Content-Type': 'application/json',
                    'Access-Control-Allow-Origin': '*',
                },
                'body': json.dumps({
                    'error': 'No Base64 string found in the request'
                })
            }
    else:
        base64_string = ""

    if base64_string:
        try:
            # Decode the Base64 string
            decoded_data = base64.b64decode(base64_string).decode('utf-8')
            return {
                'statusCode': 200,
                'headers': {
                    'Content-Type': 'application/json',
                    'Access-Control-Allow-Origin': '*',
                },
                'body': json.dumps({
                    'decoded': decoded_data
                })
            }
        except Exception as e:
            print("Error decoding Base64:", str(e))  
            return {
                'statusCode': 400,
                'headers': {
                    'Content-Type': 'application/json',
                    'Access-Control-Allow-Origin': '*',
                },
                'body': json.dumps({
                    'error': 'Invalid request',
                    'message': str(e)
                })
            }
    else:
        print("No Base64 string found") 
        return {
            'statusCode': 400,
            'headers': {
                'Content-Type': 'application/json',
                'Access-Control-Allow-Origin': '*',
            },
            'body': json.dumps({
                'error': 'No Base64 string found in the request'
            })
        }
