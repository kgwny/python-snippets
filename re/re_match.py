import re

content = r"abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
pattern = "abc"

# regular match
result = re.match("abc", content)

if result:
    print(result)
    print(result.span())
    print(result.group())
else:
    print("none")
