# term_sentiment.py
# Course 1 / Week 1 - Data Science at Scale (UW)
# November 2015

import json
import sys

### FUNCTIONS

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
             if term == token: # if the token is in the master dictionary, add the score to the sentiment score counter
                 sentiment = sentiment + scores[term]

    # repeat for each token, evaluating the new_terms dictionary

    for token in tokens:

            if token in scores:
                pass # it exists in the master dictionary, not a new term
            else:
                if not token in new_terms: # it's a new term not yet in the new_terms dictionary, so
                    new_terms[token] = float(sentiment) # add it and initialize the value to the current tweet's sentiment
                else:
                    new_terms[token] = new_terms[token] + sentiment # it's in the new_terms dictionary, just add the sentiment

### MAIN

# Initialize two empty dictionaries

scores = {}  # for the sentiment vocabulary
new_terms = {}  # for the new terms

# Read the dictionary of sentiment terms and scores

f1 = open(sys.argv[1]) # assumes arg1 is AFINN-111.txt

for line in f1:
  term, score  = line.split("\t")  # The file is tab-delimited. "\t" means "tab character"
  scores[term] = int(score)  # Convert the score to an integer.

# Then read and parse the tweets, extracting only the text

f2 = open(sys.argv[2])  # assumes arg2 is output.txt

for line in f2:
    try:
        tweet = json.loads(line)
        evaltweet(json.dumps(tweet["text"]))  # call the processing function
    except:
        pass # skip errors due to incomplete / malformed tweets

for term in new_terms:
    print "{} {}".format(term, new_terms[term])


