import logging

formatter = '%(asctime)s [%(levelname)s]　%(filename)s:%(lineno)d %(funcName)s - %(message)s'
logging.basicConfig(format=formatter, datefmt='%Y-%m-%d %H:%M:%S', level=logging.INFO)

logging.info('hello')
