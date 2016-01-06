# tweet_sentiment.py
# Course 1 / Week 1 - Data Science at Scale (UW)
# November 2015

import csv
import json
import sys
import tokenize

# define a function to evaluate tweet tokens against the dictionary of terms

def evaltweet(tweet):

    # initialize the sentiment score counter for the tweet

    sentiment = 0

    # split the text

    tokens = tweet.split()

    # for each token in the text body of the tweet:

    for token in tokens:

        # for each term in the sentiment list:

        for term in scores:
             if term == token: # if a match, add the score to the sentiment score counter
                 sentiment = sentiment + scores[term]

            # print("Term =",term, "token=",str.lower(token))

    print sentiment

# read the list of sentiment terms and scores

f1 = open(sys.argv[1]) # assumes arg1 is AFINN-111.txt

scores = {} # initialize an empty dictionary
for line in f1:
  term, score  = line.split("\t")  # The file is tab-delimited. "\t" means "tab character"
  scores[term] = int(score)  # Convert the score to an integer.

# print scores.items() # Print every (term, score) pair in the dictionary

# read the tweets

f2 = open(sys.argv[2])  # assumes arg2 is output.txt

for line in f2:
    try:
        tweet = json.loads(line) # load it as Python dict
        evaltweet(json.dumps(tweet["text"]))
        # print(json.dumps(tweet["text"], indent=4)) # pretty-print
    except:
        pass # skip errors


