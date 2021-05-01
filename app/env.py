import os
import re

print("Content-type: text/html")
header = """
<html>
<head>
<title>環境変数一覧表</title>
</head>
<body>
<table align="center" border="1" bordercolor="00cc66" cellspacing="0">
"""

content = ""
for key, value in os.environ.items():
    # value = re.sub("\w", "*", value)            #サンプルのため非表示
    line = "<tr><td>%s</td><td>%s</td></tr>\n" % (key, value)
    content = content + line

footer = """</table>
</body>
</html>
"""

print(header + content + footer)
