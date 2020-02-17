import numpy as np
import pylab as pl

x=[50,100,150,200,250,300,350,400,450,500]
y=[99,7,5,6,5,4,8,8,10,10]
pl.plot(x,y)
pl.title('Plot of Number of Valid Inputs Not Detected vs Number of Epochs')
pl.xlabel('Number of Epochs')
pl.ylabel('Number of Valid Inputs Not Detected')
pl.show()