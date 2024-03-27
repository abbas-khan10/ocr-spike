import json

import boto3
import os
import time

import botocore
import botocore.exceptions
from flask import Flask

access_key = os.getenv("AWS_ACCESS_KEY_ID")
secret_access_key = os.getenv("AWS_SECRET_ACCESS_KEY")
session_token = os.getenv("AWS_SESSION_TOKEN")

bucket = "ndrc-lloyd-george-store"
key = "lloyd_george.pdf"

s3 = boto3.client(
    "s3",
    aws_access_key_id=access_key,
    aws_secret_access_key=secret_access_key,
    aws_session_token=session_token,
    region_name="eu-west-2"
)

textract = boto3.client(
    "textract",
    aws_access_key_id=access_key,
    aws_secret_access_key=secret_access_key,
    aws_session_token=session_token,
    region_name="eu-west-2"
)

app = Flask(__name__)


def upload_file():
    try:
        s3.head_object(Bucket=bucket, Key=key)
    except botocore.exceptions.ClientError as e:
        if e.response['Error']['Code'] == "404":
            with open("data/lloyd_george.pdf", "rb") as data:
                file_bytes = data.read()

            s3.put_object(Bucket=bucket, Key="lloyd_george.pdf", Body=file_bytes)
        else:
            print("Error uploading file")
            exit(1)


@app.route('/extract', methods=['GET'])
def extract():
    upload_file()

    start = time.perf_counter()

    detect_response = textract.start_document_text_detection(
        DocumentLocation={'S3Object': {"Bucket": bucket, "Name": key}})

    print(detect_response)

    job_id = detect_response['JobId']

    extracted = {}
    text = ''
    status = None

    while status != 'SUCCEEDED':
        extract_response = textract.get_document_text_detection(JobId=job_id)
        status = extract_response['JobStatus']

        if status == "FAILED":
            print(f"Failed {extract_response}")
            exit(1)
        else:
            for item in extract_response.get('Blocks', []):
                if item['BlockType'] == 'LINE':
                    text += item['Text'] + ' '
            text = text[:-1]

    end = time.perf_counter()

    response = {
        "time_taken": end - start,
        "response": text
    }

    return json.dumps(response)


if __name__ == '__main__':
    app.run(port=5000)
