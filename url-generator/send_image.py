import boto3, os

client = boto3.client('s3', aws_access_key_id='AKIA5OX2ETWHVMCTJF5F'
                          ,aws_secret_access_key='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')

os.chdir('url-generator\whitelist_screenshots')

for file in os.listdir():
    print(file)
    if '.png' in file:
        upload_file_bucket = 'sagemaker-studio-9iyt1u3aar'
        upload_file_key = 'whitelist/' + str(file)
        client.upload_file(file, upload_file_bucket, upload_file_key)

print('Transfer complete')