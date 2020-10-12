import urllib.request
import cchardet

url = 'https://www.example.com/files/something1.txt' # Shift_JIS
# url = 'https://www.example.com/files/something2.txt' # UTF-8

with urllib.request.urlopen(url) as f:
    byte = f.read()
    html = byte.decode(cchardet.detect(byte)['encoding'])
    print(html)
