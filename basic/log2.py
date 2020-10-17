#!/usr/bin/env python

import datetime

def log(*args):
    msg = ' '.join(map(str, [datetime.datetime.now(), '>'] + list(args)))
    print(msg)
    with open('log.txt', 'at') as fd: fd.write(msg + '\n')

def main():
    log('generated', 5, 'items')

if __name__ == '__main__': main()
