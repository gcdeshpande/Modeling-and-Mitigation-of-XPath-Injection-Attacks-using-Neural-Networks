#!/usr/bin/env python

import cgi
form = cgi.FieldStorage()

name = form.getvalue('name', 'world')

print """Content-type: text/html

<html>
  <head>
    <title>Greeting Page</title>
  </head>
  <body>
    <h1>Hello, %s!</h1>

    <form action='form.py'>
    Change name <input type='text' name='name' />
    <input type='submit' />
    </form>
  </body>
</html>
""" % name
