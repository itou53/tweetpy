import os
import json
from requests_oauthlib import OAuth1Session
from dotenv import load_dotenv

# .envファイルから環境変数を読み込む
load_dotenv()

def post_tweet(tweet_text="おはよう"):
    """Twitter APIを使ってツイートを投稿する"""
    consumer_key = os.getenv("TWITTER_API_KEY")
    consumer_secret = os.getenv("TWITTER_API_SECRET")
    access_token = os.getenv("TWITTER_ACCESS_TOKEN")
    access_token_secret = os.getenv("TWITTER_ACCESS_SECRET")
    
    if not all([consumer_key, consumer_secret, access_token, access_token_secret]):
        print("Error: APIキーが不足しています。")
        return
    
    payload = {"text": tweet_text}
    
    oauth = OAuth1Session(
        consumer_key,
        client_secret=consumer_secret,
        resource_owner_key=access_token,
        resource_owner_secret=access_token_secret,
    )
    
    response = oauth.post("https://api.twitter.com/2/tweets", json=payload)
    
    if response.status_code != 201:
        print(f"Error: {response.status_code}")
        print(json.dumps(response.json(), indent=4, ensure_ascii=False))
    else:
        print("ツイート成功！")
        print(json.dumps(response.json(), indent=4, ensure_ascii=False))

if __name__ == "__main__":
    # ユーザーからの入力を取得（デフォルトは「おはよう」）
    tweet_text = input("ツイートする内容を入力してください: ") or "おはよう"
    post_tweet(tweet_text)
