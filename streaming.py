from tweepy import Stream
from tweepy.streaming import StreamListener
from authorize import give_api

api = give_api()

class MyListener(StreamListener):

    def on_data(self, data):
        try:
            with open('thanksgiving.json', 'a') as f:
                f.write(data)
                return True
        except BaseException as e:
            print("Error on data: %s" % str(e))
        return True

    def on_error(self, status):
        print(status)
        return True

twitter_stream = Stream(api.auth, MyListener())
twitter_stream.filter(track=['#ThanksgivingWithBlackFamilies'])