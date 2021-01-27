my_list = [1, 2, 3]

print(my_list)
# [1, 2, 3]

my_list = [i * 2 for i in range(3)]
print(my_list)
# [0, 2, 4]

my_list = [i for i in [1, 2, 3] if i > 1]
print(my_list)
# [2, 3]

my_list = list(range(-3, 3))
print(my_list)
# [-3, -2, -1, 0, 1, 2]

my_list = [1, 2, 3, 4, 5, 6]

print(my_list[0])
# 1
print(my_list[-1])
# 6
