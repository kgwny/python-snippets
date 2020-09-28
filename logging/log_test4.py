import logging

# rootロガーを取得
logger = logging.getLogger()
logger.setLevel(logging.DEBUG)

# 出力のフォーマットを定義
formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')

# sys.stderrへ出力するハンドラーを定義
sh = logging.StreamHandler()
sh.setLevel(logging.DEBUG)
sh.setFormatter(formatter)

# rootロガーにハンドラーを登録する
logger.addHandler(sh)
logger.debug('debugメッセージ')
logger.info('infoメッセージ')
logger.warn('warnメッセージ')
logger.error('errorメッセージ')
logger.critical('criticalメッセージ')
