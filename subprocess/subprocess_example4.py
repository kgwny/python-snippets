import subprocess
from subprocess import PIPE

# line_in.txtに記述している内容を読み込み、
# 行番号を付与してline_out.txtへ書き込む
proc = subprocess.run('cat line_in.txt | cat -n > line_out.txt', shell=True, text=True)
