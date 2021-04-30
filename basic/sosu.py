# 素数を取得する
factors = [2, 3]

for num in range(2, 100):
    i = 2
    while i<= num:
        if (num%i==0):
            break
        elif (i == int(num / 2)):
            factors.append(num)
        i += 1

print(factors)
