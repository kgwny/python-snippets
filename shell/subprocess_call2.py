import io
import os
import time
import subprocess

print(subprocess.call(['cat', 'hello.py'])) # 0

# 標準入力・標準出力を指定する（2つ目はhello2.pyが作成される）
print(subprocess.call(['cat'], stdin=open('hello.py','rb'))) # 0
print(subprocess.call(['cat', 'hello.py'], stdout=open('hello2.py','wb'))) # 0

# timeoutを指定する
print(subprocess.call(['sleep', '3'], timeout=1)) # TimeoutExpired

#（補足）実行ディレクトリ指定のcwdオプションでも~はサポートされていない．
print(subprocess.call(['ls','-l'], shell=False, cwd = "~")) # FileNotFoundError
