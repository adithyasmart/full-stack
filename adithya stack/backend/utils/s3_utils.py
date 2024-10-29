import boto3
from botocore.exceptions import NoCredentialsError

async def upload_to_s3(file):
    s3_client = boto3.client('s3')
    try:
        s3_client.upload_fileobj(file.file, 'your_s3_bucket', file.filename)
        return f"https://your_s3_bucket.s3.amazonaws.com/{file.filename}"
    except NoCredentialsError:
        raise Exception("Credentials not available")
