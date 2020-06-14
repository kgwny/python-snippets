import logging
import traceback

logging.basicConfig(level=logging.DEBUG, 
    format="%(asctime)s %(levelname)-7s %(message)s")
logger = logging.getLogger(__name__)
consoleHandler = logging.StreamHandler()
logger.addHandler(consoleHandler)

try:
    raise Exception
except:
    traceback.print_exc()
