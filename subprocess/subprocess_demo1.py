import subprocess
import sys

cp = subprocess.run(['ls', '-a'])

if cp.returncode != 0:
    print('ls failed.', file=sys.stderr)
    sys.exit(1)
