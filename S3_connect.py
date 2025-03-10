import boto3
from dotenv import load_dotenv
import os

load_dotenv()

aws_access_key = os.getenv('AWS_ACCESS_KEY_ID')
aws_secret_key = os.getenv('AWS_SECRET_ACCESS_KEY')
region = os.getenv('AWS_DEFAULT_REGION')

# IAMアクセスキーを直接指定（セキュリティ的には非推奨）
s3 = boto3.client(
    "s3",
    aws_access_key_id=aws_access_key,
    aws_secret_access_key=aws_secret_key,
    region_name=region
)

# バケット一覧を取得
response = s3.list_buckets()
for bucket in response["Buckets"]:
    print(bucket["Name"])
