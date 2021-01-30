moji = 'もじ'

# utf-8の文字コードをバイナリへ変換する
moji_utf8 = moji.encode('utf-8')
print(type(moji_utf8))
print(moji_utf8)

# バイナリをutf-8のstr型へ変換する
moji_str = moji_utf8.decode('utf-8')
print(type(moji_str))
print(moji_str)

# バイナリをリトルエンディアンで整数化する
moji_int = int.from_bytes(moji_utf8, 'little')
print(type(moji_int))
print(moji_int)
