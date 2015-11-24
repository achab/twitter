import tweepy
from authorize import give_api

api = give_api()

def print_last_status(n=10):
    for status in tweepy.Cursor(api.home_timeline).items(n):
        # Process a single status
        print(status.text)

