#!/usr/bin/env python
import Cookie, os, time
import cgi
import xml.etree.ElementTree as ET
import libxml2

cookie = Cookie.SimpleCookie()
cookie['lastvisit'] = str(time.time())

print cookie
print 'Content-Type: text/html\n'

print '<html><body>'
print '<p>Server time is', time.asctime(time.localtime()), '</p>'

##comment


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
		break
#	else:
#		flag=1
	
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



##comment

# The returned cookie is available in the os.environ dictionary
cookie_string = os.environ.get('HTTP_COOKIE')

# The first time the page is run there will be no cookies
if not cookie_string:
   print '<p>First visit or cookies disabled</p>'
   x=0
   outFile=open("/var/www/html/counter.txt","w")
   outFile.write(str(x))
   outFile.close()
   print 'Login Attempt: 1'

else: # Run the page twice to retrieve the cookie
   print '<p>The returned cookie string was "' + cookie_string + '"</p>'
   # load() parses the cookie string
   cookie.load(cookie_string)
   # Use the value attribute of the cookie to get it
   lastvisit = float(cookie['lastvisit'].value)
   
   print '<p>Your last visit was at',
   print time.asctime(time.localtime(lastvisit)), '</p>'
   print lastvisit
   print time.time()
   print 'the last visit was before', time.time()-lastvisit
   inFile=open("/var/www/html/counter.txt","r")
   hits=inFile.readline()
   x=int(hits)+1
   inFile.close()
   outFile=open("/var/www/html/counter.txt","w")
   outFile.write(str(x))
   outFile.close()
   print 'Login Attempt:',x
print '</body></html>'
