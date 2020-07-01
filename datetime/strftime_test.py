import datetime

# datetimeオブジェクト、dateオブジェクトにあるstrftime()メソッドを使うことで
# 日付や時間を任意の書式フォーマットによる文字列へ変換することができる

# %d : 0埋めした10進数で表記した月中の日にち
# %m : 0埋めした10進数で表記した月
# %y : 0埋めした10進数で表記した西暦の下2桁
# %Y : 0埋めした10進数で表記した西暦4桁
# %H : 0埋めした10進数で表記した時 （24時間表記）
# %I : 0埋めした10進数で表記した時 （12時間表記）
# %M : 0埋めした10進数で表記した分
# %S : 0埋めした10進数で表記した秒
# %f : 0埋めした10進数で表記したマイクロ秒（6桁）
# %A : ロケールの曜日名
# %a : ロケールの曜日名（短縮形）
# %B : ロケールの月名
# %b : ロケールの月名（短縮形）
# %j : 0埋めした10進数で表記した年中の日にち（正月が'001'）
# %U : 0埋めした10進数で表記した年中の週番号 （週の始まりは日曜日）
# %W : 0埋めした10進数で表記した年中の週番号 （週の始まりは月曜日）

dt_now = datetime.datetime.now()
print(dt_now.strftime('%Y-%m-%d %H:%M:%S'))
# 2020-07-01 22:31:13

d_today = datetime.date.today()
print(d_today.strftime('%y%m%d'))
# 200701

print(d_today.strftime('%A, %B %d, %Y'))
# Wednesday, July 01, 2020

print(d_today.strftime('%Y年%m月%d日'))
# 2020年07月01日

print('日番号（1年の何日目か / 正月が001）:', d_today.strftime('%j'))
print('週番号（週の始まりは日曜日 / 正月が00）:', d_today.strftime('%U'))
print('週番号（週の始まりは月曜日 / 正月が00）:', d_today.strftime('%W'))
# 日番号（1年の何日目か / 正月が001）: 183
# 週番号（週の始まりは日曜日 / 正月が00）: 26
# 週番号（週の始まりは月曜日 / 正月が00）: 26

week_num_mon = int(d_today.strftime('%W'))
print(week_num_mon)
print(type(week_num_mon))
# 26
# <class 'int'>

# 任意のフォーマットで隔週日付のリストを取得する
d = datetime.date(2020, 7, 1)
td = datetime.timedelta(weeks=2)
n = 4
f = '%Y年%m月%d日'

l = []

for i in range(n):
    l.append((d + i * td).strftime(f))

print(l)
print('\n'.join(l))

l = [(d + i * td).strftime(f) for i in range(n)]
print(l)
