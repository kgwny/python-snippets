#!/usr/bin/env python
# -*- coding: utf-8 -*-
 
import cgi
import cgitb
cgitb.enable()
 
print("Content-Type: text/html; charset=utf-8")    # HTML is following
print("")                           # blank line, end of headers
 
form = cgi.FieldStorage()
if "imagefile" in form:
  fileitem = form["imagefile"]
  if fileitem.file:
      # It's an uploaded file; count lines
      from PIL import Image
 
      image = Image.open(fileitem.file)
 
      image.save("org.png")
      image.convert("1").save("1_1-bit-pixels.png")
      image.convert("L").save("L_8-bit-grayscale.png")
      image.convert("P").save("P_8-bit-colors.png")
 
      print("<h1>オリジナル</h1>")
      print("<img src=\"../org.png\" width=\"350\">")
      print("<h1>画像モード変換後</h1>")
      print("<table>")
      print("  <tr><td>1_1-bit-pixels.png<br />")
      print("          <img src=\"../1_1-bit-pixels.png\" width=\"350\"></td>")
      print("      <td>L_8-bit-grayscale.png<br />")
      print("          <img src=\"../L_8-bit-grayscale.png\" width=\"350\"></td>")
      print("      <td>P_8-bit-colors.png<br />")
      print("          <img src=\"../P_8-bit-colors.png\" width=\"350\"></td></tr>")
