# frequency.py
# Course 1 / Week 1 - Data Science at Scale (UW)
# November 2015

import json
import sys

# Initialize variables

frequencies = {}  # for the new terms
tokencount = 0

# function to parse and filter tokens and maintain counts

def evaltweet(tweet):
    global tokencount  # running counter

    # split the tweet

    tokens = tweet.split()

    # for each token in the text body of the tweet:

    for token in tokens:

        tokencount = tokencount + 1  # increment the counter

        if (token.startswith("#")) or (token.startswith("@")):  # skip these
            continue
        else:
            frequencies[token] = frequencies.get(token, 0) + 1  # increment the term frequencies

# Read and parse the tweets, extracting only the text

f1 = open(sys.argv[1])  # assumes arg1 is output.txt

for line in f1:
    try:
        tweet = json.loads(line)
        evaltweet(json.dumps(tweet["text"]))
    except:
        pass  # skip errors due to incomplete / malformed tweets

for token in frequencies:
    print "{0} {1:0.6f}".format(token, (float(frequencies[token]) / float(tokencount)))
