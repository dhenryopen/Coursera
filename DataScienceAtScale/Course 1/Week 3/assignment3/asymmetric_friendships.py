import MapReduce
import sys

"""
Friend Count in the Simple Python MapReduce Framework
"""

mr = MapReduce.MapReduce()

# =============================
# Do not modify above this line

def mapper(record):
    friends_pair = record[0] + ":" + record[1] # build a person:friend pair
    mr.emit_intermediate(1, friends_pair)  # set all keys to a constant of 1 so we have 1 reducer

# what comes into the reducer is a list of person:friend pairs (friends_list)

def reducer(key, friends_list):

    # create a reverse_list of friend:person pairs - these represent *potential* symmetrical friendships

    reverse_list = list()

    for pair in friends_list:
        names = pair.split(":")
        reverse_pair = names[1] + ":" + names[0]
        reverse_list.append(reverse_pair)

    mutual_friends_list = list()

    for pair in reverse_list:           # for each friend:person pair in the reverse_list
        if pair in friends_list:        # look for it's existence in the friends_list
            mutual_friends_list.append(pair)  # if it's a match, we include the pair from the list to subtract

    not_friends_list = list(set(friends_list) - set(mutual_friends_list)) # subtract the mutual_friends_list from the friends_list

    output_list=list()

    for pair in not_friends_list:       # re-form the list of pairs
        record=pair.split(":")
        not_friends_record=[record[0],record[1]]
        output_list.append(not_friends_record)

    for pair in not_friends_list:       # and add the reverse order pairs
        record=pair.split(":")
        not_friends_record=[record[1],record[0]]
        output_list.append(not_friends_record)

    sorted_output_list = sorted(output_list)

    for pair in sorted_output_list:
        mr.emit((pair[0], pair[1]))

# Do not modify below this line
# =============================
if __name__ == '__main__':
  inputdata = open(sys.argv[1])
  mr.execute(inputdata, mapper, reducer)
