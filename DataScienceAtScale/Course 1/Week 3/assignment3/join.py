import MapReduce
import sys

"""
SQL Query Simulated in the Simple Python MapReduce Framework
"""

mr = MapReduce.MapReduce()

# =============================
# Do not modify above this line

def mapper(record):
    key = record[1]
    mr.emit_intermediate(key,record)

def reducer(key, list_of_values):
    i = 0
    # order_info = {}
    # line_item_info = {}
    # complete_record = {}

    for l in list_of_values:
        if i == 0:
            order_info = l
        else:
            line_item_info = l
            joined_record = order_info + line_item_info
            mr.emit((joined_record))
        i += 1

# Do not modify below this line
# =============================
if __name__ == '__main__':
  inputdata = open(sys.argv[1])
  mr.execute(inputdata, mapper, reducer)
