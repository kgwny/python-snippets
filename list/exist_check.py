tmp_list = ['a.txt', 'b.doc']

for s in tmp_list:
    if s.endswith('.txt'):
        print('yes')

print(len([s for s in tmp_list if s.endswith('.txt')]))
# 1
