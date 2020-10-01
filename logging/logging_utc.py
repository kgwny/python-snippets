import logging
from datetime import datetime, timedelta, timezone

# UTCで日付を作成
utc = datetime.now(timezone.utc)
print('utc:', utc)

def custom_time(*args):
    return datetime.now(timezone.utc).timetuple()

logging.Formatter.converter = custom_time

formatter = '%(asctime)s [%(levelname)s]　%(filename)s:%(lineno)d %(funcName)s - %(message)s'
logging.basicConfig(
    format=formatter,
    datefmt='%Y-%m-%d %H:%M:%S',
    level=logging.INFO
)

logging.info('hello')
