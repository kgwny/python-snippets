s = 'hoge ika tako'

width = 20

s1 = s.ljust(width)
s2 = s.rjust(width)
s3 = s.center(width)

print("'" + s1 + "'")
print("'" + s2 + "'")
print("'" + s3 + "'")
# 'hoge ika tako       '
# '       hoge ika tako'
# '   hoge ika tako    '

print("'" + s3.lstrip() + "'")
print("'" + s3.rstrip() + "'")
print("'" + s3.strip() + "'")
# 'hoge ika tako    '
# '   hoge ika tako'
# 'hoge ika tako'
