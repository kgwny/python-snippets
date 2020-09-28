import re

p = re.compile('[a-z]+')

print(p.fullmatch('abc'))
# True

print(p.fullmatch('abc123'))
# False

ym = re.compile(r'^\d{4}-(0[1-9]|1[0-2])$')

print(ym.fullmatch('999-00'))
print(ym.fullmatch('1000-0'))
print(ym.fullmatch('2020-12'))

if ym.fullmatch('2020-12'):
    print(True)
else:
    print(False)
