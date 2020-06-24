
list_a = set(['red', 'blue', 'green'])
list_b = set(['green', 'yellow', 'white'])

# 順序性は担保されないのかも

print(list_a)
# {'red', 'blue', 'green'}

print(list_b)
# {'green', 'white', 'yellow'}

print(list_a - list_b)
# {'red', 'blue'}

print(list_a | list_b)
# {'blue', 'white', 'red', 'green', 'yellow'}

print(list_a & list_b)
# {'green'}

print(list_a ^ list_b)
# {'blue', 'white', 'red', 'yellow'}

print('green' in list_a)
# True

list_a.add('black')
print(list_a)
# {'red', 'blue', 'green', 'black'}
