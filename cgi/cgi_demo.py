import cgitb

# https://docs.python.org/ja/3/library/cgi.html

cgitb.enable()
cgitb.enable(display=0, logdir='/path/to/logdir')

print('Content-Type: text/html')
print()
print('<html>')
print('<head>')
print('<title>python cgi script test</title>')
print('</head>')
print('<body>')
print('<h1>Hello, world!</h1>')
print('こんにちは、世界！')
print('</body>')
print('</html>')
