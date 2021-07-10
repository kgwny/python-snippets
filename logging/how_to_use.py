import sys
import io
import argparse
import logging
import locale

sys.stdin = io.TextIOWrapper(sys.stdin.buffer, encoding='utf-8')
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.buffer, encoding='utf-8')

def setup_logger(log_file):
    logger = logging.getLogger()
    logger.setLevel(logging.DEBUG)

    formatter = logging.Formatter(
        fmt='%(asctime)s.%(msecs)-3d [%(levelname)s] %(filename)s:%(lineno)d %(funcName)s - %(message)s',
        datefmt='%Y-%m-%d %H:%M:%S'
    )

    sh = logging.StreamHandler()
    sh.setLevel(logging.INFO)
    sh.setFormatter(formatter)
    logger.addHandler(sh)

    fh = logging.FileHandler(log_file)
    fh.setLevel(logging.DEBUG)
    fh.setFormatter(formatter)
    logger.addHandler(fh)

def main():
    locale.setlocale(locale.LC_ALL, 'en_US.UTF-8')
    setup_logger('log_example.txt')

    parser = argparse.ArgumentParser(
        description='This tool is hogehoge.',
        formatter_class=argparse.RawTextHelpFormatter
    )
    parser.add_argument('--flag', action='store_true', help='flag.')
    parser.add_argument('val', help='something value')
    args = parser.parse_args()

    logging.info('flag = ' + str(args.flag))
    logging.info('val = ' + args.val)

if __name__ == '__main__':
    main()

## 実行例・引数ありパターン
# $ python3 how_to_use.py --flag aaa
# 2021-07-10 20:16:06.786 [INFO] how_to_use.py:42 main - flag = True
# 2021-07-10 20:16:06.786 [INFO] how_to_use.py:43 main - val = aaa

## 実行例・引数なしパターン
# $ python3 how_to_use.py
# usage: how_to_use.py [-h] [--flag] val
# how_to_use.py: error: the following arguments are required: val

# logging --- Python 用ロギング機能
# https://docs.python.org/ja/3/library/logging.html

