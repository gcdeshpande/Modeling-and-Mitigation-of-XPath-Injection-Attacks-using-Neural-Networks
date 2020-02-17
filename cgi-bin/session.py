#!/usr/bin/env python
import os,cgi,cgitb,Cookie; cgitb.enable()
import datetime
sc=Cookie.SimpleCookie(os.environ.get('HTTP_COOKIE',''))
expires=datetime.datetime.now()+datetime.timedelta(minutes=1)
c_name=sc.get('name').value if sc.has_key('name') else 'nocookie'
f_name=cgi.FieldStorage().getfirst('form','noform')
sc['name']=f_name
sc['name']["expires"]=expires.strftime("%a, %d-%b-%Y %H:%M:%S GMT")
print "Content-Type: text/html"
print sc.output()
count=count+1
 
print count
print """
<html><body><ul>
<li>get COOKIE value: {0}</li>
<li>posted FORM: {1}</li>
<li>set COOKIE: {2}</li>
</ul>
<form method="post">
<input type='text' name='form' value='{3}'/>
<input type='submit' value='submit' />
</form></body></html>""".format(c_name,f_name,sc.output(),f_name)