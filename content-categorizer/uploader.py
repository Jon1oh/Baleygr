import os
import boto3

client = boto3.client(
    "s3",
    aws_access_key_id=os.environ["AWS_ACCESS_KEY_ID"],
    aws_secret_access_key=os.environ["AWS_SECRET_ACCESS_KEY"],
)


os.chdir("content-categorizer/webpages")
bucket = "sagemaker-studio-hvyjem62pnq"
for file in os.listdir():
    if file.endswith(".txt"):
        client.upload_file(f"{file}", bucket, f"{file}")
