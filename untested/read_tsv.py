import csv

target_tsv = "data.tsv"

f = open(path, "r")
data = csv.reader(f, delimiter = "\t")
for row in data:
    print(row)
f.close()
