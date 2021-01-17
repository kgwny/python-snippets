import re

match = re.search(r'\d+', 'aaa123zzz')

if match:
    print('matched:', match.group(0))

# search を使うと文字列の途中からでも一致する
m = re.search(r'B+', 'AAABBBCCC')
assert(m != None)  # 一致

# match を使うと文字列の先頭から一致させる
m = re.match(r'B+', 'AAABBBCCC')
assert(m == None)  # 不一致
