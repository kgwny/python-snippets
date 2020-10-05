# 重複チェック

list1 = [1, 2, 3, 4]

if len(list1) != len(set(list1)):
    print('duplicate error detected.')
else:
    print('check ok.')

list2 = [1, 2, 2, 3, 4]

if len(list2) != len(set(list2)):
    print('duplicate error detected.')
else:
    print('check ok.')
