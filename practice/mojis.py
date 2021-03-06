mojis = """
書き方はダブルクォーテーションで
文章を囲めばOKです。
"""
print(mojis)

# => 書き方はダブルクォーテーションで
# => 文章を囲めばOKです。

mojis = """\
改行もそのまま反映されるため、先頭行の改行を消したい場合は
バックスラッシュを使用すると消えます。
"""
print(mojis)
# => 改行もそのまま反映されるため、先頭行の改行を消したい場合は
# => バックスラッシュを使用すると消えます。

mojis_f = f"""
後述するフォーマット済み文字列リテラルにも応用が利きます。
mojis:{mojis}
"""

print(mojis_f)

# => 後述するフォーマット済み文字列リテラルにも応用が利きます。
# => mojis:改行もそのまま反映されるため、先頭行の改行を消したい場合は
# => バックスラッシュを使用すると消えます。

name = "田中"

# 文字列の前にfを記述します。
message = f"あなたの名前は{name}です。"
print(message)
# => あなたの名前は田中です。

x, y, z = (1, 2, 3)
print(x)
print(y)
print(z)
# => 1
# => 2
# => 3
