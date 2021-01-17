import re

match = re.search(r'<b>(.+)</b>', 'This is a <b>nice</b> pen')
if match:
    print(match.group(0))  # 検索パターン全体に一致する文字列
    print(match.group(1))  # 検索パターン中の括弧で囲まれた部分に一致する文字列

match = re.search(r'【(.+)】', 'This is a 【pen】.')
if match:
    print(match.group(0))  # 検索パターン全体に一致する文字列
    print(match.group(1))  # 検索パターン中の括弧で囲まれた部分に一致する文字列
