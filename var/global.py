# グローバル変数
def func():
    global x
    print(x)
    # 1
    x = 2

x = 1
func()
print(x)
# 2
