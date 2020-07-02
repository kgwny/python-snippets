import datetime
import calendar

# 現在日付の取得
current_date = datetime.date.today()
print(current_date)

# 現在日時の取得
current_datetime = datetime.datetime.now()
print(current_datetime)

# 年月日を基にして日付を生成する
y=2020
m=7
d=3
generated_d = datetime.date(y, m, d)
print(generated_d)

# 年月日時分を基にして日付を生成する
generated_dt = datetime.datetime(year=2019, month=12, day=31, hour=23, minute=59, second=59)
print(generated_dt)

current_datetime = datetime.datetime.now()
print("year=%s month=%s day=%s week()=%s" % 
    (current_datetime.year,
        current_datetime.month,
        current_datetime.day,
        current_datetime.weekday(),
    )
)

# datetimeを文字列に変換する
str_current_datetime = current_datetime.strftime('%Y-%m-%d %H:%M:%S')
print(str_current_datetime)

# dateを文字列に変換する
str_current_date = current_date.strftime('%Y-%m-%d')
print(str_current_date)

# strptime:文字列をdateオブジェクトへ変換する
str_date = '2020-12-31'
strped_date = datetime.datetime.strptime(str_date, '%Y-%m-%d')
date_date = datetime.date(strped_date.year, strped_date.month, strped_date.day)
print(date_date)
print(type(date_date))

# strptime:文字列をdatetimeオブジェクトへ変換する
str_datetime = '2017-12-01 23:06:19'
tdatetime = datetime.datetime.strptime(str_datetime, '%Y-%m-%d %H:%M:%S')

# 月初を取得する
def get_firstdate(y, m):
    return datetime.date(y, m, 1)

first_date = get_firstdate(2020, 7)
print(first_date)

# 月末を取得する
def get_lastdate(y, m):
    _, days = calendar.monthrange(y, m)
    firstdate = get_firstdate(y, m)
    lastdate = firstdate + datetime.timedelta(days=days - 1)
    return lastdate

last_date = get_lastdate(2020, 7)
print(last_date)

# 月初の週始まり（日曜日）を取得する
def get_first_sunday(y, m):
    firstdate = get_firstdate(y, m)
    from_date = firstdate - datetime.timedelta(days=firstdate.weekday()+1)
    return from_date

first_sunday = get_first_sunday(2020, 7)
print(first_sunday)

# 月末の週終わり（土曜日）を取得する
def get_last_saturday(y, m):
    lastdate = get_lastdate(y, m)
    to_date = lastdate + datetime.timedelta(days=lastdate.weekday())
    return to_date

last_saturday = get_last_saturday(2020, 7)
print(last_saturday)

# 24Hを超える表記の時刻をdatetimeに変換する
def over24Hdatetime(year, month, day, hour, minute):
    # to minute
    minutes = int(hour) * 60 + int(minute)
    dt = datetime.datetime(year=year, month=month, day=day)
    dt += datetime.timedelta(minutes=minutes)    
    return dt

dt14 = over24Hdatetime(2020, 7, 1, 26, 1)
print(dt14)

# 時刻同士の引算を行い、分で値を取得する
def get_minutes(fromdt, todt):
    return (todt - fromdt).seconds / 60

from_dt = datetime.datetime.strptime('2020-06-09 09:00', '%Y-%m-%d %H:%M')
to_dt = datetime.datetime.strptime('2020-06-09 17:30', '%Y-%m-%d %H:%M')

minutes = get_minutes(from_dt, to_dt)
print(minutes)
