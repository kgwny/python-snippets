
# 三項演算子

# [変数] = [True条件のときの値] if [条件] else [False条件のときの値]

# var = 'OK' if boolean == True else 'NG'

def ternary_operator(boolean):
    return 'OK' if boolean == True else 'NG'

boolean = bool(1)
print(ternary_operator(boolean))
# OK

boolean = bool(0)
print(ternary_operator(boolean))
# NG
