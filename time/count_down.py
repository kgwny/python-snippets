import time

# count down
for i in range(3, 0, -1):
    print('%s %0.2f %0.2f' % (time.ctime(), time.time(), time.clock()))
    print('Sleeping', i)
    time.sleep(i)
