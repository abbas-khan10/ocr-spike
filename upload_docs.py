import boto3
import os


access_key = os.getenv("AWS_ACCESS_KEY_ID")
secret_access_key = os.getenv("AWS_SECRET_ACCESS_KEY")
session_token = os.getenv("AWS_SESSION_TOKEN")

bucket = "ndrc-lloyd-george-store"

s3 = boto3.client(
    "s3",
    aws_access_key_id=access_key,
    aws_secret_access_key=secret_access_key,
    aws_session_token=session_token,
    region_name="eu-west-2"
)

with open("data/lloyd_george.pdf", "rb") as data:
    file_bytes = data.read()

s3.put_object(Bucket=bucket, Key="lloyd_george.pdf", Body=file_bytes)

