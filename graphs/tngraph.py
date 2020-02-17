#!/usr/bin/env python
# a bar plot with errorbars
import numpy as np
import matplotlib.pyplot as plt

N = 10
modData = (1, 93, 95, 94, 95, 96, 92, 92, 90, 90)
#menStd =   (2, 3, 4, 1, 2)

ind = np.arange(N)  # the x locations for the groups
width = 0.35       # the width of the bars

fig = plt.figure()
ax = fig.add_subplot(111)
rects1 = ax.bar(ind, modData, width, color='#6495ed')

nmodData = (28, 80, 66, 62, 43, 37, 24, 42, 42, 55)
#womenStd =   (3, 5, 2, 3, 3)
rects2 = ax.bar(ind+width, nmodData, width, color='#d3d3d3')

# add some
ax.set_ylabel('Number of Valid Inputs Detected')
ax.set_xlabel('Number of Epochs')
ax.set_title('Comparison of True Negatives')
ax.set_xticks(ind+width)
ax.set_xticklabels( ('50', '100', '150', '200', '250','300', '350', '400', '450', '500') )
ax.set_ylim(0,120)
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
