import logging

logger = logging.getLogger()
logger.setLevel(logging.DEBUG)

formatter = logging.Formatter(
    fmt='%(asctime)s.%(msecs)-3d [%(levelname)s] %(filename)s:%(lineno)d %(funcName)s - %(messgage)s',
    datefmt='%Y-%m-%d %H:%M:%S'
)

# stream 標準出力
sh = logging.StreamHandler()
sh.setLevel(logging.INFO)
sh.setFormatter(formatter)
logger.addHandler(sh)

# file 標準ファイル出力
fh = logging.FileHandler('logfile.txt')
fh.setLevel(logging.DEBUG)
fh.setFormatter(formatter)
logger.addHandler(fh)
