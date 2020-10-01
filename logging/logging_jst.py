import logging
from datetime import datetime, timedelta, timezone

# JSTタイムゾーンを作成
jst = datetime.now(timezone(timedelta(hours=9), 'JST'))
print('jst:', jst)

def custom_time(*args):
    return datetime.now(timezone(timedelta(hours=9), 'JST')).timetuple()

logging.Formatter.converter = custom_time

formatter = '%(asctime)s [%(levelname)s]　%(filename)s:%(lineno)d %(funcName)s - %(message)s'
logging.basicConfig(
    format=formatter,
    datefmt='%Y-%m-%d %H:%M:%S',
    level=logging.INFO
)

logging.info('hello')
