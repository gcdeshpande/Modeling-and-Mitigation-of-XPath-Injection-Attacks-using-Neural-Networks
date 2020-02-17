#!/usr/bin/env python
import cgi
import xml.etree.ElementTree as ET
import libxml2
import urllib
import re

print "Content-type: text/html\n";
print

print """\
<html>
<head>
<title> Python - Hello World </title>
</head>
<body>
<h1>
"""

form=cgi.FieldStorage()
usrname=form.getvalue("txtName", "(no text)")
passwd=form.getvalue("txtPasswd", "(no passwd)")
#usrname="user' or '1'='1"
#passwd="password"


#if re.search('[a-zA-Z0-9+_\-\.]+@[0-9a-zA-Z][.-0-9a-zA-Z]*.[a-zA-Z]+', usrname):
#  print 'success'
#else:
#  print 'fail'
  
#if re.match('[a-zA-Z0-9]+', usrname) and re.match('[^\'\=]+',usrname):
#  print 'success'
#else:
#  print 'fail'
  
#if re.match('[^\'0-9]+', usrname):
#  print 'success'
#else:
#  print 'fail'

count=0
#for i in usrname:
#  if i=='\'':
#    count=0  ///use flag
#  elif i=='\=':
#    count=count+1

length=0
for l in usrname:
  length=length+1

print length

singleQuotes=0
doubleQuotes=0
everyThingElse=0
equalTo=0
squareBrackets=0
roundedBrackets=0
curlyBrackets=0
forwardSlash=0
backwardSlash=0
asterisk=0
pipes=0
whiteSpace=0
alphabets=0
digits=0
dots=0

for i in range(length):
  if usrname[i]=='\'':
    singleQuotes=singleQuotes+1
  elif usrname[i]=='\"':
    doubleQuotes=doubleQuotes+1
  elif usrname[i]=='=':
    equalTo=equalTo+1
  elif usrname[i]=='[' or usrname[i]==']':
    squareBrackets=squareBrackets+1    
  elif usrname[i]=='(' or usrname[i]==')':
    roundedBrackets=roundedBrackets+1
  elif usrname[i]=='{' or usrname[i]=='}':
    curlyBrackets=curlyBrackets+1
  elif usrname[i]=='/':
    forwardSlash=forwardSlash+1
  elif usrname[i]=='\\':
    backwardSlash=backwardSlash+1
  elif usrname[i]=='*':
    asterisk=asterisk+1
  elif usrname[i]=='|':
    pipes=pipes+1
  elif usrname[i]==' ':
    whiteSpace=whiteSpace+1
  elif re.search('[a-zA-Z]',usrname[i]):
    alphabets=alphabets+1
  elif re.search('[0-9]',usrname[i]):
    digits=digits+1
  elif usrname[i]=='.':
    dots=dots+1
  else:
    everyThingElse=everyThingElse+1

print '<br> Single Quotes',singleQuotes
print '<br> Double Quotes', doubleQuotes
print '<br> equalTo', equalTo
print '<br> Square Brackets',squareBrackets
print '<br> Rounded Brackets',roundedBrackets
print '<br> curlyBrackets', curlyBrackets
print '<br> Asterisks', asterisk
print '<br> forward Slashes', forwardSlash
print '<br> backward Slashes', backwardSlash
print '<br> pipes', pipes
print '<br> White Spaces', whiteSpace
print '<br> Alphabets', alphabets
print '<br> Digits', digits
print '<br> dots', dots
print '<br> Every Thing Else', everyThingElse


##Error Code
## 100  - Success - valid
## 101 - 
code=0  
print count

if (singleQuotes==1 and alphabets==(length-singleQuotes)) or (dots<=2 and alphabets==(length-dots)) or (alphabets==length) or (digits==length):
  print 'valid'
  code=100
elif singleQuotes>1 or doubleQuotes>0 or equalTo>0 or squareBrackets>0 or roundedBrackets>0 or curlyBrackets>0 or forwardSlash>0 or backwardSlash>0 or dots==1 or whiteSpace>0 or pipes>0:
  print 'Malicious'
  code=101
elif everyThingElse>0:
  print 'Invalid'
  code=102
  
  
  
  
  
#  print 'invalid'
#else:
#  print 'valid'
      
count=0
rss=libxml2.parseDoc(urllib.urlopen('http://localhost/data.xml').read())
for url in rss.xpathEval("//users/user[username/text()='"+usrname+"'and password/text()='"+passwd+"']"):
  print url.name,url.content

#pnodes=rss.xpathEval('//users/user/password/text()')

#unodes=rss.xpathEval(usrname)
#pnodes=rss.xpathEval(passwd)

#for i in unodes:
#  count=count+1
#print 'no of users',count

#flag=0
#for i in range(0,count):
#  if eval(usrname)==eval(unodes[i]) and eval(passwd)==eval(pnodes[i]):
#    flag=1
#    break
    
#if flag==1:
#  print 'login success <br>'
#else:
#  print 'login failed <br>'



#tree=ET.parse('/var/www/html/data.xml')
#root=tree.getroot()
#message=root.getchildren()
#print "\n root element is", root.tag

#print "\n child elements of ", root.tag, "are \n"
#for m in message:
#	print m.tag,m.text, "\n"

#for n in root.iter("name"):
#	print n.tag, n.attrib['first']

#flag=0
#print "usernames and passwords are"
#for z in root.iter(usrname):
#	uname= z.find("username").text
#	pword= z.find("password").text
#	print uname, pword
 #       if uname==usrname:
#		flag=1
#	else:
#		flag=0
	
#if flag==1:
#	print "login success"
#else:
#	print "login failed"
#

#y=root.findall(".")
#for xy in y:
#	print xy.find(".").text

#expr="//users/user/username/text()='mitch' and password/text()='@lltogether'"
#doc=libxml2.parseFile('/var/www/html/data.xml')
#for url in doc.xpathEval("//users/user/username/text()='" +usrname+"'"):
#for url in doc.xpathEval(usrname):
#	print url.content



#form=cgi.FieldStorage()
#message=form.getvalue("txtName", "(no text)")

print """\

</h1>
</body>
</html>
""" #% message

