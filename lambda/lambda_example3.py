from math import copysign

num_list = [1, -2, 3, -4, 5, -6, 7]

def func(n):
    return int(copysign(n**2, n))
    # return n ** 2 * [1, -1][n < 0] と同義

result1 = list(map(func, num_list))
print(result1)
# [1, -4, 9, -16, 25, -36, 49]

# 関数をlambdaに置き換える
result2 = list(map(lambda x: int(copysign(x**2, x)), num_list))
print(result2)
# [1, -4, 9, -16, 25, -36, 49]
