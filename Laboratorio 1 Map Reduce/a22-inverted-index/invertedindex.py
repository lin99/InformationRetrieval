import MapReduce
import sys

mr = MapReduce.MapReduce()

# =============================
# Do not modify above this line

def mapper(record):
    # key: document identifier
    # value: document contents
    key = record[0]
    value = record[1]
    # --- TU CODIGO AQUI ---
    words = value.split()
    variable = set()
    
    for k in words:
        if not (k in variable):
            mr.emit_intermediate(k,key)
            variable.add(k)

def reducer(key, list_of_values):
    # --- TU CODIGO AQUI ---
   mr.emit((key, list_of_values)) 
# Do not modify below this line
# =============================
if __name__ == '__main__':
  inputdata = open(sys.argv[1])
  mr.execute(inputdata, mapper, reducer)
