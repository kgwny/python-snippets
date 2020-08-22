#!/usr/bin/env python
# -*- coding: utf-8 -*-
 
import cgi
import cgitb
cgitb.enable()
 
print("Content-Type: text/html; charset=utf-8")
print("")
 
form = cgi.FieldStorage()
if "name" not in form or "addr" not in form:
  print("<h1>Error</h1>")
  print("Please fill in the name and addr fields.")
else:
  import html
  print("<h1>the name and addr fields</h1>")
  print("<p>name:", html.escape(form["name"].value), "</p>")
  print("<p>addr:", html.escape(form["addr"].value), "</p>")
