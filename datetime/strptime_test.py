import datetime

# datetimeのstrptime()を使うと、日付や時刻を表す文字列からdatetimeオブジェクトを生成できる
# 元の文字列に対応する書式化文字列を指定する必要がある

date_str = '2020/7/1 12:30'
date_dt = datetime.datetime.strptime(date_str, '%Y/%m/%d %H:%M')
print(date_dt)
# 2020-07-01 12:30:00

print(type(date_dt))
# <class 'datetime.datetime'>

print(date_dt.strftime('%Y年%m月%d日 %H時%M分'))
# 2020年07月01日 12時30分


date_str = '2020年7月1日'
date_format = '%Y年%m月%d日'
td_10_d = datetime.timedelta(days=10)

# 10日前
date_dt = datetime.datetime.strptime(date_str, date_format)
date_dt_new = date_dt - td_10_d
date_str_new = date_dt_new.strftime(date_format)

print(date_str_new)
# 2020年06月21日
