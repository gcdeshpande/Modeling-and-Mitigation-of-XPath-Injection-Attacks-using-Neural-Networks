import numpy as np
import pylab as pl

x1=[0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]
y1=[0.235, 0.81, 0.73, 0.585, 0.41, 0.32, 0.27, 0.41, 0.425, 0.525]

x2=x1
y2=[0.005, 0.915, 0.955, 0.965, 0.945, 0.960, 0.925, 0.910, 0.90, 0.92]
modPlot=pl.plot(x1,y1,'k')
nmodPlot=pl.plot(x2, y2,'b')
pl.legend([modPlot,nmodPlot],('Modular Neural Network','Single Neural Network'))
#pl.ylim(0,110)

pl.title('Plot of Number of Valid Inputs Not Detected vs Number of Epochs')
pl.xlabel('Number of Epochs')
pl.ylabel('Number of Valid Inputs Not Detected')
pl.show()
