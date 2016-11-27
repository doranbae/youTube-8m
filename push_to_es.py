import csv
from pyes import *

reader = csv.reader(open('out.csv'))

conn = ES('127.0.0.1:9200', timeout=20.0)

counter = 0
for row in reader:
        try:
                out = {"thumbnail":row[1]}
                conn.index(out,'index_col',counter, bulk=True)
                counter += 1
        except:
                pass
