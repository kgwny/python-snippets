str_1 = 'hogehoge'
list_1 = [100, 200, 300]
list_2 = [100, 200, 300]
list_3 = [300, 200, 100]
tuple_1 = (100, 200, 300)

print(list_1 == list_2)
# True

print(list_1 == list_3)
# False

print(list_1 == tuple_1)
# False

print(str_1 == 'hogehoge')
# True
