import numpy as np
import pylab as pl

x=[50,100,150,200,250,300,350,400,450,500]
y=[100,10,4,1,6,4,7,10,10,6]
pl.plot(x,y)
pl.title('Plot of Number of Not Attacks Detected vs Number of Epochs')
pl.xlabel('Number of Epochs')
pl.ylabel('Number of Attacks Not Detected')
pl.show()