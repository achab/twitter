import json

with open('test/stream_DALS.json', 'r') as f:
    line = f.readline() # read only the first line
    tweet = json.loads(line) # load it as Python dict
    print(json.dumps(tweet, indent=4)) # pretty-print
