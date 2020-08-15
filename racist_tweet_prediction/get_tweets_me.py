from config import API_SECRET

import tweepy
import time
import pandas as pd 
pd.set_option('display.max_colwidth', 1000)

authentication = tweepy.OAuthHandler(API_SECRET['key'], API_SECRET['secret'])
authentication.set_access_token(API_SECRET['access_token'], API_SECRET['access_token_secret'])

api = tweepy.API(authentication, wait_on_rate_limit=True)

def get_related_tweets(text_query):
    tweets_list = []
    count = 50
    try:
        for tweet in api.search(q=text_query, count=count):
            print(tweet.text)

            tweets_list.append({
                # 'created_at': tweet.created_at,
                # 'tweet_id': tweet.id,
                'tweet_text': tweet.text[:40]
            })
        
        return pd.DataFrame.from_dict(tweets_list)

    except BaseException as e:
        print('failed on_status', str(e))
        time.sleep(3)