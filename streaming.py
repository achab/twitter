from tweepy import Stream
from tweepy.streaming import StreamListener
from authorize import give_api
import argparse
import json
import string

def get_parser():
    """Get parser for command line arguments."""
    parser = argparse.ArgumentParser(description="Twitter Downloader")
    parser.add_argument("-q",
                        "--query",
                        dest="query",
                        help="Query/Filter",
                        default='-')
    parser.add_argument("-d",
                        "--data-dir",
                        dest="data_dir",
                        help="Output/Data Directory")
    return parser


class MyListener(StreamListener):

    def __init__(self, data_dir, query):
        query_fname = format_filename(query)
        self.outfile = "%s/stream_%s.json" % (data_dir, query_fname)

    def on_data(self, data):
        try:
            with open(self.outfile, 'a') as f:
                f.write(data)
                print(data)
                return True
        except BaseException as e:
            print("Error on data: %s" % str(e))
            time.sleep(5)
        return True

    def on_error(self, status):
        print(status)
        return True

def format_filename(fname):
    """Convert file name into a safe string."""
    return ''.join(convert_valid(one_char) for one_char in fname)

def convert_valid(one_char):
    """Convert in '_' an invalid char"""
    valid_chars = "-_.%s%s" % (string.ascii_letters, string.digits)
    if one_char in valid_chars:
        return one_char
    else:
        return '_'

@classmethod
def parse(cls, api, raw):
    status = cls.first_parse(api, raw)
    setattr(status, 'json', json.dumps(raw))
    return status


if __name__ == "__main__":
    parser = get_parser()
    args = parser.parse_args()
    api = give_api()

    twitter_stream = Stream(api.auth, MyListener(args.data_dir, args.query))
    twitter_stream.filter(track=[args.query])
