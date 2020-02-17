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
    <table>
      <tr> <td>Login:</td><td><input type="text" name="txtName" /> </td> </tr>
      <tr> <td>Password:</td><td> <input type="password" name="txtPasswd" /> </td> </tr>
      <tr> <td align="right"><input type="submit" value="Login" /> </td> <td align="left"> <input type="reset"></tr>
    </table>  
    </form>
  '''

@route('/login', method='POST')
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
  
  
  open("/var/www/html/results.txt","w").close() 
  
 # results_string='Server time is: '+ time.asctime(time.localtime())
 # outFile.write(str(results_string))
    
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
 
  x=0
  inFile=open("/var/www/html/counter.txt","r")
  hits=inFile.readline()
  x=int(hits)+1
  inFile.close()
  
  outFile=open("/var/www/html/counter.txt","w")
  outFile.write(str(x))
  outFile.close()
  
  log_attempts=str(x)
  outFile=open("/var/www/html/results.txt","a")
  outFile.write(str("Login Attempt: "+log_attempts))
  #outFile.write(str(x))
  outFile.write(str('\n'))
  outFile.close()

  open("/var/www/html/traindata.txt","w").close() 
  
  if x<=3:
    attempts=x
    classval2=0
  else:  
    attempts=4
    classval2=1

  code=0  
  if (singleQuotes==1 and alphabets==(length-singleQuotes)) or (dots<=2 and alphabets==(length-dots)) or (alphabets==length) or (digits==length) or (dots<=2 and alphabets==(length-dots-atTheRate) and atTheRate==1):
    code=40
    classval=0
  elif singleQuotes>1 or doubleQuotes>0 or equalTo>0 or squareBrackets>0 or roundedBrackets>0 or curlyBrackets>0 or forwardSlash>0 or backwardSlash>0 or dots>=3 or whiteSpace>0 or pipes>0 or atTheRate>1:
    code=4000
    classval=2
  elif everyThingElse>0:
    code=400
    classval=1

  classes_stg1=['valid', 'invalid', 'malicious']
  trndata_stg1=ClassificationDataSet(2,class_labels=classes_stg1)
  trndata_stg1.appendLinked([40], [0])
  trndata_stg1.appendLinked([400], [1])
  trndata_stg1.appendLinked([4000], [2])
  trndata_stg1._convertToOneOfMany()
  tstdata_stg1=ClassificationDataSet(2,class_labels=classes_stg1)
  tstdata_stg1.appendLinked([code],[classval])
  rnn_stg1 = buildNetwork( trndata_stg1.indim, 50, trndata_stg1.outdim, hiddenclass=LSTMLayer, outclass=SoftmaxLayer, outputbias=False, recurrent=True)
  trainer_stg1 = RPropMinusTrainer( rnn_stg1, dataset=trndata_stg1, verbose=True )
  trainer_stg1.trainEpochs( 100 )
  trnresult_stg1=percentError(trainer_stg1.testOnClassData(), trndata_stg1['class'])
  tstresult_stg1=percentError(trainer_stg1.testOnClassData(dataset=tstdata_stg1), tstdata_stg1['class'])
  
 # outFile.write(str('\n'))
 # outFile.write(str('\n'))
  outFile=open("/var/www/html/results.txt","a")
  outFile.write(str('\n'))
  results_string='Result of Neural Network 1 (I/P: Error Code;  O/P: Class)'
  outFile.write(str(results_string))
  outFile.write(str('\n'))
  results_string='Number of training patterns: ', len(trndata_stg1)
  outFile.write(str(results_string))
  outFile.write(str('\n'))
  results_string='Input and output dimensions: ', trndata_stg1.indim, trndata_stg1.outdim
  outFile.write(str(results_string))
  outFile.write(str('\n'))
  results_string="train error: %5.2f%%" % trnresult_stg1, ",  test error: %5.2f%%" % tstresult_stg1
  outFile.write(str(results_string))
  outFile.write(str('\n'))
  outFile.close()
  
  classes_stg2=['valid', 'malicious']
  trndata_stg2=ClassificationDataSet(2,class_labels=classes_stg2)
  trndata_stg2.appendLinked([1], [0])
  trndata_stg2.appendLinked([2], [0])
  trndata_stg2.appendLinked([3], [0])
  trndata_stg2.appendLinked([4], [1])
  trndata_stg2._convertToOneOfMany()
  tstdata_stg2=ClassificationDataSet(2,class_labels=classes_stg2)
  tstdata_stg2.appendLinked([attempts],[classval2])
  rnn_stg2 = buildNetwork( trndata_stg2.indim, 50, trndata_stg2.outdim, hiddenclass=LSTMLayer, outclass=SoftmaxLayer, outputbias=False, recurrent=True)
  trainer_stg2 = RPropMinusTrainer( rnn_stg2, dataset=trndata_stg2, verbose=True )
  trainer_stg2.trainEpochs( 100 )
  trnresult_stg2=percentError(trainer_stg2.testOnClassData(), trndata_stg2['class'])
  tstresult_stg2=percentError(trainer_stg2.testOnClassData(dataset=tstdata_stg2), tstdata_stg2['class'])
  
  outFile=open("/var/www/html/results.txt","a")
  outFile.write(str('\n'))
  results_string='Result of Neural Network 2 (I/P: Login attempt;  O/P: Class)'
  outFile.write(str(results_string))
  outFile.write(str('\n'))
  results_string='Number of training patterns: ', len(trndata_stg2)
  outFile.write(str(results_string))
  outFile.write(str('\n'))
  results_string='Input and output dimensions: ', trndata_stg2.indim, trndata_stg2.outdim
  outFile.write(str(results_string))
  outFile.write(str('\n'))
  results_string="train error: %5.2f%%" % trnresult_stg2, ",  test error: %5.2f%%" % tstresult_stg2
  outFile.write(str(results_string))
  outFile.write(str('\n'))
  outFile.close()
  
  #if tstresult==0.0:
  #  if classes[classval]=='valid':
  #    rss=libxml2.parseDoc(urllib.urlopen('http://localhost/data.xml').read())
  #    for url in rss.xpathEval("//users/user[username/text()='"+usrname+"'and password/text()='"+passwd+"']"):
#	print url.name,url.content
#    elif classes[classval]=='malicious':
#      rss=libxml2.parseDoc(urllib.urlopen('http://localhost/fakedata.xml').read())
#      for url in rss.xpathEval("//users/user[username/text()='"+usrname+"'and password/text()='"+passwd+"']"):
#	print url.name,url.content
#    elif classes[classval]=='invalid':
#      print "Error"

  message=''
  #if (trnresult_stg1==0.0 and tstresult_stg1==0.0) and (trnresult_stg2==0.0 and tstresult_stg2==0.0):
  if tstresult_stg1==0.0 and tstresult_stg2==0.0:
    if classes_stg1[classval]=='valid' and classes_stg2[classval2]=='valid':
      message='valid'
    elif (classes_stg1[classval]=='valid' and classes_stg2[classval2]=='malicious') or (classes_stg1[classval]=='malicious' and classes_stg2[classval2]=='valid'):
      message='malicious'
    elif (classes_stg1[classval]=='invalid' and classes_stg2[classval2]=='valid') or (classes_stg1[classval]=='valid' or classes_stg2[classval2]=='invalid'):
      message='invalid'
    elif (classes_stg1[classval]=='invalid' and classes_stg2[classval2]=='malicious') or (classes_stg1[classval]=='malicious' and classes_stg2[classval2]=='invalid'):
      message='malicious'
    elif classes_stg1[classval]=='malicious' and classes_stg2[classval2]=='malicious':
      message='malicious'
 # else:
 #   redirect('http://localhost:8080/login')
    
  output=''
  fakeOutput=''
  #if message!='':
  if message=='valid':
#      return 'login successful'
    rss=libxml2.parseDoc(urllib.urlopen('/var/www/html/data.xml').read())
    for url in rss.xpathEval("//users/user[username/text()='"+usrname+"'and password/text()='"+passwd+"']"):
      output=output+url.name+url.content
    if output=='':
      rss=libxml2.parseDoc(urllib.urlopen('/var/www/html/fakedata.xml').read())
      for url in rss.xpathEval("//users/user[username/text()='"+usrname+"'and password/text()='"+passwd+"']"):
	fakeOutput=fakeOutput+url.name+url.content
      if fakeOutput=='':
	return 'login failed'
      else:
	return 'fake login successful'
    else:
      return 'login successful'
  elif message=='malicious':
    redirect('http://localhost/cgi-bin/myprojectfinal1.py?txtName='+usrname+'&txtPasswd='+passwd)
 #     rss=libxml2.parseDoc(urllib.urlopen('/var/www/html/fakedata.xml').read())
 #     for url in rss.xpathEval("//users/user[username/text()='"+usrname+"'and password/text()='"+passwd+"']"):
#	return output+url.name+url.content	
  elif message=='invalid':
    return 'Error'

  inFile=open("http://localhost/counter.txt","r")
  hits=inFile.readline()
  x=int(hits)+1
  inFile.close()
  outFile=open("http://localhost/counter.txt","w")
  outFile.write(str(x))
  outFile.close()


  cookie_string = os.environ.get('HTTP_COOKIE')
  #if not cookie_string:
  if request.get_cookie("visited"):
    #x=0
    #outFile=open("/var/www/html/counter.txt","w")
    #outFile.write(str(x))
    #outFile.close()
    inFile=open("/var/www/html/counter.txt","r")
    hits=inFile.readline()
    x=int(hits)+1
    inFile.close()
    outFile=open("/var/www/html/counter.txt","w")
    outFile.write(str(x))
    outFile.close()
  else: # Run the page twice to retrieve the cookie
    #cookie.load(cookie_string)
    #lastvisit = float(cookie['lastvisit'].value)
    response.set_cookie("visited", "yes")
    x=0
    outFile=open("/var/www/html/counter.txt","w")
    outFile.write(str(x))
    outFile.close()
 #   
 #   inFile=open("/var/www/html/counter.txt","r")
 #   hits=inFile.readline()
 #   x=int(hits)+1
 #   inFile.close()
 #   outFile=open("/var/www/html/counter.txt","w")
 #   outFile.write(str(x))
 #   outFile.close()
       
run(host='localhost', port=8080, debug=True)
