import numpy as np
import pylab as pl

x1=[50,100,150,200,250,300,350,400,450,500]
y1=[1,93,95,94,95,96,92,92,90,90]

x2=x1
y2=[28,80,66,62,43,37,24,42,42,55]
modPlot=pl.plot(x1,y1,'k')
nmodPlot=pl.plot(x2, y2,'b')
pl.legend([modPlot,nmodPlot],('Modular Neural Network','Single Neural Network'))
pl.ylim(0,110)

pl.title('Plot of Number of Valid Inputs Detected vs Number of Epochs')
pl.xlabel('Number of Epochs')
pl.ylabel('Number of Valid Inputs Detected')
pl.show()