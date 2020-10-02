# 標準入力

# 文字列
s = input()
print('This is ' + s + '.')

# 整数値
num = int(input())
print('This is ' + str(num) + '.')

# 2つ以上の整数
a, b = map(int, input().split())
print('print:', a, b)

# list
li1 = list(map(int, input().split()))
print('print:', li1)

# n行に１つずつ入力される整数
n = 2 # ここでは2行入力してみる
li2 = [int(input()) for _ in range(n)]
print('print:', li2)
