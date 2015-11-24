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

def process_friends():
    for friend in tweepy.Cursor(api.friends).items():
        process_or_store(friend._json)

def process_all_tweets():
    for tweet in tweepy.Cursor(api.user_timeline).items():
        process_or_store(tweet._json)