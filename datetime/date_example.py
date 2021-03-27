import datetime

# 日付計算

from_date = datetime.date(2021, 3, 31)
print(type(from_date))
print(from_date)

# from 〜 to を3日間としたいとき
interval = 3
to_date = from_date + datetime.timedelta(days=interval-1)
print(type(to_date))
print(to_date)

# 文字列への変換

date = str(from_date)
print(type(date))
print(date)
