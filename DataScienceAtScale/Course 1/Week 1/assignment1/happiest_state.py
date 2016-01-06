# happiest_state.py
# Course 1 / Week 1 - Data Science at Scale (UW)
# November 2015

import csv
import json
import sys
import tokenize

scores = {} # initialize an empty dictionary for tweet scores
state_scores = {}

states = {  # create a lookup dictionary for state abbreviations
        'AK': 'Alaska',
        'AL': 'Alabama',
        'AR': 'Arkansas',
        'AS': 'American Samoa',
        'AZ': 'Arizona',
        'CA': 'California',
        'CO': 'Colorado',
        'CT': 'Connecticut',
        'DC': 'District of Columbia',
        'DE': 'Delaware',
        'FL': 'Florida',
        'GA': 'Georgia',
        'GU': 'Guam',
        'HI': 'Hawaii',
        'IA': 'Iowa',
        'ID': 'Idaho',
        'IL': 'Illinois',
        'IN': 'Indiana',
        'KS': 'Kansas',
        'KY': 'Kentucky',
        'LA': 'Louisiana',
        'MA': 'Massachusetts',
        'MD': 'Maryland',
        'ME': 'Maine',
        'MI': 'Michigan',
        'MN': 'Minnesota',
        'MO': 'Missouri',
        'MP': 'Northern Mariana Islands',
        'MS': 'Mississippi',
        'MT': 'Montana',
        'NA': 'National',
        'NC': 'North Carolina',
        'ND': 'North Dakota',
        'NE': 'Nebraska',
        'NH': 'New Hampshire',
        'NJ': 'New Jersey',
        'NM': 'New Mexico',
        'NV': 'Nevada',
        'NY': 'New York',
        'OH': 'Ohio',
        'OK': 'Oklahoma',
        'OR': 'Oregon',
        'PA': 'Pennsylvania',
        'PR': 'Puerto Rico',
        'RI': 'Rhode Island',
        'SC': 'South Carolina',
        'SD': 'South Dakota',
        'TN': 'Tennessee',
        'TX': 'Texas',
        'UT': 'Utah',
        'VA': 'Virginia',
        'VI': 'Virgin Islands',
        'VT': 'Vermont',
        'WA': 'Washington',
        'WI': 'Wisconsin',
        'WV': 'West Virginia',
        'WY': 'Wyoming'
}

# define a function to evaluate tweet tokens against the dictionary of terms

def get_state(this_location):

    # try to return the state associated with the location attribute

    location_str = this_location.upper()  # force to upper case
    location_str = location_str[-3:] # get the last three characters
    location_str = location_str.replace('"','')  # chop off the " character

    if location_str in states:
        return location_str
    else:
        return

def eval_sentiment(tweet_text):

    # initialize the sentiment score counter for the tweet

    this_sentiment = 0  #local variable

    # split the text

    tokens = tweet_text.split()

    # for each token in the text body of the tweet:

    for token in tokens:

        # for each term in the sentiment list:

        for term in scores:
             if term == token: # if a match, add the score to the sentiment score counter
                 this_sentiment = this_sentiment + scores[term]

    return this_sentiment

### MAIN

# read the list of sentiment terms and scores

f1 = open(sys.argv[1]) # assumes arg1 is AFINN-111.txt

for line in f1:
  term, score  = line.split("\t")  # The file is tab-delimited. "\t" means "tab character"
  scores[term] = int(score)  # Convert the score to an integer.

# read the tweets

f2 = open(sys.argv[2])  # assumes arg2 is output.txt

for line in f2:
    try:
        tweet = json.loads(line) # load it as Python dict
        this_sentiment = eval_sentiment(json.dumps(tweet["text"]))
        this_location = json.dumps(tweet["user"]["location"])

        if this_location != "null": # test for null string
            this_state = get_state(this_location)

            if this_state: # test for null value
                state_scores[this_state] = state_scores.get(this_state, 0) + this_sentiment  # increment the term frequencies
    except:
        pass # skip errors

happiest_state_name=max(state_scores, key=state_scores.get)
print(happiest_state_name)
