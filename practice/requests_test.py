import requests, lxml.html

res = requests.get("https://yahoo.co.jp/")
root = lxml.html.fromstring(res.text).getroottree()

for i in root.xpath('//a[@class="titleLink"]'):
    if "ニュース" in i.text:
        print(i.text)
