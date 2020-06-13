import requests

user = input("> input user: ")
pswd = input("> input pswd: ")

res = requests.get("https://api.github.com/user", auth=(user, pswd))

print(res.status_code)
print(res.headers["content-type"])
print(res.encoding)
print(res.text)
print(res.json())
print(res.content)
