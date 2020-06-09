import re

content = r"1234567890"

# \d 任意の数字[0-9]
pattern = "\d"

# regular expressions
repatter = re.compile(pattern)
result = repatter.match(content)

print(result)
print(result.span())
print(result.group())
