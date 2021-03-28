tmp_list = ['a.txt', 'b.doc']

for s in tmp_list:
    if s.endswith('.txt'):
        print('yes')

hoge_list = len([s for s in tmp_list if s.endswith('.txt')])
print(hoge_list)


# if len([for s in tmp_list if s.endswith('a.txt')]) > 0:
#     print('yes')
# else:
#     print('no')
