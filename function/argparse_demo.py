import argparse
# argparseをインポート

# parserを生成する
parser = argparse.ArgumentParser(description='このプログラムの説明')

# parser.add_argumentで受け取る引数を追加していく
# ※arg1,2,3,4があるとする

# 必須の引数を追加する
parser.add_argument('arg1', help='この引数の説明')
# オプションの引数を追加する
parser.add_argument('arg2', help='foooo')
parser.add_argument('--arg3')
# よく使う引数の省略形の定義を追加する
parser.add_argument('-a', '--arg4')

# 引数を解析する
args = parser.parse_args()

print('arg1='+args.arg1)
print('arg2='+args.arg2)
print('arg3='+args.arg3)
print('arg4='+args.arg4)
