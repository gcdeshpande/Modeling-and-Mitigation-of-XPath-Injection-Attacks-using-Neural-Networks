import numpy as np
import pylab as pl

x1=[50,100,150,200,250,300,350,400,450,500]
y1=[100,10,4,1,6,4,7,10,10,6]

x2=x1
y2=[81,18,20,45,61,73,70,60,57,50]
modPlot=pl.plot(x1,y1,'k')
nmodPlot=pl.plot(x2, y2,'b')
pl.legend([modPlot,nmodPlot],('Modular Neural Network','Single Neural Network'))
#pl.ylim(0,110)

pl.title('Plot of Number of Attacks Not Detected vs Number of Epochs')
pl.xlabel('Number of Epochs')
pl.ylabel('Number of Attacks Not Detected')
pl.show()