import os
import pathlib
from zipfile import ZipFile

src_dir = 'src'

# create dir
os.makedirs(src_dir, exist_ok=True)

src_file = 'hoge.txt'

# create file
target_path = pathlib.Path(src_dir + '/' + src_file)
target_path.touch()

target_zip = 'washigasodateta.zip'

# create zip
#with ZipFile(target_zip, 'w') as myzip:
#    myzip.write(src_dir)
