import requests

user=input("> input user: ")
pswd=input("> input pswd: ")

r = requests.get("https://api.github.com/user", auth=(user, pswd))

print(r.status_code)
print(r.headers["content-type"])
print(r.encoding)
print(r.text)
print(r.json())
print(r.content)
