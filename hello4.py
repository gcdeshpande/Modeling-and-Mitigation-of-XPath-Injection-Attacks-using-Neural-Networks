from bottle import route, run
import libxml2
import urllib
from bottle import redirect
@route('/')
@route('/hello1')
def hello1():
  usrname='3]|/*|/a[1'
  passwd='3]|/*|/a[1'
  output=''
  rss=libxml2.parseDoc(urllib.urlopen('http://localhost/data.xml').read())
  for url in rss.xpathEval("//users/user[username/text()='"+usrname+"'and password/text()='"+passwd+"']"):
    output=output+url.name+url.content
  return output
  
  
@route('/hello')
def wrong():
  redirect("http://localhost/myproject.py")


run(host='localhost', port=8080, debug=True)
