# 条件に合致した最初の値を抽出する
def find(cond, li, default=None):
    return next((l for l in li if cond(l)), default)

# 以下と同義
def find_(cond, li, default=None):
    for l in li:
        if cond(l):
            return l
    else:
        return default
