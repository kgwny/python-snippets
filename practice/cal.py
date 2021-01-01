#!/usr/bin/python3

from datetime import datetime, timedelta, timezone
import calendar

import cgi_decode
cgi_decode.Set()

JST = timezone(timedelta(hours=+9), 'JST')
date = datetime.now(JST)

# 年の指定 初期値を当年に
y = int(GET.get('year',date.strftime('%Y')))
# 月の指定 初期値を当月に
m = int(GET.get('month',date.strftime('%m')))

# 指定年月の1日の曜日と月の日数
w1, t1 = calendar.monthrange(y, m)
# 指定年月の前月の日数
(_y, _m) = (y-1, 12) if m < 2 else (y, m-1)
_, t0 = calendar.monthrange(_y, _m)
# 指定年月の月末曜日
w2 = calendar.weekday(y, m, t1)
