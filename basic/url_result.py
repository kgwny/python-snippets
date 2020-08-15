#!/usr/local/bin/python

# change above line to point to local python executable

import urllib.request

# create URL with desired search parameters

url = "http://example.com?param=hoge"

print(url)

# retrieve URL and  write results to filename

filename = "./tmp/result.txt"

urllib.request.urlretrieve(url, filename)

### Done!
