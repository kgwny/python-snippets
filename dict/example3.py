d1 = {'k1': 1, 'k2': 2}
d2 = {'k3': 3, 'k4': 4}

print(d1)
# {'k1': 1, 'k2': 2}

print(d2)
# {'k3': 3, 'k4': 4}

# 複数の辞書を結合する
d = {**d1, **d2}
print(d)
# {'k1': 1, 'k2': 2, 'k3': 3, 'k4': 4}
