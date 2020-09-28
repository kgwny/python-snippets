import re

ym = re.compile(r'^\d{4}-(0[1-9]|1[0-2])$')

print(ym.fullmatch('999-00'))
print(ym.fullmatch('1000-00'))
print(ym.fullmatch('1000-01'))
print(ym.fullmatch('1000-12'))
print(ym.fullmatch('1000-13'))
print(ym.fullmatch('2020-12'))
