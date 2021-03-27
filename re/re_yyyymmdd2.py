import re

ymd = re.compile(r'[12]\d{3}[-](0[1-9]|1[0-2])[-](0[1-9]|[12][0-9]|3[01])$')

# OK
print(ymd.fullmatch('2020-01-01'))
print(ymd.fullmatch('2020-01-31'))
print(ymd.fullmatch('2020-12-31'))
print(ymd.fullmatch('2999-12-31'))
print(ymd.fullmatch('2020-02-31')) # 許容

# NG
print(ymd.fullmatch('20200101'))
print(ymd.fullmatch('2020-1-31'))
print(ymd.fullmatch('2020-01-1'))
print(ymd.fullmatch('2020-00-31'))
print(ymd.fullmatch('2020-13-31'))
print(ymd.fullmatch('2020-01-00'))
print(ymd.fullmatch('2020-01-32'))
print(ymd.fullmatch('3020-02-22'))

# NG
print(ymd.fullmatch('9999/99/99'))
print(ymd.fullmatch('2020年1月1日'))
print(ymd.fullmatch('2020/01/23'))
print(ymd.fullmatch('1900/01/23'))
print(ymd.fullmatch('2020/12/11'))
