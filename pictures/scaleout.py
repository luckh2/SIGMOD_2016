#!/usr/bin/env python
# a bar plot with errorbars
import numpy as np
import matplotlib.pyplot as plt

N = 6
Kira = (3806, 996, 511, 268, 152, 104)
C = (1874, 887, 398, 236, 161, 134)

ind = 0.15+np.arange(N)  # the x locations for the groups
width = 0.35       # the width of the bars

ax = plt.subplot()
ax.set_yscale("log", nonposx='clip')
rects1 = ax.bar(ind, Kira, width, color='b', log='True')
rects2 = ax.bar(ind+width, C, width, color='orange', hatch="/", log='True')

ax.set_ylim([1, 10000])
ax.grid(True)

# add some text for labels, title and axes ticks
ax.set_xlabel('Scale (number of cores)', size='x-large')
ax.set_ylabel('Time-to-solution (seconds)', size='x-large')
ax.set_xticks(ind+width)
ax.set_xticklabels( ('8', '32', '64', '128', '256', '512'), size='x-large') 
plt.yticks(size='large')
ax.legend( (rects1[0], rects2[0]), ('Kira SE', 'C') )

plt.show()

