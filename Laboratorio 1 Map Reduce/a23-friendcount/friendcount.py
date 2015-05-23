import MapReduce
import sys

mr = MapReduce.MapReduce()

# =============================
# Do not modify above this line

def mapper(record):
    # key: personA
    # value: personB
    key = record[0]
    value = record[1]
    # --- TU CODIGO AQUI ---
    mr.emit_intermediate(key,value)
    
def reducer(key, list_of_values):
    # --- TU CODIGO AQUI ---
    res = 0
    for k in list_of_values:
        res += 1
    mr.emit((key,res))

# Do not modify below this line
# =============================
if __name__ == '__main__':
  inputdata = open(sys.argv[1])
  mr.execute(inputdata, mapper, reducer)
