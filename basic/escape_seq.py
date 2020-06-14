
# エスケープシーケンス

# \改行 : バックスラッシュと改行(\newline)
var = '\
文字\
\
'
print(var)

# \\ : バックスラッシュ(\)
var = '\\'
print(var)

# \' : シングルクォート(')
var = '\''
print(var)

# \" : ダブルクォート(")
var = '\"'
print(var)

# \a : ASCII 端末ベル (BEL)
var = '\a'
print(var)

# \b : ASCII バックスペース(BS)
var = '\b'
print(var)

# \f : ASCII フォームフィード(FF)
var = '\f'
print(var)

# \n : ASCII 改行(LF)
var = '\n'
print(var)

# \r : ASCII 復帰(CR)
var = '\r'
print(var)

# \t : ASCII 垂直タブ(VT)
var = '\t'
print(var)

# \U : ユニコード文字
var = U'\U00003042'
print(var)
# あ

# \N{name} : Unicode で名前 name を持つ文字
var = u'\N{HIRAGANA LETTER A}'
print(var)
# あ

# ex
var = 'a\tb\nA\tB'
print(var)
# a b
# A B

# エスケープシーケンス無効化

# raw文字列 : r もしくは R を付与する
var = r'a\tb\nA\tB'
print(var)

var = R'a\tb\nA\tB'
print(var)

# バックスラッシュ付与
var = 'a\\tb\\nA\\tB'
print(var)

# \ooo : 8進数(0〜7)を持つASCII文字

# \xnn : 16進数(0〜f)を持つASCII文字
