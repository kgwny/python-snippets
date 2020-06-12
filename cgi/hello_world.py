import cgitb

# https://docs.python.org/ja/3/library/cgi.html

cgitb.enable()
cgitb.enable(display=0, logdir="/path/to/logdir")

print("Content-Type: text/html")    # HTML is following
print()                             # blank line, end of headers

print("<TITLE>CGI script output</TITLE>")
print("<H1>This is my first CGI script</H1>")
print("Hello, world!")
