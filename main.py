import os
import sys
import textwrap
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

client = OpenAI(
    api_key=os.getenv("OPENAI_API_KEY")
)

if len(sys.argv) < 2:
    print("引数を入力して")
    sys.exit(1)

today_event = " ".join(sys.argv[1:])

completion = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[
        {"role": "system", "content": "あなたは親切なアシスタントです。"},
        {
            "role": "user",
            "content": f"以下の出来事を元に140文字以内の日記を出力してください。内容はできるだけ抽象的かつ文学的っぽくして、具体的な固有名詞や特定できる情報はすべてぼやかして書いて。\n\n{today_event}"
        }
    ]
)

print(completion.choices[0].message.content)