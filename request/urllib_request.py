import urllib.request

url = "https://www.google.com/"

# get
res = urllib.request.urlopen(url=url)
html = res.read()
print(html)
