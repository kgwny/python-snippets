def check(x):
    if x == 1:
        print('x = 1')
    elif x == 2:
        print('x = 2')
    else:
        pass

def loop(x):
    y = x
    while True:
        print(y)
        y = y + 1
        if y == 10:
            break

check(1)
# x = 1

check(2)
# x = 2

loop(1)
