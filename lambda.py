import json
import boto3

def lambda_handler(event, context):
    data = json.loads(event["Data"])
    
    sns = boto3.client('sns')
    
    for packet in data.get("Packets", []):
        print(packet)
        
        # publish packets as messages to topic
        response = sns.publish(
        TopicArn='arn:aws:sns:ap-southeast-2:027464419432:Myriota',    
        Message=packet,    
        )
        print(response)
        
        # phone numbers are subscribed to topic so sohuld receive updates
