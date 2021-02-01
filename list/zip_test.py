original = [['ね', 'ねずみ'], ['うし', 'うし'], ['とら', 'とら'], ['う', 'うさぎ']]

shorts, fulls = [x for x in zip(*original)]
print(shorts)
# ('ね', 'うし', 'とら', 'う')
print(fulls)
# ('ねずみ', 'うし', 'とら', 'うさぎ')
