import os
import shutil

target_dir = 'tmp'

os.makedirs(target_dir, exist_ok=True)

target_file = 'hoge.txt'

with open(target_dir + '/' + target_file, 'w') as f:
    f.write('foo bar baz')

if os.path.exists(target_dir + '/' + target_file):
    print('file created')

# force delete
shutil.rmtree(target_dir)

if not os.path.exists(target_dir):
    print('dir deleted')
