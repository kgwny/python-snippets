import csv, os

target_file = 'tmp.csv'

text = 'title1,title2,title3\nword1,word2,word3'

# create file
if not os.path.exists(target_file):
    with open(target_file, 'w') as f:
        f.write(text)

# read file
with open(target_file, 'r') as f:
    data = csv.reader(f, delimiter = ',')
    for row in data:
        print(row)

# remove file
os.remove(target_file)
