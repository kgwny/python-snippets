import io
import os
import time
import subprocess

# 文字列で与える→shell=True
# ・ クオート混入による誤作動リスク

# 文字列のリストで与える→shell=False (default)
# ・ ワイルドカード等が使えず，低自由度

# 文字列リストで与える方法（以降の5つはこの記法では不可）
print(subprocess.call(['ls','-l'], shell=False)) # 0

# シェルパイプライン
print(subprocess.call('echo -e "a\nb\nc" | wc -l', shell=True)) # 0

# セミコロン
print(subprocess.call('echo Failed.; exit 1', shell=True)) # 1

# ワイルドカード
print(subprocess.call('ls -l *.py', shell=True)) # 0

# 環境変数
print(subprocess.call('echo $HOME', shell=True)) # 0

# HOMEを表すチルダ記号
print(subprocess.call('ls -l ~', shell=True)) # 0
