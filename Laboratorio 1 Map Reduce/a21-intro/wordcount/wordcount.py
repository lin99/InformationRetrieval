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
    words = value.split()

    # ---- TU CODIGO AQUI ----
  
    for w in words:
        mr.emit_intermediate(w,1)
    # ------------------------

def reducer(key, list_of_values):
    # ---- TU CODIGO AQUI ----
    mr.emit((key, len(list_of_values)))
    # ------------------------

# Do not modify below this line
# =============================
if __name__ == '__main__':
  inputdata = open(sys.argv[1])
  mr.execute(inputdata, mapper, reducer)
