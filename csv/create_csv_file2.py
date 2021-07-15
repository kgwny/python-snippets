import os, csv

target_file = './tmp/target2.csv'

text1 = 'title1,title2,title3\n'
text2 = 'word1,word2,word3\n'
text3 = 'hoge1,hoge2,hoge3\n'

text_list = []
text_list.append(text1)
text_list.append(text2)
text_list.append(text3)

# create file
if not os.path.exists(target_file):
    with open(target_file, 'w') as f:
        for tmp_text in text_list:
            print(tmp_text)
            f.write(tmp_text)

# read file
# with open(target_file, 'r') as f:
#     data = csv.reader(f, delimiter = ',')
#     for row in data:
#         print(row)

# remove file
# os.remove(target_file)
