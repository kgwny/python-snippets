
utf8_str = 'あ'

utf8_bytes = utf8_str.encode('utf-8')
print(utf8_bytes)
# b'\xe3\x81\x82'

sjis_bytes = utf8_str.encode('sjis')
print(sjis_bytes)
# b'\x82\xa0'

cp932_bytes = utf8_str.encode('cp932')
print(cp932_bytes)
# b'\x82\xa0'

eucjp_bytes = utf8_str.encode('euc_jp')
print(eucjp_bytes)
# b'\xa4\xa2'

jis_bytes = utf8_str.encode('iso2022_jp')
print(jis_bytes)
# b'\x1b$B$"\x1b(B'

print(utf8_bytes.decode('utf-8'))
print(sjis_bytes.decode('sjis'))
print(cp932_bytes.decode('cp932'))
print(eucjp_bytes.decode('euc_jp'))
print(jis_bytes.decode('iso2022_jp'))
# あ