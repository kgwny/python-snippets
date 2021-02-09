# immutableなので要素の変更は不可
tuple_test = (0, 1, 2)
# tuple_test[0] = 0
# TypeError: 'tuple' object does not support item assignment

tuple_data = (4, 3, 2, 1)
print(all(tuple_data))
print(any(tuple_data))
print(enumerate(tuple_data))
print(len(tuple_data))
print(max(tuple_data))
print(min(tuple_data))
print(sorted(tuple_data))
print(sum(tuple_data))

# list -> tuple
num_list = [1, 2, 3, 4]
print(num_list)
num_tuple = tuple(num_list)
print(num_tuple)
