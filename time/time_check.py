import time

# 時間を解析して整形する
now = time.ctime()
print(now)

parsed = time.strptime(now)
print(parsed)
# time.struct_time

print(time.strftime("%a %b %d %H:%M:%S %Y", parsed))

# time.time()
print('The time is : ' + str(time.time()))

# later
later = time.time() + 15
print('15 secs from now : ' + time.ctime(later))
