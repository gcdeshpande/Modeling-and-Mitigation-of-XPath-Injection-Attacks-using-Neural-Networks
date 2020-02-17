#!/usr/bin/env python
import Cookie, os, time


cookie = Cookie.SimpleCookie()
cookie['lastvisit'] = str(time.time())


print cookie
print 'Content-Type: text/html\n'

print '<html><body>'
print '<p>Server time is', time.asctime(time.localtime()), '</p>'

# The returned cookie is available in the os.environ dictionary
cookie_string = os.environ.get('HTTP_COOKIE')

# The first time the page is run there will be no cookies
if not cookie_string:
   print '<p>First visit or cookies disabled</p>'
   x=0
   outFile=open("/var/www/html/counter.txt","w")
   outFile.write(str(x))
   outFile.close()
   print 'hits: 1'

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
   print 'hits:',x

print '</body></html>'
