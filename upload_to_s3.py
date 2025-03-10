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

file_name = "diary.txt"
bucket_name = "diaryapp.ito"

try:
    with open(file_name, "rb") as file:
        s3.upload_fileobj(file, bucket_name, file_name)
        print(f"'{file_name}'が'{bucket_name}'にアップロードされました。")
except Exception as e:
    print(f"アップロード中にエラーが発生しました： {e}")