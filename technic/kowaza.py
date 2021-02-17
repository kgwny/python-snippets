source_word = 'Hello World!'
search_word = 'or'

# 小技 - 文字列検索（検索キーワード in 文字列）
if search_word in source_word:
    print('"{}" is included in "{}".'.format(search_word, source_word))

some_dict = {
    'programming': ['android', 'c', 'css', 'python', 'swift', 'kotlin'],
    'gardening': ['hydroponics', 'planter'],
    'iot': ['raspberry_pi', 'arduino'],
    'analog': ['speaker', 'electric_circuit'],
    'posts': ['localize', 'hotsand', 'camp'],
}

# 小技 - 辞書検索（key, array in 辞書）
for key, array in some_dict.items():
    if 'python' in array:
        print(key, array)

# 小技 - 文字列の中にある区切り文字で分割・結合する
csv_data1 = 'hoge,ika,tako'
arr = csv_data1.split(',')
print('split:', arr)

csv_data2 = ','.join(arr)
print('join:', csv_data2)

# 小技 - 文字列の置換
word = 'Hello World!'
result = word.replace('World', 'Python')
print(result)
# Hello Python!

# 小技 - 正規表現で文字列置換
import re
text = 'Hello world!'
result = re.sub('[a-z]*!', 'Python!', text)
print(result)
# Hello Python!

num_str = '114514@hoge'
res = re.sub('[0-9]*@', '*@', num_str)
print(res)
# *@hoge

# 小技 - URLの抽出
import re
pattern = 'https?://[\w/:%#\$&\?\(\)~\.=\+\-]+'
text = '''
<link rel="dns-prefetch" href="https://images-na.ssl-images-amazon.com">
<link rel="dns-prefetch" href="https://m.media-amazon.com">
<link rel="dns-prefetch" href="https://completion.amazon.com">
'''
result = re.findall(pattern, text)
print(result)

# 小技 - 最終更新日のタイムスタンプ取得
import os
import datetime
st = os.stat('.gitignore')
update_time = datetime.datetime.fromtimestamp(st.st_mtime)
print(update_time.strftime('%Y-%m-%d %H:%M:%S'))
