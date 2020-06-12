import urllib.request

url = "https://www.google.com/"

# get
r = urllib.request.urlopen(url=url)
print(r)
print(r.headers["content-type"])
print(r.json())
