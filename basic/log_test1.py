import logging
import traceback

logging.basicConfig(level=logging.DEBUG, 
    format="%(asctime)s %(levelname)-7s %(message)s")
logger = logging.getLogger(__name__)
consoleHandler = logging.StreamHandler()
logger.addHandler(consoleHandler)

try:
    f = open('hoge.txt')
except Exception as e:
    print(e)
    logging.error('hoge.txtが存在しません！！！', exc_info=True)

try:
    raise Exception
except:
    traceback.print_exc()
