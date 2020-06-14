from zipfile import ZipFile

target_zip = 'archive.zip'

with ZipFile(target_zip) as zf:
    zf.extractall()
