#!/usr/bin/env python
import matplotlib.pyplot as plt
import numpy as np
import pylab as pl

fig = plt.figure()
ax1 = fig.add_subplot(121)

## the data
N=10
x = (0.72, 0.20, 0.34, 0.38, 0.57, 0.63, 0.76, 0.58, 0.58, 0.45)
y= (0.235, 0.81, 0.73, 0.585, 0.41, 0.32, 0.27, 0.41, 0.425, 0.525)

## left panel
ax1.scatter(x,y,color='blue',s=10,edgecolor='none')
ax1.set_aspect(1./ax1.get_data_ratio()) # make axes square
ax1.set_ylim([0,1])
ax1.set_xlim([0,1])

p = (0.99, 0.07, 0.05, 0.06, 0.05, 0.04, 0.08, 0.08, 0.10, 0.10)
q= (0.005, 0.915, 0.955, 0.965, 0.945, 0.960, 0.925, 0.910, 0.90, 0.92)



## left panel
ax1.scatter(p,q,color='red',s=10,edgecolor='none')
ax1.set_aspect(1./ax1.get_data_ratio()) # make axes square
ax1.set_ylim([0,1])
ax1.set_xlim([0,1])
ax1.set_xlabel("False Positive Rate")
ax1.set_ylabel("True Positive Rate")
ax1.set_title('ROC Space')


dx=[0,1]
dy=[0,1]
plt.plot(dx,dy,'k')
plt.show()


