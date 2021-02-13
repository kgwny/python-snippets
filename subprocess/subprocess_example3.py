import subprocess
from subprocess import PIPE

IN_FILE = 'input.txt'
OUT_FILE = 'output.txt'

# インプットファイルに記述されている値を取得して処理を行い、
# アウトプットファイルへ結果を記述する
with open(IN_FILE) as input_file:
    with open(OUT_FILE, 'w') as output_file:
        proc = subprocess.run('cat -n', shell=True, stdin=input_file, stdout=output_file, text=True)
