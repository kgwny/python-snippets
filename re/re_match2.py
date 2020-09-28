import re

pattern = r'\d{4}-\d{2}'
string = '2020-01-31'

result = re.match(pattern, string)

if result:
    print(result)
    print(result.span())
    print(result.group())
else:
    print('none')

print(re.match(pattern, string).group())
