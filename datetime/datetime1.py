import datetime

# 現在時刻を取得
now = datetime.datetime.now() 

# 現在の年を取得
now_year = str(now.year).zfill(4)

# 現在の月を取得
now_month = str(now.month).zfill(2)

# 現在の日を取得
now_day = str(now.day).zfill(2)

# 現在の時を取得
now_hour = str(now.hour).zfill(2)

# 現在の分を取得
now_minute = str(now.minute).zfill(2)

# 現在の秒を取得
now_second = str(now.second).zfill(2) 

print(now_year , now_month , now_day, now_hour , now_minute , now_second)   
