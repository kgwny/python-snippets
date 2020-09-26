from logging import basicConfig, getLogger, INFO

# メインのファイルのみに記述する
formatter='%(asctime)s,%(msecs)d %(levelname)-8s [%(filename)s:%(lineno)d:%(funcName)s] - %(message)s'
basicConfig(format=formatter, datefmt='%Y-%m-%d %H:%M:%S', level=INFO)

# すべてのファイルに記述する
logger = getLogger(__name__)

logger.info('hello')
