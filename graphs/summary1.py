#!/usr/bin/env python
# a bar plot with errorbars
import numpy as np
import matplotlib.pyplot as plt

N = 4
modData = (84.2,15.8,83.8,16.2)
#menStd =   (2, 3, 4, 1, 2)

ind = np.arange(N)  # the x locations for the groups
width = 0.35       # the width of the bars

fig = plt.figure()
ax = fig.add_subplot(111)
rects1 = ax.bar(ind, modData, width, color='#6495ed')

nmodData = (46.5,53.5,47.9,52.1)
#womenStd =   (3, 5, 2, 3, 3)
rects2 = ax.bar(ind+width, nmodData, width, color='#d3d3d3')

# add some
ax.set_ylabel('')
ax.set_xlabel('')
ax.set_title('Average Detection Rate with Outlier')
ax.set_xticks(ind+width)
ax.set_xticklabels( ('True Positives', 'False Negatives', 'True Negatives', 'False Positives') )
ax.set_ylim(0,90)
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
