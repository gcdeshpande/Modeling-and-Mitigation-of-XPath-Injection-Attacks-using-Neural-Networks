from bottle import route, run, request, redirect
import Cookie, os, time
import cgi
import xml.etree.ElementTree as ET
import libxml2
import urllib
import re
from pybrain.datasets            import ClassificationDataSet
from pybrain.structure.modules   import LSTMLayer, SoftmaxLayer
from pybrain.supervised          import RPropMinusTrainer
from pybrain.tools.validation    import testOnSequenceData
from pybrain.tools.shortcuts     import buildNetwork
from pybrain.utilities           import percentError
from pybrain.supervised.trainers import BackpropTrainer

@route('/')  
@route('/loginform')
def loginform():
  return '''
    <form action="/login" method="post">
      Login:<input type="text" name="txtName" /> <br />
      Password: <input type="password" name="txtPasswd" /> <br />
      <input type="submit" value="Login" />
      <input type="reset" value="Clear" />
    </form>
  '''

@route('/login', method='post')
def login():
  cookie = Cookie.SimpleCookie()
  cookie['lastvisit'] = str(time.time())
#  print 'Content-Type: text/html\n'
#  print '<html><body>'
 # form=cgi.FieldStorage()
  #usrname=form.getvalue("txtName", "(no text)")
  #passwd=form.getvalue("txtPasswd", "(no passwd)")

  usrname=request.forms.get('txtName')
  passwd=request.forms.get('txtPasswd')
  
  length=0
  #return usrname
  for l in usrname:
    length=length+1

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
  atTheRate=0

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
    elif usrname[i]=='@':
      atTheRate=atTheRate+1
    else:
      everyThingElse=everyThingElse+1

  
  cookie_string = os.environ.get('HTTP_COOKIE')
  if not cookie_string:
    x=0
    outFile=open("/var/www/html/counter.txt","w")
    outFile.write(str(x))
    outFile.close()
  else: # Run the page twice to retrieve the cookie
    cookie.load(cookie_string)
    lastvisit = float(cookie['lastvisit'].value)
    inFile=open("/var/www/html/counter.txt","r")
    hits=inFile.readline()
    x=int(hits)+1
    inFile.close()
    outFile=open("/var/www/html/counter.txt","w")
    outFile.write(str(x))
    outFile.close()
  
  code=0 
  attempts=0
  classval=0
  if ((singleQuotes==1 and alphabets==(length-singleQuotes)) or (dots<=2 and alphabets==(length-dots)) or (alphabets==length) or (digits==length) or (dots<=2 and alphabets==(length-dots-atTheRate) and atTheRate==1)) and (x<4):
    code=40
    classval=0
    attempts=x
  elif (singleQuotes>1 or doubleQuotes>0 or equalTo>0 or squareBrackets>0 or roundedBrackets>0 or curlyBrackets>0 or forwardSlash>0 or backwardSlash>0 or dots>=3 or whiteSpace>0 or pipes>0 or atTheRate>1) and (x>3):
    code=4000
    classval=2
    attempts=4
  elif everyThingElse>0 and x<3:
    code=400
    classval=1
    attempts=x
  elif everyThingElse>0 and x>3:
    code=400
    classval=2
    attempts=4

  classes=['valid', 'invalid', 'malicious']
  trndata=ClassificationDataSet(2,class_labels=classes)
  trndata.appendLinked([40,1], [0])
  trndata.appendLinked([40,2], [0])
  trndata.appendLinked([40,3], [0])
  trndata.appendLinked([40,4], [2])
  trndata.appendLinked([400,1], [1])
  trndata.appendLinked([400,2], [1])
  trndata.appendLinked([400,3], [1])
  trndata.appendLinked([400,4], [2])
  trndata.appendLinked([4000,1], [2])
  trndata.appendLinked([4000,2], [2])
  trndata.appendLinked([4000,3], [2])
  trndata.appendLinked([4000,4], [2])
  trndata._convertToOneOfMany()
  tstdata=ClassificationDataSet(2,class_labels=classes)
  tstdata.appendLinked([code,attempts],[classval])
  rnn = buildNetwork( trndata.indim, 50, trndata.outdim, hiddenclass=LSTMLayer, outclass=SoftmaxLayer, outputbias=False, recurrent=True)
  trainer = RPropMinusTrainer( rnn, dataset=trndata, verbose=True )
  trainer.trainEpochs( 100 )
  trnresult=percentError(trainer.testOnClassData(), trndata['class'])
  tstresult=percentError(trainer.testOnClassData(dataset=tstdata), tstdata['class'])
  if tstresult==0.0:
    if classes[classval]=='valid':
      rss=libxml2.parseDoc(urllib.urlopen('http://localhost/data.xml').read())
      for url in rss.xpathEval("//users/user[username/text()='"+usrname+"'and password/text()='"+passwd+"']"):
	print url.name,url.content
    elif classes[classval]=='malicious':
      rss=libxml2.parseDoc(urllib.urlopen('http://localhost/fakedata.xml').read())
      for url in rss.xpathEval("//users/user[username/text()='"+usrname+"'and password/text()='"+passwd+"']"):
	print url.name,url.content
    elif classes[classval]=='invalid':
      print "Error"

  outFile=open("/var/www/html/output.txt","w")
  
  output=''
  fakeOutput=''
  if tstresult==0.0:
    if classes[classval]=='valid':
#      return 'login successful'
      rss=libxml2.parseDoc(urllib.urlopen('/var/www/html/data.xml').read())
      for url in rss.xpathEval("//users/user[username/text()='"+usrname+"'and password/text()='"+passwd+"']"):
	output=output+url.name+url.content
	outFile.write(str(output))
      if output=='':
	rss=libxml2.parseDoc(urllib.urlopen('/var/www/html/fakedata.xml').read())
	for url in rss.xpathEval("//users/user[username/text()='"+usrname+"'and password/text()='"+passwd+"']"):
	  fakeOutput=fakeOutput+url.name+url.content
	  outFile.write(str(fakeOutput))
	if fakeOutput=='':
	  return 'login failed'
	else:
	  return 'fake login successful'
      else:
	return 'login successful'
    elif classes[classval]=='malicious':
      redirect('http://localhost/cgi-bin/myproject.py?txtName='+usrname+'&txtPasswd='+passwd)
 #     rss=libxml2.parseDoc(urllib.urlopen('/var/www/html/fakedata.xml').read())
 #     for url in rss.xpathEval("//users/user[username/text()='"+usrname+"'and password/text()='"+passwd+"']"):
#	return output+url.name+url.content	
    elif classes[classval]=='invalid':
      return 'Error'
  
  outFile.close()
  

run(host='localhost', port=8080, debug=True)
