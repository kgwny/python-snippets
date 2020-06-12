import subprocess, sys
from subprocess import PIPE

cp = subprocess.run(["ls", "-a"])
if cp.returncode != 0:
    print("ls failed", file=sys.stderr)
    sys.exit(1)
