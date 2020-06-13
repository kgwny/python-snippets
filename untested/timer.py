from time import sleep

limit = 10

def timer(secs):
    for i in range(0, secs):
        print(i)
        sleep(1)
    print('time over')

timer(limit)
