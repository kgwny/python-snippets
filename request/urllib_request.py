import urllib.request

url = 'https://www.google.com/'

# urlopen
res = urllib.request.urlopen(url=url)
print(type(res))
#<class 'http.client.HTTPResponse'>

html = res.read()
print(type(html))
#<class 'bytes'>


# request
req = urllib.request.Request(url)
print(type(req))
#<class 'urllib.request.Request'>

with urllib.request.urlopen(req) as res:
    body = res.read()

#print(type(body))
#<class 'bytes'>
