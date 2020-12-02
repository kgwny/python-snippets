import os, csv

# delimiterが異なっているだけであり、tsvも扱うことが可能

target_file = './tmp/target.tsv'

text = 'title1\ttitle2\ttitle3\nword1\tword2\tword3'

# create file
if not os.path.exists(target_file):
    with open(target_file, 'w') as f:
        f.write(text)

# read file
with open(target_file, 'r') as f:
    data = csv.reader(f, delimiter = '\t')
    for row in data:
        print(row)

# remove file
# os.remove(target_file)
