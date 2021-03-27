import re

# 厳密ではなく、ややファジーな仕上がり
ymd = re.compile(r'^\d{4}-(0[1-9]|1[0-2])-(0[1-9]|1[0-9]|2[0-9]|3[0-1])$')

print(ymd.fullmatch('2020-01-00'))
print(ymd.fullmatch('2020-01-01'))
print(ymd.fullmatch('2020-01-09'))
print(ymd.fullmatch('2020-01-10'))
print(ymd.fullmatch('2020-01-19'))
print(ymd.fullmatch('2020-01-20'))
print(ymd.fullmatch('2020-01-29'))
print(ymd.fullmatch('2020-01-30'))
print(ymd.fullmatch('2020-01-31'))
print(ymd.fullmatch('2020-01-32'))

print(ymd.fullmatch('2020-12-00'))
print(ymd.fullmatch('2020-12-01'))
print(ymd.fullmatch('2020-12-31'))
print(ymd.fullmatch('2020-12-32'))
print(ymd.fullmatch('2020-13-00'))
print(ymd.fullmatch('2020-13-31'))
