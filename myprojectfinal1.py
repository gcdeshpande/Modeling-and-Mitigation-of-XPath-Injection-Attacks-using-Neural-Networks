#!/usr/bin/env python
import Cookie, os, time
import cgi
import xml.etree.ElementTree as ET
import libxml2
import urllib
import re

print 'Content-Type: text/html\n'

print '<html><body>'
outFile=open("/var/www/html/log.txt","a")
outFile.write(str("Remote Port: "+os.environ['REMOTE_PORT']))
outFile.write(str('\n'))
outFile.close()

outFile=open("/var/www/html/log.txt","a")
outFile.write(str("Remote Address: "+os.environ['REMOTE_ADDR']))
outFile.write(str('\n'))
outFile.close()

outFile=open("/var/www/html/log.txt","a")
outFile.write(str("Request Method "+os.environ['REQUEST_METHOD']))
outFile.write(str('\n'))
outFile.close()

outFile=open("/var/www/html/log.txt","a")
outFile.write(str("Web Browser: "+os.environ['HTTP_USER_AGENT']))
outFile.write(str('\n'))
outFile.close()

outFile=open("/var/www/html/log.txt","a")
outFile.write(str("Query String: "+os.environ['QUERY_STRING']))
outFile.write(str('\n'))
outFile.close()

outFile=open("/var/www/html/log.txt","a")
outFile.write(str("Server Time: "+time.asctime(time.localtime())))
outFile.write(str('\n'))
outFile.write(str('\n'))
outFile.write(str('\n'))
outFile.close()

##comment
form=cgi.FieldStorage()
usrname=form.getvalue("txtName", "(no text)")
passwd=form.getvalue("txtPasswd", "(no passwd)")

rss=libxml2.parseDoc(urllib.urlopen('http://localhost/fakedata.xml').read())
for url in rss.xpathEval("//users/user[username/text()='"+usrname+"'and password/text()='"+passwd+"']"):
  print url.name,url.content  

print '</body></html>'

