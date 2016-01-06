# top_ten.py
# Course 1 / Week 1 - Data Science at Scale (UW)
# November 2015

import json
import sys

hashtag_counter = {}  # initialize an empty dictionary for tweet scores

### MAIN

f1 = open(sys.argv[1])  # assumes arg1 is output.txt

for line in f1:
    try:
        tweet = json.loads(line.strip())

        if 'text' in tweet:  # only messages contains 'text' field is a tweet
            hashtags = []

            for hashtag in tweet['entities']['hashtags']:
                hashtags.append(hashtag['text'])

            for tag in hashtags:
                hashtag_counter[tag] = hashtag_counter.get(tag, 0) + 1

    except:  # read in a line is not in JSON format (sometimes an error will occur
        continue

i = 0
for tag in sorted(hashtag_counter, key=hashtag_counter.get, reverse=True):
    if i < 10:
        print "{0} {1}".format(tag, float(hashtag_counter[tag]))
        i += 1
