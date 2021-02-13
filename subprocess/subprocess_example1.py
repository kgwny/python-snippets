import subprocess
from subprocess import PIPE

# dateコマンドを実行する
# subprocess.run()により同期処理を実行する
# サブプロセスで処理を実行し、終わるまで待つ場合はsubprocess.runを使う
proc = subprocess.run('date', shell=True, stdout=PIPE, stderr=PIPE, text=True)
date = proc.stdout
print('STDOUT: {}'.format(date))

# STDOUT: 現在の日付: 2021/02/13 
# 新しい日付を入力してください: (年-月-日) 

# shell=True
# 文字列からの解析をモジュールに任せることができます。 
# この設定はコマンドラインから実行して使うために必要です。
