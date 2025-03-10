import os
from openai import OpenAI

client = OpenAI(
    api_key=os.getenv("OPENAI_API_KEY")
)

completion = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[
        {"role": "system", "content": "あなたは新設なアシスタントです。"},
        {
            "role": "user",
            "content": "プログラミングにおける再起について俳句を書いてください"
        }
    ]
)

print(completion.choices[0].message.content)