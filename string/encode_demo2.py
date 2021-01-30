
moji = 'もじれつ'

# utf-8のバイナリへ変換する
moji_utf8 = moji.encode('utf-8')

# moji_utf8をバイナリデータとしてファイルに保存する
with open('./tmp/moji_utf8.txt', 'wb') as f:
    f.write(moji_utf8)

# Shift-JISのバイナリへ変換する
moji_shift = moji.encode('shift-jis')

# moji_shiftをバイナリデータとしてファイルに保存する
with open('./tmp/moji_shift.txt', 'wb') as f:
    f.write(moji_shift)
