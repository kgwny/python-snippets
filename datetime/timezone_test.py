from datetime import datetime, timedelta, timezone

# JSTタイムゾーンを作成
jst = timezone(timedelta(hours=9), 'JST')

# JSTで、日付を作成
now = datetime.now(jst)
print('JST:', now)
# 出力例：2018-12-06 01:18:21.852966+09:00

# UTCで、日付を作成
now = datetime.now(timezone.utc)
print('UTC:', now)
# 出力例：2018-12-05 16:18:21.854607+00:00
