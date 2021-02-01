rng = list(range(10, 0))
print(rng)
# []

rng = list(range(10, 0, -1))
print(rng)
# [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]

# 上の例と等価
rng = list(range(1, 11))
rng.reverse()
print(rng)
# [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
