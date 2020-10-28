import subprocess
import os

print('メモリ使用量：',subprocess.check_output(["ps", "up", str(os.getpid())]).decode('utf8').split()[16])
