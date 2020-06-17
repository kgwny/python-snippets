
def add(int1, int2):
    return int1 + int2

integer = add(1, 2)
print(integer)
# 3

def loop_msg(msg, repeat=3):
    for i in range(repeat):
        print(str(i + 1) + ':' + msg)

loop_msg('www')
loop_msg('lmao', repeat=5)
