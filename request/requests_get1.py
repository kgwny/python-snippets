import requests

# @see
# https://requests-docs-ja.readthedocs.io/en/latest/

user = "dont write"
pswd = "dont write"
r = requests.get("https://api.github.com/user", auth=(user, pswd))
print(r.status_code)
print(r.headers["content-type"])
print(r.encoding)
print(r.text)
print(r.json())
