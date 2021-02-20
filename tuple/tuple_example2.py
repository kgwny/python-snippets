# 空のタプル
empty_tuple = ()
print(type(empty_tuple))
# <class 'tuple'>
print(empty_tuple)
# ()

# 要素がひとつだけのタプル
one_element_tuple = ('something')
print(one_element_tuple)
print(type(one_element_tuple))
# <class 'str'>
# 文字列になってしまう問題がある

# 回避策
# 書式その１
one_element_tuple = ('something',)
print(one_element_tuple)
# ('something',)

# 書式その２
one_element_tuple = 'something',
print(one_element_tuple)
# ('something',)
