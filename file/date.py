from pathlib import Path
import datetime

p = Path(r'./tmp/aaa.txt')

# 作成日
create_time = datetime.datetime.fromtimestamp(p.stat().st_ctime)
# 更新日
update_time = datetime.datetime.fromtimestamp(p.stat().st_mtime)
# アクセス日
access_time = datetime.datetime.fromtimestamp(p.stat().st_atime)

print('作成日:', create_time.strftime('%Y-%m-%d %H:%M:%S'))
print('更新日:', update_time.strftime('%Y-%m-%d %H:%M:%S'))
print('アクセス日:', access_time.strftime('%Y-%m-%d %H:%M:%S'))
