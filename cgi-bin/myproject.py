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
print '<p>Server time is', time.asctime(time.localtime()), '</p>'

##comment
form=cgi.FieldStorage()
usrname=form.getvalue("txtName", "(no text)")
passwd=form.getvalue("txtPasswd", "(no passwd)")

length=0
for l in usrname:
  length=length+1

#print length

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
code=0  
#print count

if (singleQuotes==1 and alphabets==(length-singleQuotes)) or (dots<=2 and alphabets==(length-dots)) or (alphabets==length) or (digits==length) or (dots<=2 and alphabets==(length-dots-atTheRate) and atTheRate==1):
#  print 'valid'
  code=40
  classval=0
elif singleQuotes>1 or doubleQuotes>0 or equalTo>0 or squareBrackets>0 or roundedBrackets>0 or curlyBrackets>0 or forwardSlash>0 or backwardSlash>0 or dots>=3 or whiteSpace>0 or pipes>0 or atTheRate>1:
#  print 'Malicious'
  code=4000
  classval=2
elif everyThingElse>0:
#  print 'Invalid'
  code=400
  classval=1
  
##comment

##RNN Code start here

classes=['valid', 'invalid', 'malicious']
trndata=ClassificationDataSet(2,class_labels=classes)
trndata.appendLinked([40], [0])
trndata.appendLinked([400], [1])
#trndata.appendLinked([501], [1])
trndata.appendLinked([4000], [2])

trndata._convertToOneOfMany()

tstdata=ClassificationDataSet(2,class_labels=classes)
tstdata.appendLinked([code],[classval])
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
#tstdata._convertToOneOfMany()

# construct LSTM network - note the missing output bias
rnn = buildNetwork( trndata.indim, 50, trndata.outdim, hiddenclass=LSTMLayer, outclass=SoftmaxLayer, outputbias=False, recurrent=True)
#rnn.reset()


#print tstdata
# define a training method
trainer = RPropMinusTrainer( rnn, dataset=trndata, verbose=True )

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
trainer.trainEpochs( 100 )
       
    #trnresult = 100. * (1.0-testOnSequenceData(rnn, trndata))
    #tstresult = 100. * (1.0-testOnSequenceData(rnn, tstdata))
trnresult=percentError(trainer.testOnClassData(), trndata['class'])
tstresult=percentError(trainer.testOnClassData(dataset=tstdata), tstdata['class'])
   # trnresult = testOnSequenceData(rnn, trndata)*100
   # tstresult = testOnSequenceData(rnn, tstdata)*100
 
print "<br>train error: %5.2f%%" % trnresult, ",  test error: %5.2f%%" % tstresult
#print "</font>"
# just for reference, plot the first 5 timeseries
#plot(trndata['input'][0:250,:],'-o')
#hold(True)
#plot(trndata['target'][0:250,0])

print "<br>Number of training patterns: ", len(trndata)
print "<br>Input and output dimensions: ", trndata.indim, trndata.outdim
print "<br>First sample (input, target, class):"
print trndata['input'][0], trndata['target'][0], trndata['class'][0]

#print "Number of training patterns: ", len(tstdata)
#print "output dimensions: ", tstdata.outdim
#print "First sample (input, target, class):"
#print tstdata[0], tstdata[1], tstdata[2]
#print 'class', classes[tstdata['class'][0]]
#class_index = max(xrange(len(tstdata)), key=tstdata.__getitem__)
#class_name = classes[class_index]

#if tstresult==0.0:
#  print 'class', classes[classval]
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
