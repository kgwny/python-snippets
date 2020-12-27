import os

target_file = 'const.txt'
# item1=aaa
# item2=bbb
# item3=ccc
# 

consts = ''

if os.path.exists(target_file):
    with open(target_file, 'r') as f:
        consts = f.read()

l = consts.split('\n')
print(l)
# ['item1=aaa', 'item2=bbb', 'item3=ccc', '']

d = dict(s.split('=') for s in l if s != '')
print(d)
# {'item1': 'aaa', 'item2': 'bbb', 'item3': 'ccc'}
