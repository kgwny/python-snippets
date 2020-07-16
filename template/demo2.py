#!/usr/bin/env python

from tqdm import tqdm
import time

# pip install tqdm
# プログレスバー表示

def main():
    for i in tqdm(range(100)):
        time.sleep(0.02)

    for i in tqdm([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]):
        time.sleep(0.02)

    for i in tqdm('hogehoge'):
        time.sleep(0.02)

    bar = tqdm(total = 1000)
    for i in range(100):
        bar.update(10)
        time.sleep(0.02)

    bar = tqdm(total = 1000)
    bar.set_description('Progress rate')
    for i in range(100):
        bar.update(10)
        time.sleep(0.02)

if __name__ == '__main__':
    main()
