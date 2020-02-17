#!/usr/bin/env python
import cgi

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
message=form.getvalue("txtName", "(no text)")

print """\

hello %s
</h1>
</body>
</html>
""" % message

