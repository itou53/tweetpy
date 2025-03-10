import os
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

def lambda_handler(event, context):
    client = OpenAI(
        # api_key=os.environ.get("OPENAI_API_KEY"),  # This is the default and can be omitted
        api_key=os.getenv('OPENAI_API_KEY')
    )

    chat_completion = client.chat.completions.create(
        messages=[
            {
                "role": "user",
                "content": "Say this is a test",
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
