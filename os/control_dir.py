import os
import shutil

if not os.path.exists('tmp'):
    os.mkdir('tmp')

if not os.path.exists('tmp/test1'):
    os.mkdir('tmp/test1')

try:
    # os.remove() ではディレクトリは削除できない
    os.remove('tmp/test1')
except OSError as e:
    print('os.remove', e)

# os.rmdir() によりディレクトリを削除できる
# ただし、中身が空の場合のみ
os.rmdir('tmp/test1')
os.rmdir('tmp')

# os.makedirs() によりサブディレクトリも含めて一気に作成できる
os.makedirs('tmp/a/b/c/d')

# os.removedirs() によりサブディレクトリも含めて一気に削除できる
# ただし、中身が空の場合のみ
os.removedirs('tmp/a/b/c/d')

os.makedirs('tmp/a/b/c')
print('hello world', file=open('tmp/a/b/c/test.txt', mode='wt'))

try:
    # 削除対象ディレクトリにファイルが存在していると削除できない
    os.removedirs('tmp/a/b/c')
except OSError as e:
    print('os.removedirs', e)

# shutil.rmtree() はファイルが存在していても再帰的に削除できる
shutil.rmtree('tmp')
