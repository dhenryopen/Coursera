import MapReduce
import sys

"""
Process DNA Sequences in the Simple Python MapReduce Framework
"""

mr = MapReduce.MapReduce()

# =============================
# Do not modify above this line

list_of_books = list()

def mapper(record):
    mr.emit_intermediate(1, record)  # constant key of "1", pass all records to one reducer

def reducer(key, list_of_values):

    dna_sequences = list()

    for l in list_of_values:
        dna_sequences.append(l[1][0:len(l[1])-10])  # trim last 10 characters

    dna_sequences = list(set(dna_sequences))  # remove duplicates

    for d in dna_sequences:
        mr.emit(d)

# Do not modify below this line
# =============================
if __name__ == '__main__':
  inputdata = open(sys.argv[1])
  mr.execute(inputdata, mapper, reducer)
