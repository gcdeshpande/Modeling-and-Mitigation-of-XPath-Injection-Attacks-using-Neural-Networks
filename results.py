#!/usr/bin/env python
import Cookie, os, time
import cgi
import xml.etree.ElementTree as ET
import libxml2
import urllib
import re
#from pylab import plot, hold, show
#from scipy import sin, rand, arange
#from pybrain.datasets            import SequenceClassificationDataSet
from pybrain.datasets            import ClassificationDataSet
from pybrain.structure.modules   import LSTMLayer, SoftmaxLayer
from pybrain.supervised          import RPropMinusTrainer
from pybrain.tools.validation    import testOnSequenceData
from pybrain.tools.shortcuts     import buildNetwork
from pybrain.utilities           import percentError
from pybrain.supervised.trainers import BackpropTrainer


cookie = Cookie.SimpleCookie()
cookie['lastvisit'] = str(time.time())

print cookie
print 'Content-Type: text/html\n'

print '<html><body>'
#print '<p>Server time is', time.asctime(time.localtime()), '</p>'
#print 'remote address', os.environ['REMOTE_ADDR']
#print os.environ['REMOTE_PORT']
#outFile=open("/var/www/html/log.txt","a")
#outFile.write(str("Remote Port: "+os.environ['REMOTE_PORT']))
#outFile.write(str('\n'))
#outFile.close()

#outFile=open("/var/www/html/log.txt","a")
#outFile.write(str("Remote Address: "+os.environ['REMOTE_ADDR']))
#outFile.write(str('\n'))
#outFile.close()

#outFile=open("/var/www/html/log.txt","a")
#outFile.write(str("Request Method "+os.environ['REQUEST_METHOD']))
#outFile.write(str('\n'))
#outFile.close()

#outFile=open("/var/www/html/log.txt","a")
#outFile.write(str("Web Browser: "+os.environ['HTTP_USER_AGENT']))
#outFile.write(str('\n'))
#outFile.close()

#outFile=open("/var/www/html/log.txt","a")
#outFile.write(str("Query String: "+os.environ['QUERY_STRING']))
#outFile.write(str('\n'))
#outFile.close()

#outFile=open("/var/www/html/log.txt","a")
#outFile.write(str("Server Time: "+time.asctime(time.localtime())))
#outFile.write(str('\n'))
#outFile.write(str('\n'))
#outFile.write(str('\n'))
#outFile.close()






##comment
#form=cgi.FieldStorage()
#usrname=form.getvalue("txtName", "(no text)")
#passwd=form.getvalue("txtPasswd", "(no passwd)")

#length=0
#for l in usrname:
#  length=length+1

#print length

#singleQuotes=0
#doubleQuotes=0
#everyThingElse=0
#equalTo=0
#squareBrackets=0
#roundedBrackets=0
#curlyBrackets=0
#forwardSlash=0
#backwardSlash=0
#asterisk=0
#pipes=0
#whiteSpace=0
#alphabets=0
#digits=0
#dots=0
#atTheRate=0

#for i in range(length):
#  if usrname[i]=='\'':
#    singleQuotes=singleQuotes+1
#  elif usrname[i]=='\"':
#    doubleQuotes=doubleQuotes+1
#  elif usrname[i]=='=':
#    equalTo=equalTo+1
#  elif usrname[i]=='[' or usrname[i]==']':
#    squareBrackets=squareBrackets+1    
#  elif usrname[i]=='(' or usrname[i]==')':
#    roundedBrackets=roundedBrackets+1
#  elif usrname[i]=='{' or usrname[i]=='}':
#    curlyBrackets=curlyBrackets+1
#  elif usrname[i]=='/':
#    forwardSlash=forwardSlash+1
#  elif usrname[i]=='\\':
#    backwardSlash=backwardSlash+1
#  elif usrname[i]=='*':
#    asterisk=asterisk+1
#  elif usrname[i]=='|':
#    pipes=pipes+1
#  elif usrname[i]==' ':
#    whiteSpace=whiteSpace+1
#  elif re.search('[a-zA-Z]',usrname[i]):
#    alphabets=alphabets+1
#  elif re.search('[0-9]',usrname[i]):
#    digits=digits+1
#  elif usrname[i]=='.':
#    dots=dots+1
#  elif usrname[i]=='@':
#    atTheRate=atTheRate+1
#  else:
#    everyThingElse=everyThingElse+1

#print '<br> Single Quotes',singleQuotes
#print '<br> Double Quotes', doubleQuotes
#print '<br> equalTo', equalTo
#print '<br> Square Brackets',squareBrackets
#print '<br> Rounded Brackets',roundedBrackets
#print '<br> curlyBrackets', curlyBrackets
#print '<br> Asterisks', asterisk
#print '<br> forward Slashes', forwardSlash
#print '<br> backward Slashes', backwardSlash
#print '<br> pipes', pipes
#print '<br> White Spaces', whiteSpace
#print '<br> Alphabets', alphabets
#print '<br> Digits', digits
#print '<br> dots', dots
#print '<br> @ Symbols', atTheRate
#print '<br> Every Thing Else', everyThingElse


##Error Code
## 100  - Success - valid
## 101 - 

#print count
#x=0

#inFile=open("/var/www/html/counter.txt","r")
#hits=inFile.readline()
#x=int(hits)+1
#inFile.close()

#code=0 
#attempts=0
#classval=0
#if ((singleQuotes==1 and alphabets==(length-singleQuotes)) or (dots<=2 and alphabets==(length-dots)) or (alphabets==length) or (digits==length) or (dots<=2 and alphabets==(length-dots-atTheRate) and atTheRate==1)):
#  code=40
#  classval=0
#elif (singleQuotes>1 or doubleQuotes>0 or equalTo>0 or squareBrackets>0 or roundedBrackets>0 or curlyBrackets>0 or forwardSlash>0 or backwardSlash>0 or dots>=3 or whiteSpace>0 or pipes>0 or atTheRate>1):
#  code=4000
#  classval=2
#elif everyThingElse>0:
#  code=400
#  classval=1


#if x<=3:
#  attempts=x
#  classval2=0
#else:  
#  attempts=4
#  classval2=1
##comment

##RNN Code start here

#testcode=[4000,4000,4000,4000,4000,4000,4000,4000,4000,4000,4000,4000,4000,4000,4000,4000,4000,4000,4000,4000,4000,4000,4000,4000,4000,4000,4000,4000,4000,4000,4000,4000,4000,4000,4000,4000,4000,4000,4000,4000,4000,4000,4000,4000,4000,4000,4000,4000,4000,4000,4000,4000,4000,4000,4000,4000,4000,4000,4000,4000,4000,4000,4000,4000,4000,4000,4000,4000,4000,4000,4000,4000,4000,4000,4000,4000,4000,4000,4000,4000,4000,4000,4000,4000,4000,4000,4000,4000,4000,4000,4000,4000,4000,4000,4000,4000,4000,4000,4000,4000]
#testclassval=[2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2]
#testattempts=[4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4]
#testclassval2=[1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]

testcode=[40,40,40,40,40,40,40,40,40,40,40,40,40,40,40,40,40,40,40,40,40,40,40,40,40,40,40,40,40,40,40,40,40,40,40,40,40,40,40,40,40,40,40,40,40,40,40,40,40,40,40,40,40,40,40,40,40,40,40,40,40,40,40,40,40,40,40,40,40,40,40,40,40,40,40,40,40,40,40,40,40,40,40,40,40,40,40,40,40,40,40,40,40,40,40,40,40,40,40,40]
testclassval=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
testattempts=[1,2,3,1,2,3,1,2,3,1,2,3,1,2,3,1,2,3,1,2,3,1,2,3,1,2,3,1,2,3,1,2,3,1,2,3,1,2,3,1,2,3,1,2,3,1,2,3,1,2,3,1,2,3,1,2,3,1,2,3,1,2,3,1,2,3,1,2,3,1,2,3,1,2,3,1,2,3,1,2,3,1,2,3,1,2,3,1,2,3,1,2,3,1,2,3,1,2,3,1]
testclassval2=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]

valid=0
invalid=0
malicious=0
start=time.time()
for i in range(100):
  print "=============================="
  print "ITERATION: ",i
  print "=============================="
  print testcode[i],testclassval[i],testattempts[i],testclassval2[i]
  code=testcode[i]
  classval=testclassval[i]
  attempts=testattempts[i]
  classval2=testclassval2[i]
 
  classes1=['valid', 'invalid', 'malicious']
  trndata1=ClassificationDataSet(2,class_labels=classes1)
  trndata1.appendLinked([40], [0])
  trndata1.appendLinked([400], [1])
  trndata1.appendLinked([4000], [2])
  trndata1._convertToOneOfMany()

  tstdata1=ClassificationDataSet(2,class_labels=classes1)
  tstdata1.appendLinked([code],[classval])
  
  classes2=['valid', 'malicious']
  trndata2=ClassificationDataSet(2,class_labels=classes2)
  trndata2.appendLinked([1], [0])
  trndata2.appendLinked([2], [0])
  trndata2.appendLinked([3], [0])
  trndata2.appendLinked([4], [1])
  trndata2._convertToOneOfMany()

  tstdata2=ClassificationDataSet(2,class_labels=classes2)
  tstdata2.appendLinked([attempts],[classval2])
  
#tstdata.appendLinked([40],[1])
#tstdata.appendLinked([500],[1])
#tstdata.appendLinked([501], [2])
#tstdata.appendLinked([5000], [2])

#tstdata.appendLinked([0,0], [0])
#tstdata.appendLinked([0,1], [0])
#tstdata.appendLinked([1,0], [0])
#tstdata.appendLinked([1,1], [0])
#tstdata.appendLinked([0,0], [1])
#tstdata.appendLinked([0,1], [1])
#tstdata.appendLinked([1,0], [1])
#tstdata.appendLinked([1,1], [1])
#tstdata.appendLinked([0,0], [2])
#tstdata.appendLinked([0,1], [2])
#tstdata.appendLinked([1,0], [2])
#tstdata.appendLinked([1,1], [2])
#tstdata._convertToOneOfMany()


# construct LSTM network - note the missing output bias
  rnn1 = buildNetwork( trndata1.indim, 50, trndata1.outdim, hiddenclass=LSTMLayer, outclass=SoftmaxLayer, outputbias=False, recurrent=True)
  rnn2 = buildNetwork( trndata2.indim, 50, trndata2.outdim, hiddenclass=LSTMLayer, outclass=SoftmaxLayer, outputbias=False, recurrent=True)
#rnn.reset()


#print tstdata
# define a training method
  trainer1 = RPropMinusTrainer( rnn1, dataset=trndata1, verbose=True )
  trainer2 = RPropMinusTrainer( rnn2, dataset=trndata2, verbose=True )
# instead, you may also try
#trainer = BackpropTrainer( rnn, dataset=trndata, verbose=True, momentum=0.9, learningrate=0.00001 )
#rnn.sortModules()
#tstdata=rnn.activate((5000))
# carry out the training

##for i in xrange(10):
#outFile=open("/var/www/html/output.txt","w")
#trainer.trainEpochs(1)
#outFile.close()
#print "<font color='white'>"  
  trainer1.trainEpochs(100)
       
    #trnresult = 100. * (1.0-testOnSequenceData(rnn, trndata))
    #tstresult = 100. * (1.0-testOnSequenceData(rnn, tstdata))
  trnresult1=percentError(trainer1.testOnClassData(), trndata1['class'])
  tstresult1=percentError(trainer1.testOnClassData(dataset=tstdata1), tstdata1['class'])
   # trnresult = testOnSequenceData(rnn, trndata)*100
   # tstresult = testOnSequenceData(rnn, tstdata)*100
 
  print "<br>train error: %5.2f%%" % trnresult1, ",  test error: %5.2f%%" % tstresult1
#print "</font>"
# just for reference, plot the first 5 timeseries
#plot(trndata['input'][0:250,:],'-o')
#hold(True)
#plot(trndata['target'][0:250,0])



  trainer2.trainEpochs(100)
       
    #trnresult = 100. * (1.0-testOnSequenceData(rnn, trndata))
    #tstresult = 100. * (1.0-testOnSequenceData(rnn, tstdata))
  trnresult2=percentError(trainer2.testOnClassData(), trndata2['class'])
  tstresult2=percentError(trainer2.testOnClassData(dataset=tstdata2), tstdata2['class'])
   # trnresult = testOnSequenceData(rnn, trndata)*100
   # tstresult = testOnSequenceData(rnn, tstdata)*100
 
  print "<br>train error: %5.2f%%" % trnresult2, ",  test error: %5.2f%%" % tstresult2
#  print "<br>Number of training patterns: ", len(trndata1)
#  print "<br>Input and output dimensions: ", trndata1.indim, trndata1.outdim
#  print "<br>First sample (input, target, class):"
#  print trndata1['input'][0], trndata1['target'][0], trndata1['class'][0]
  #print "x: ",x
  #print "attempts: ",attempts
  #print "stage1 ", classes1[classval]
  #print "stage2 ", classes2[classval2]
#log_string='<br>'+time.asctime(time.localtime())
#log_string=log_string+os.environ['REMOTE_ADDR']
#log_string=log_string+os.environ['REMOTE_HOST']
#log_string=log_string+os.environ['REMOTE_PORT']
#log_string=log_string+os.environ['REMOTE_USER']
#print log_string
#log_string=log_string+'\t'+os.environ['HTTP_USER_AGENT']
#log_string=log_string+'\t'+os.environ['REQUEST_METHOD']
#log_string=log_string+'\t'+os.environ['QUERY_STRING']+'\n'


#print "Number of training patterns: ", len(tstdata)
#print "output dimensions: ", tstdata.outdim
#print "First sample (input, target, class):"
#print tstdata[0], tstdata[1], tstdata[2]
#print 'class', classes[tstdata['class'][0]]
#class_index = max(xrange(len(tstdata)), key=tstdata.__getitem__)
#class_name = classes[class_index]

#if tstresult==0.0:
#  print 'class', classes[classval]
  message=''
  if trnresult1==0.0 and trnresult2==0.0 and tstresult1==0.0 and tstresult2==0.0:
    if classes1[classval]=='valid' and classes2[classval2]=='valid':
      message='valid'
      valid=valid+1
    elif (classes1[classval]=='valid' and classes2[classval2]=='malicious') or (classes1[classval]=='malicious' and classes2[classval2]=='valid'):
      message='malicious'
      malicious=malicious+1
    elif (classes1[classval]=='invalid' and classes2[classval2]=='valid') or (classes1[classval]=='valid' and classes2[classval2]=='invalid'):
      message='invalid'
      invalid=invalid+1
    elif (classes1[classval]=='invalid' and classes2[classval2]=='malicious') or (classes1[classval]=='malicious' and classes2[classval2]=='invalid'):
      message='malicious'
      malicious=malicious+1
    elif (classes1[classval]=='malicious' and classes2[classval2]=='malicious'):
      message='malicious'
      malicious=malicious+1

#  if tstresult1==0.0:
#    if message=='valid':
#      rss=libxml2.parseDoc(urllib.urlopen('http://localhost/data.xml').read())
#      for url in rss.xpathEval("//users/user[username/text()='"+usrname+"'and password/text()='"+passwd+"']"):
#	print url.name,url.content
#    elif message=='malicious':
#      rss=libxml2.parseDoc(urllib.urlopen('http://localhost/fakedata.xml').read())
#      for url in rss.xpathEval("//users/user[username/text()='"+usrname+"'and password/text()='"+passwd+"']"):
#	print url.name,url.content
#	if url.name=='' and url.content=='':
#	  print 'username and password'
#    elif message=='invalid':
#      print "Error"
  
    
print "valid:", valid
print "invalid", invalid
print "malicious", malicious
end=time.time()
total=end-start
print "time taken is ", total
##RNN code end here

# The returned cookie is available in the os.environ dictionary
cookie_string = os.environ.get('HTTP_COOKIE')

# The first time the page is run there will be no cookies
if not cookie_string:
   print '<p>First visit or cookies disabled</p>'
   x=0
   outFile=open("/var/www/html/counter.txt","w")
   outFile.write(str(x))
   outFile.close()
   print '<br>Login Attempt: ',x+1

else: # Run the page twice to retrieve the cookie
   print '<br><p>The returned cookie string was "' + cookie_string + '"</p>'
   # load() parses the cookie string
   cookie.load(cookie_string)
   # Use the value attribute of the cookie to get it
   lastvisit = float(cookie['lastvisit'].value)
   
   print '<br><p>Your last visit was at',
   print time.asctime(time.localtime(lastvisit)), '</p>'
   print lastvisit
   print time.time()
   print '<br>The last visit was before', time.time()-lastvisit
   inFile=open("/var/www/html/counter.txt","r")
   hits=inFile.readline()
   x=int(hits)+1
   inFile.close()
   outFile=open("/var/www/html/counter.txt","w")
   outFile.write(str(x))
   outFile.close()
   print '<br>Login Attempt:',x

print '</body></html>'

