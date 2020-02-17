#!/usr/bin/env python2.7
import cgi
import lxml
from lxml import etree

print "Content-type: text/html\n"
print 

print """\
<html>
<head>
<title> Python - XML Parser </title>
</head>
<body>
"""

infile="/var/www/html/imlog.xml"
xmldata=etree.parse(infile)
messages=xmldata.findall("//message")
for msg in messages:
	msgdate=msg.attrib['date']
	msgtime=msg.attrib['time']
	msgfrom=msg.find("from/user").attrib['friendlyname']
	msgto=msg.find("to/user").attrib['friendlyname']
	msgtext=msg.findtext("text")
print """\
	print '%s, %s: %s to %s: %s\n'
</body>
</html>
""" % msgdate,msgtime,msgfrom,msgto,msgtext
