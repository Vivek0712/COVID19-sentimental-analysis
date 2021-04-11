import os
import json
import boto3
import csv
from boto3.dynamodb.conditions import Key, Attr

comprehend = boto3.client('comprehend')
dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('covidsentiment')
print("Loading function")


def lambda_handler(event, context):
    """Read file from s3 on trigger."""
    s3 = boto3.client("s3")
    if event:
        file_obj = event["Records"][0]
        bucketname = str(file_obj['s3']['bucket']['name'])
        filename = str(file_obj['s3']['object']['key'])
        print("Filename: ", filename)
        fileObj = s3.get_object(Bucket=bucketname, Key=filename)
        file_content = fileObj["Body"].read().decode('utf-8').splitlines(True)
        print(file_content)
        recList = list()
        reader = csv.DictReader(file_content)
        for row in reader:
        # csv_header_key is the header keys which you have defined in your csv header
            # print(row['text'])
            table.put_item(
            Item={
               
                'text': row['text'],
                'location': row['location'],
                'phase': row['phase'],
                'sentiment': comprehend.detect_sentiment(Text=row['text'],LanguageCode='en')['Sentiment']
                }
            )   
