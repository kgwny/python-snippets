# lambda記法
# lambda 引数: 返り値

# lambdaにより実現したきことはこれと一緒
# def func(引数):
#     return 返り値

n = 2

def double(n):
    return n * 2

print(double(n))
# 4

lambda_n = lambda n: n * 2

print(lambda_n(n))
# 4
