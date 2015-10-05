#!/usr/bin/env python
# a bar plot with errorbars
import numpy as np
import matplotlib.pyplot as plt

N = 6
Kira = (100, 98, 98, 93.5, 98.4, 96.1)
C = (100, 50, 25, 12.5, 6.3, 3.2)

ind = 0.15+np.arange(N)  # the x locations for the groups
width = 0.35       # the width of the bars

ax = plt.subplot()
rects1 = ax.bar(ind, Kira, width, color='b')
rects2 = ax.bar(ind+width, C, width, color='orange', hatch="/")
ax.set_ylim([0, 120])
ax.grid(True)

# add some text for labels, title and axes ticks
ax.set_xlabel('Scale (number of cores)', size='x-large')
ax.set_ylabel('Locality hit ratio (percentage)', size='x-large')
ax.set_xticks(ind+width)
ax.set_xticklabels( ('8', '32', '64', '128', '256', '512'), size='x-large') 
plt.yticks(size='large')
ax.legend( (rects1[0], rects2[0]), ('Kira SE', 'C') )

plt.show()

