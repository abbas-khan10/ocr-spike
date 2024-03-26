import boto3
import os


access_key = os.getenv("AWS_ACCESS_KEY_ID")
secret_access_key = os.getenv("AWS_SECRET_ACCESS_KEY")
session_token = os.getenv("AWS_SESSION_TOKEN")

key = "lloyd_george.pdf"
bucket = "ndrc-lloyd-george-store"

textract = boto3.client(
    "textract",
    aws_access_key_id=access_key,
    aws_secret_access_key=secret_access_key,
    aws_session_token=session_token,
    region_name="eu-west-2"
)

with open("data/lloyd_george.pdf", "rb") as data:
    file_bytes = data.read()

detect_response = textract.start_document_text_detection(DocumentLocation={'S3Object': {"Bucket": bucket, "Name": key}})
print(detect_response)

job_id = detect_response['JobId']

text = ''
status = None

while status != 'SUCCEEDED':
    extract_response = textract.get_document_text_detection(JobId=job_id)
    status = extract_response['JobStatus']

    if status == "SUCCEEDED":
        for item in extract_response.get('Blocks', []):
            if item['BlockType'] == 'LINE':
                text += item['Text'] + ' '
        text = text[:-1]
    elif status == "FAILED":
        print(f"Failed {extract_response}")
        break

print(text)
