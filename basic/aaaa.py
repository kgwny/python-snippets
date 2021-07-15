import random

with open('my_file.txt', 'w') as f:
    for _ in range(10):
        f.write('a' * random.randint(0, 100))
        f.write('\n')

it = (len(x) for x in open('my_file.txt'))
print(next(it))
print(next(it))
