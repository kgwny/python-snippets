scores = [
    {'ika': 77, 'tako': 23},
    {'ika': 33, 'tako': 85},
    {'ika': 55, 'tako': 100}
]

scores_sorted = sorted(scores, key=lambda x:x['ika'])

print(scores_sorted)
# [{'ika': 33, 'tako': 85}, {'ika': 55, 'tako': 100}, {'ika': 77, 'tako': 23}]
