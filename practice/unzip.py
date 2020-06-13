from zipfile import ZipFile

target_zip = 'archive.zip'

with zipfile.ZipFile(target_zip) as zf:
    zf.extractall()
