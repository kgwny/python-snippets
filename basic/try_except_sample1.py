# 1/0の実行時にZeroDivitionError発生
try:
    print(1/0)
except ZeroDivisionError:
    print('ZeroDivisionError detectd.')
