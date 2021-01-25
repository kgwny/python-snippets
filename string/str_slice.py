# 文字列操作・スライス
my_str = "01234"

# 文字列から特定の位置を切り出す
#[(start):(end):(step)]

print(my_str[2:4])
# 23
print(my_str[0:5:2])
# 024
print(my_str[:3])
# 012
print(my_str[3:])
# 34
print(my_str[::-1])
# 43210 逆順になる
