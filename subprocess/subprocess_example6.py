import time
import subprocess
from subprocess import PIPE

# 非同期処理を実現するにはPopenの実行時に名前付きパイプを使う
# ファイルに一度書き出しをしても実現可能だが
# 書き出す量が多い時には書き出しが終わるまでの時間を要する

# my_pipeという名前でパイプを作成
# $ mkfifo my_pipe

s = 'hoge piyo huga'
proc = subprocess.Popen('cat {} | cat -n; sleep 10'.format('my_pipe'), shell=True, stdout=PIPE, stderr=PIPE, text=True)
with open('my_pipe', 'w') as fifo:
    fifo.write(s)

# サブプロセスが処理終わるまでの間に、並列で別の重い処理
time.sleep(10)

# サブプロセスの完了を待つ
result = proc.communicate()
(stdout, stderr) = (result[0], result[1])
print('stdout: {}'.format(stdout))
# stdoutT:  1  hoge piyo huga
