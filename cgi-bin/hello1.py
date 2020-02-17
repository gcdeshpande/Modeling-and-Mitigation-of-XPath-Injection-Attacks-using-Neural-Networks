#!/usr/bin/env python
import cgi
import xml.etree.ElementTree as ET
import libxml2
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

tree=ET.parse('/var/www/html/data.xml')
root=tree.getroot()
message=root.getchildren()
print "\n root element is", root.tag

print "\n child elements of ", root.tag, "are \n"
for m in message:
	print m.tag,m.text, "\n"

for n in root.iter("name"):
	print n.tag, n.attrib['first']

flag=0
print "usernames and passwords are"
for z in root.iter(usrname):
	uname= z.find("username").text
	pword= z.find("password").text
	print uname, pword
        if uname==usrname:
		flag=1
	else:
		flag=0
	
if flag==1:
	print "login success"
else:
	print "login failed"


y=root.findall(".")
for xy in y:
	print xy.find(".").text

#expr="//users/user/username/text()='mitch' and password/text()='@lltogether'"
doc=libxml2.parseFile('/var/www/html/data.xml')
#for url in doc.xpathEval("//users/user/username/text()='" +usrname+"'"):
for url in doc.xpathEval(usrname):
	print url.content



#form=cgi.FieldStorage()
#message=form.getvalue("txtName", "(no text)")

print """\

</h1>
</body>
</html>
""" % message

