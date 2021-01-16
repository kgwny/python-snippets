from collections import defaultdict

val_str = {'a': 1, 'b': 2, 'c': 3}
d = defaultdict(int)

for key in val_str:
    d[key] += 1

print(d)
# defaultdict(<class 'int'>, {'a': 1, 'b': 1, 'c': 1})
