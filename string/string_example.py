
string = """
複数行に渡る文字列を変数に代入したいときは
ダブルクォーテーションで囲みます。
"""
print(string)

string = """\
複数行に渡る文字列は改行についてもそのまま反映されます。
改行を消したい場合はバックスラッシュを使用することで消去できます。
"""
print(string)

string = "埋め込み文字列だよ"

string_f = f"""
フォーマット済みの文字列リテラルにも使用することができます。
str:{string}
"""
print(string_f)
