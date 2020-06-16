
# byte列から文字列へ変換する
byte_str = b"\xe3\x81\x82"
utf8_str = byte_str.decode()
print(type(utf8_str))
print(utf8_str)

# 文字列からbyte列へ変換する
utf8_str = "あ"
byte_str = utf8_str.encode()
print(type(byte_str))
print(byte_str)
