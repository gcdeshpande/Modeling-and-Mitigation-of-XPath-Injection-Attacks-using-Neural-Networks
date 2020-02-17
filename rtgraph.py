#!/usr/bin/env python
# a bar plot with errorbars
import numpy as np
import matplotlib.pyplot as plt

N = 10
modData = (10.23,20.27,30.98,40.74,51.31,62.05,70.54,81.47,92.27,101.75)
#menStd =   (2, 3, 4, 1, 2)

ind = np.arange(N)  # the x locations for the groups
width = 0.35       # the width of the bars

fig = plt.figure()
ax = fig.add_subplot(111)
rects1 = ax.bar(ind, modData, width, color='#6495ed')

nmodData = (15.31,30.20,45.74,61.32,75.61,90.78,106.34,120.45,136.17,150.87)
#womenStd =   (3, 5, 2, 3, 3)
rects2 = ax.bar(ind+width, nmodData, width, color='#d3d3d3')

# add some
ax.set_ylabel('Response Time')
ax.set_xlabel('Number of Samples')
ax.set_title('Comparison of Response time')
ax.set_xticks(ind+width)
ax.set_xticklabels( ('10', '20', '30', '40', '50','60', '70', '80', '90', '100') )
ax.set_ylim(0,190)
ax.legend( (rects1[0], rects2[0]), ('Modular Neural Networks', 'Single Neural Network') )

def autolabel(rects):
    # attach some text labels
    for rect in rects:
        height = rect.get_height()
        ax.text(rect.get_x()+rect.get_width()/2., 1.02*height, '%d'%int(height),
                ha='center', va='bottom')

autolabel(rects1)
autolabel(rects2)

plt.show()
