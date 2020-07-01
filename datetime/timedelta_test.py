import datetime

# timedeltaオブジェクトは2つの日時の時間差、経過時間を表す
# 日数、秒数、マイクロ秒数の情報を保持しており、
# 属性days, seconds, microsecondsでアクセスできる
# また、total_seconds()メソッドでトータルの秒数を取得できる

# timedeltaオブジェクトのコンストラクタ
delta = datetime.timedelta(days=0, seconds=0, microseconds=0, milliseconds=0, minutes=0, hours=0, weeks=0)
print(delta)
# 0:00:00

print(type(delta))
# <class 'datetime.timedelta'>


# deltatimeオブジェクト同士を引算して得た結果は、timedeltaオブジェクトとなる
dt_now = datetime.datetime.now()
dt_old = datetime.datetime(2020, 6, 30, 12, 00,00)

td = dt_now - dt_old
print(td)
# 1 day, 10:40:35.351313

print(type(td))
# <class 'datetime.timedelta'>

print(td.days)
# 1

print(td.seconds)
print(td.microseconds)
print(td.total_seconds())

td_1w = datetime.timedelta(weeks=1)
print(td_1w)
# 7 days, 0:00:00

print(td_1w.days)
# 7


# 1週間前
d_1w = dt_now - td_1w
print(d_1w)
# 2018-01-26

# 10日
td_10d = datetime.timedelta(days=10)
print(td_10d)
# 10 days, 0:00:00

# 10日後
dt_10d = dt_now + td_10d
print(dt_10d)

# 50分
td_50m = datetime.timedelta(minutes=50)
print(td_50m)
# 0:50:00

print(td_50m.seconds)
# 3000

# 50分後
dt_50m = dt_now + td_50m
print(dt_50m)


# 特定の日付まで何日あるか？
d_today = datetime.date.today()
d_target = datetime.date(2020, 7, 24)
td = d_target - d_today
print(td)
print(td.days)
