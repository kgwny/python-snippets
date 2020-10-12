import chardet
import urllib.request

rawdata = urllib.request.urlopen('https://www.yahoo.co.jp/').read()
chardet.detect(rawdata)
