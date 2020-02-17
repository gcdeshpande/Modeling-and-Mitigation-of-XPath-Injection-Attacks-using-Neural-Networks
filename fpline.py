import numpy as np
import pylab as pl

x1=[50,100,150,200,250,300,350,400,450,500]
y1=[99,7,5,6,5,4,8,8,10,10]

x2=x1
y2=[72,20,34,38,57,63,76,58,58,45]
modPlot=pl.plot(x1,y1,'k')
nmodPlot=pl.plot(x2, y2,'b')
pl.legend([modPlot,nmodPlot],('Modular Neural Network','Single Neural Network'))
#pl.ylim(0,110)

pl.title('Plot of Number of Valid Inputs Not Detected vs Number of Epochs')
pl.xlabel('Number of Epochs')
pl.ylabel('Number of Valid Inputs Not Detected')
pl.show()