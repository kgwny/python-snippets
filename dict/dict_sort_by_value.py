score = {'kokugo': 49, 'sansuu': 85, 'rika': 60, 'shakai': 76}

# dictionary の中身をvalueでソートする
score_sorted = sorted(score.items(), key=lambda x:x[1])

print(score_sorted)
# [('kokugo', 49), ('rika', 60), ('shakai', 76), ('sansuu', 85)]
