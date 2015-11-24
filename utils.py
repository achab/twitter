import tweepy
import json
from authorize import give_api

api = give_api()

def process_or_store(tweet):
    print(json.dumps(tweet))

def process_last_status(n=10):
    for status in tweepy.Cursor(api.home_timeline).items(n):
        # Process a single status
        process_or_store(status._json)

