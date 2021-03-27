import datetime

# 日付計算

now = datetime.datetime(2021, 3, 31)
print(now)
# => datetime.datetime(2019, 8, 2, 1, 59, 33, 338054)

# 1週 加算
print(now + datetime.timedelta(weeks=1))
# => datetime.datetime(2019, 8, 9, 1, 59, 33, 338054)

# 1日 減算
print(now + datetime.timedelta(days=1))
# => datetime.datetime(2019, 7, 23, 1, 59, 33, 338054)

# 10時間 加算
now + datetime.timedelta(hours=10)
# => datetime.datetime(2019, 8, 2, 11, 59, 33, 338054)

# 10分 減算
now - datetime.timedelta(minutes=10)
# => datetime.datetime(2019, 8, 2, 1, 49, 33, 338054)

# 10秒 加算
now + datetime.timedelta(seconds=10)
# => datetime.datetime(2019, 8, 2, 1, 59, 43, 338054)

# 7日, 1時間, 10分 加算
now + datetime.timedelta(days=7, hours=1, seconds=10)
# => datetime.datetime(2019, 8, 9, 2, 59, 43, 338054)
