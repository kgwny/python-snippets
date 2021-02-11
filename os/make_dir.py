import os
import glob

wk_dir = os.getcwd()
print('work_dir:', wk_dir)

target_dir = 'tmp'

if not os.path.exists(target_dir):
    os.mkdir(target_dir)

# change dir: target_dir
os.chdir(target_dir)

wk_dir = os.getcwd()
print('work_dir:', wk_dir)

ls = glob.glob('.')

for f in ls:
    print(f)
