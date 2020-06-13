import os
import logging
import sys

def make_dir(target_dir):
    if not os.path.exists(target_dir):
        os.makedirs(target_dir)

def main():
    logging.basicConfig(
        format='%(asctime)s,%(msecs)d %(levelname)-8s [%(filename)s %(lineno)d %(funcName)s] - %(message)s', 
        datefmt='%Y-%m-%d:%H:%M:%S',
        level=logging.INFO)

    logging.info('start main')

    dir_name = sys.argv[1]
    make_dir(dir_name)

    logging.info('end main')

if __name__ == '__main__':
    main()
