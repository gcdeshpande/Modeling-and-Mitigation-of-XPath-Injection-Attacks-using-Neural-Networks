import numpy as np
import pylab as pl

x=[50,100,150,200,250,300,350,400,450,500]
y=[1,93,95,94,95,96,92,92,90,90]
pl.plot(x,y)
pl.title('Plot of Number of Valid Inputs Detected vs Number of Epochs')
pl.xlabel('Number of Epochs')
pl.ylabel('Number of Valid Inputs Detected')
pl.show()