import time

print('gmtime    : ' + str(time.gmtime()))
print('localtime : ' + str(time.localtime()))
print('mktime    : ' + str(time.mktime(time.localtime())))

t = time.localtime()

print('Day of month : ', t.tm_mday)
print('Day of week  : ', t.tm_wday)
print('Day of year  : ', t.tm_yday)
