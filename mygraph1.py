import numpy as np
import pylab as pl

y1=[10,20,30,40,50,60,70,80,90,100]
x1=[10.23,20.27,30.98,40.74,51.31,62.05,70.54,81.47,92.27,101.75]

y2=y1
x2=[15.31,30.20,45.74,61.32,75.61,90.78,106.34,120.45,136.17,150.87]
pl.plot(x1,y1)
pl.plot(x2,y2)
pl.title('Plot of Number of Attacks Detected vs Number of Epochs')
pl.xlabel('Response Time')
pl.ylabel('Number of Samples')
pl.show()