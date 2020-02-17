import numpy as np
import pylab as pl

x1=[50,100,150,200,250,300,350,400,450,500]
y1=[0, 90, 96, 99, 94, 96, 93, 90, 90, 94]

x2=x1
y2=[19, 82, 80, 55, 39, 27, 30, 40, 43, 50]
modPlot=pl.plot(x1,y1,'k')
nmodPlot=pl.plot(x2, y2,'b')
pl.legend([modPlot,nmodPlot],('Modular Neural Network','Single Neural Network'))
pl.ylim(0,110)

pl.title('Plot of Number of Attacks Detected vs Number of Epochs')
pl.xlabel('Number of Epochs')
pl.ylabel('Number of Attacks Detected')
pl.show()