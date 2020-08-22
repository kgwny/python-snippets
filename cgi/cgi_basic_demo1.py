#!/usr/bin/env python
# -*- coding: utf-8 -*-
 
import cgi
import cgitb
cgitb.enable()
 
print("Content-Type: text/html")
print("")
print("<html><head>")
print("<title>CGI script output</title>")
print("</head><body>")
print("<h1>This is my first CGI script</h1>")
print("Hello, world!")
print("</body></html>")
