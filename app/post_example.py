import requests
import json

url = 'http://localhost:8080/test/'

params = json.dumps({'key': 'hoge', 'value': 'fuga'})
session = requests.session()
res = session.post(url, data=params)
print(res.text)
