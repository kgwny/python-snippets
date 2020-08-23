#!/usr/bin/env python
# -*- coding: utf-8 -*-

import cgi
import cgitb
import datetime
import locale
import json
import shelve
import urllib
from string import Template
cgitb.enable()

# 動作未確認

app='mini-bbs'
dbname='mini-bbs.db'

def keys():
  db=shlve.open(dbname)
  d=db.keys()
  db.close()
  return d

def msg_get(page):
  db=shelve.open(dbname)
  d=json.dumps(db[page]) if db.has_key(page) else '[]'
  db.close()
  return d

def msg_post(page,name,date,msg):
  db=shelve.open(dbname)
  if db.has_key(page):
    data=db[page]
    data.append({"name":name,"date":date,"msg":msg})
  else:
    data=[{"name":name,"date":date,"msg":msg}]
  db[page]=data
  db.close()

def msg_del(page,date):
  db=shelve.open(dbname)
  if db.has_key(page):
    data=db[page]
    for e in filter(lambda x:x['date']==date,data):
      data.remove(e)
    db[page]=data
  db.close()

def main():
  form=cgi.FieldStorage()
  q=form.getvalue('q','view')
  p=form.getvalue('p','notitle')
  if q=='post' and form.has_key('msg'):
    name=unicode(form.getvalue('name','anon'),'utf-8');
    date=datetime.datetime.today().strftime("%F %T")
    msg=unicode(form['msg'].value,'utf-8');
    msg_post(p,name,date,msg)
  elif q=='del' and form.has_key('date'):
    date=urllib.unquote(form['date'].value)
    msg_del(p,date)
  print t.substitute(app=app,msg=msg_get(p))

t=Template("""Content-Type: text/html
<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<style type="text/css"><!--
*{margin:0;padding:0;}
body{margin:5px;}
form{margin:10px 0;}
p{margin-top:1em;font-size:small;color:blue;}
pre{margin:5px 1em;font-size:normal;}
input,textarea{margin:2px;padding:1px 4px;}
--></style>
<title>${app}</title>
</head>
<body>
<h1>${app}</h1>
<form method="post" id="form">
<span>
<input type="submit" value="submit"/>
<label>name:<input type="text" name="name" size="20" /></label>
</span><br/>
<textarea cols="70" rows="5" name="msg" wrap="off"></textarea>
<input type="hidden" name="q" value="post"/>
<input type="hidden" name="date"/>
</form>
<div id="board"/>
<script>
(function (json){
  var board=document.getElementById('board');
  for(var i=json.length-1;i>=0;i--){
    var date=json[i]['date'];
    var p=document.createElement('p');
    var h=document.createTextNode(json[i]['name']+" - "+date+" ");
    p.appendChild(h);
    var del=document.createElement('input');
    del.type='button';
    del.value='del';
    del.addEventListener('click',(function(id){return function(){
      if(confirm("delete?")==false) return false;
      var f=document.getElementById('form');
      f.q.value='del';
      f.date.value=id;
      f.submit();
    }})(date),false);
    p.appendChild(del);
    board.appendChild(p);
    var pre=document.createElement('pre');
    var msg=document.createTextNode(json[i]['msg']);
    pre.appendChild(msg);
    board.appendChild(pre);
  }
})(${msg});
</script>
</body>
</html>""")

main()
