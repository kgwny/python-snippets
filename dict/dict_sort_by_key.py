score = {'kokugo': 49, 'sansuu': 85, 'rika': 60, 'shakai': 76}

# score.sort()
# AttributeError: 'dict' object has no attribute 'sort'

# dictionary の中身をキーでソートする
score_sorted = sorted(score.items(), key=lambda x:x[0])

print(score_sorted)
# [('kokugo', 49), ('rika', 60), ('sansuu', 85), ('shakai', 76)]
