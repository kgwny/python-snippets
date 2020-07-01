import datetime

# datetimeオブジェクト
now = datetime.datetime.now()
print(now)
print(type(now))
# <class 'datetime.datetime'>

print("年:" + str(now.year))
print("月:" + str(now.month))
print("日:" + str(now.day))
print("時:" + str(now.hour))
print("分:" + str(now.minute))
print("秒:" + str(now.second))
print("マイクロ秒:" + str(now.microsecond))


# datetimeオブジェクトのコンストラクタ
# datetime(year, month, day, hour=0, minute=0, second=0, microsecond=0, tzinfo=None)

# 2020-07-01 00:00:00.0
dt_sample = datetime.datetime(2020, 7, 1, hour=0, minute=0, second=0, microsecond=0, tzinfo=None)
print(dt_sample)

dt_full = datetime.datetime(2020, 7, 2, 19, 1, 10, 5000)
print(dt_full)
# 2020-07-02 19:01:10.005000

print(dt_full.minute)
# 1

print(dt_full.microsecond)
# 5000

yesterday = datetime.datetime(2020, 6, 30)
print(yesterday)
# 2020-06-30 00:00:00

print(yesterday.minute)
# 0


# dateオブジェクト
d_today = datetime.date.today()
print(d_today)
# 2018-02-02

print(type(d_today))
# <class 'datetime.date'>

print(d_today.year)
# 2018

# dateオブジェクトのコンストラクタ
dt_old = datetime.date(2010, 12, 31)
print(dt_old)
# 2010-12-31

print(dt_old.year)
# 2010


# timeオブジェクト
t_now = datetime.time()
print(t_now)
# 00:00:00
print(type(t_now))
# <class 'datetime.time'>

# timeオブジェクトのコンストラクタ
t = datetime.time(hour=0, minute=0, second=0, microsecond=0, tzinfo=None)
print(t)

print(t.hour)
# 0
