import re

content = r"abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
pattern = "abc"

# regular expressions
repatter = re.compile(pattern)
result = repatter.match(content)

print(result)
print(result.span())
print(result.group())
