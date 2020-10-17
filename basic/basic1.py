#!/usr/bin/env python

import argparse

def main():
    print('Hello python!')

    parser = argparse.ArgumentParser()

    # -w / --word というオプションを追加．デフォルトは 'hello! '
    parser.add_argument('-w', '--word', default='hello! ')

    # -s / --size というオプションを追加，デフォルトは5で型はint
    parser.add_argument('-s', '--size', default=5, type=int)

    # コマンドラインの引数をパースしてargsに入れる．エラーがあったらexitする
    args = parser.parse_args()

    print(args.word * args.size)

if __name__ == '__main__':
    main()
