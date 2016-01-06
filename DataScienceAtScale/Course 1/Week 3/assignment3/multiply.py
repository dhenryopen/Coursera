import MapReduce
import sys

"""
Multiply Matrix Example in the Simple Python MapReduce Framework
"""

mr=MapReduce.MapReduce()

# =============================
# Do not modify above this line

def mapper(record):
    if record[0]=='a':
        x = 0
        while x < 5:
            mr.emit_intermediate((record[1],x),record)
            x += 1
    else:
        x = 0
        while x < 5:
            mr.emit_intermediate((x,record[2]),record)
            x += 1

def reducer(key, list_of_values):
    i={}
    j={}
    x=0
    total=0

    for x in list_of_values:
        if x[0]=='a':
            i[x[2]]=x[3]
        else:
            j[x[1]]=x[3]

    for x in i:
        if x in j:
            total+=i[x]*j[x]

    mr.emit((key[0],key[1],total))

# Do not modify below this line
# =============================
if __name__ == '__main__':
  inputdata = open(sys.argv[1])
  mr.execute(inputdata, mapper, reducer)