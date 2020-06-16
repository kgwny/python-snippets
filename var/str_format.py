
errmsg = 'random error'
errcode = 65535

print('ERROR: %s (%d)' % (errmsg, errcode))
# ERROR: random error (65535)

# '%s' : 文字列
# '%d' : 整数
# '%f' : 浮動小数点数
# '%x' : 16進数
# '%o' : 8進数
# '%%' : %を表す

print('%s' % 'abc')
# abc

print('%d' % 255)
# 255

print('%f' % 2.55)
# 2.55

print('%x' % 255)
# ff

print('%o' % 255)
# 377

print('%%%s' % '文字')
# %文字

print('|%5s|' % 'abc')
# |  abc| : 右寄せ5文字分

print('|%-5s|' % 'abc')
# |abc  | : 左寄せ5文字分

print('|%5d|' % 123)
# |  123| : 右寄せ5桁

print('|%-5d|' % 123)
# |123  | : 左寄せ5桁

print('|%+5d|' % 123)
# | +123| : ±符号付き

print('|%5.2f|' % 1.23)
# | 1.23| : 全体桁数.少数点以下の桁数

print('|%05d|' % 123)
# |00123| : 0埋め
