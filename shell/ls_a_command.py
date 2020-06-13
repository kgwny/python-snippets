import subprocess, sys
from subprocess import PIPE

proc = subprocess.run(["ls", "-a"])
if proc.returncode != 0:
    print("ls failed", file=sys.stderr)
    sys.exit(1)
