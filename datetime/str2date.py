import datetime

str_date = '2021-03-31'
target_date = [int(s) for s in str_date.split('-')]
print(target_date)

try:
    date = datetime.date(target_date[0], target_date[1], target_date[2])
except Exception as e:
    print('[ERROR]', e)
    exit(1)
else:
    print(date)
