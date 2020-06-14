import os
import pathlib
import zipfile

src_dir = 'src'

# create dir
os.makedirs(src_dir, exist_ok=True)

src_file = 'hoge.txt'

# create file
target_path = pathlib.Path(src_dir + '/' + src_file)
target_path.touch()

target_zip = 'archive.zip'

# create zip
with zipfile.ZipFile(target_zip, 'w', compression=zipfile.ZIP_DEFLATED) as myzip:
    myzip.write('src/hoge.txt', arcname='src/hoge.txt')
