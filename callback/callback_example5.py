# callback:コールバック関数
def showResult(a, b, callback): 
    c = callback(a, b)
    print(c)
    
def add(a, b):
    return a + b

# 第3引数として関数オブジェクトaddを渡す
showResult(3, 4, add)
# 7

# 第3引数として無名関数を渡す
showResult(3, 4, lambda a, b : a + b)
# 7
