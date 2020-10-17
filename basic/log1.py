import logging

# logging.basicConfig : rootLoggerの設定ができる
# basicConfig未設定の場合、defaultの出力レベルはlogging.WARNなので、
# debugやinfoのログは出力されない
logging.basicConfig(level=logging.DEBUG, 
    format="%(asctime)s %(levelname)-7s %(message)s")

# ログ出力
logging.debug("debug")
logging.info("info")
logging.warn("warn")
logging.error("error")

# 2020-06-14 22:17:15,649 DEBUG   debug
# 2020-06-14 22:17:15,649 INFO    info
# 2020-06-14 22:17:15,649 WARNING warn
# 2020-06-14 22:17:15,649 ERROR   error
