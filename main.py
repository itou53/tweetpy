import os
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

def get_role_text(file_path = "role_text.txt"):
    """
    ローカルファイルからロールテキストを読み込む
    デフォルトでは'role_text.txt'を読み込む
    """
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"File not found: {file_path}")
    
    with open(file_path, "r", encoding="utf-8") as file:
        role_text = file.read().strip()
        return role_text

def lambda_handler(event, context):
    client = OpenAI(
        # api_key=os.environ.get("OPENAI_API_KEY"),  # This is the default and can be omitted
        api_key=os.getenv('OPENAI_API_KEY')
    )

    # ロールテキストを取得
    role_text = get_role_text()
    
    chat_completion = client.chat.completions.create(
        messages=[
            {
                "role": "system",
                "content": role_text,
            },
            {
                "role": "user",
                "content": "おやすみ",
            }
        ],
        model="gpt-4o",
    )

    response_context = chat_completion.choices[0].message.content
    print(response_context)

# ローカル実行用（AWS Lambda外でテストする場合）
if __name__ == "__main__":
    test_event = {"message": "write a haiku about nature"}
    response = lambda_handler(test_event, None)
    print(response)
