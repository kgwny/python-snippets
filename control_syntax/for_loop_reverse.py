# forループの昇順と降順

str_list = ['hoge', 'foo', 'piyo']

# ふつうのforループ
for str in str_list:
    print(str)

# hoge
# foo
# piyo

# 逆順に走るforループ
for str in reversed(str_list):
    print(str)

# piyo
# foo
# hoge
