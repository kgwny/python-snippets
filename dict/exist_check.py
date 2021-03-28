# 辞書
dict_1 = { 'a' : 'aaa', 'b' : 'bbb', 'c' : 'ccc' }
print(dict_1)

# リスト
list_1 = ['a', 'b', 'c']
print(list_1)

if all(key in dict_1 for key in list_1):
    print('辞書の中にすべてのキーがある')
else:
    print('辞書の中にないキーがある')
