# replaceメソッドによる文字列置換
s1 = 'this is a sample string'
s2 = s1.replace('this', 'that')  # replaceメソッドは新しい文字列を返す
print(s1)  # this is a sample string
print(s2)  # that is a sample string

s2 = s1.replace(' ', '')  # 第2引数を空文字列にすると置換前の文字列が削除される
print(s2)  # thisisasamplestring

s1 = 'foo bar baz foo bar baz foo bar baz'
s2 = s1.replace('foo', 'FOO', 2)  # 置換を行う回数を指定
print(s2)  # FOO bar baz FOO bar baz foo bar baz

s2 = s1.replace('foo', 'FOO').replace('bar', 'BAR')  # replaceメソッドを連鎖
print(s2)  # FOO BAR baz FOO BAR baz FOO BAR baz

# maketransメソッドで変換テーブルを作成して、translateメソッドで置換
d = {' ': '_', 't': 'TT', 'a': None}  # ' 'を'_'に、't'を'TT'に、'a'は削除
tbl = str.maketrans(d)  # 辞書dを基に変換テーブルを作成
s1 = 'this is a sample string'
s2 = s1.translate(tbl)
print(s2)  # TThis_is__smple_sTTring

tbl = str.maketrans(' a', '_A')  # 半角空白文字をアンダースコアに、'a'を'A'に
s2 = s1.translate(tbl)
print(s2)  # this_is_A_sAmple_string

tbl = str.maketrans('bcde', 'BCDE', 'a')  # 'b'～'e'を大文字に、'a'は削除
s2 = s1.translate(tbl)
print(s2)  # this is  smplE string

# タブ文字を半角空白文字に置換
s1 = '01\t4\t89'
s2 = s1.expandtabs(4)  # 4タブでタブ文字を半角空白文字に展開
print(s2)  # 01  4   89
