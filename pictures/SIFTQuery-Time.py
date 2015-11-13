#!/usr/bin/env python
# a bar plot with errorbars
import numpy as np
import matplotlib.pyplot as plt

N = 4
Random = (321.1, 143.96, 156.42, 144.57)
Batch100 = (1120.07, 165.83, 171.79, 156.58)
Batch1K = (10045.12, 325.56, 267.13, 224.42)
Batch10K = (76594.73, 3434.05, 2572.04, 2226.05)

RandomSDV = (26, 6.37, 4.31, 0.95)
Batch100SDV = (55.06, 14.93, 13.25, 23.98)
Batch1KSDV = (546.67, 10.45, 37.69, 20.72)
Batch10KSDV = (6194.96, 564.33, 312.15, 300.34)



ind = 0.1+np.arange(N)  # the x locations for the groups
width = 0.2       # the width of the bars

f, (ax, ax2) = plt.subplots(2, 1, sharex=True)
ax.set_ylim([1000, 80000])
ax2.set_ylim([0, 500])

ax.spines['bottom'].set_visible(False)
ax2.spines['top'].set_visible(False)
ax.xaxis.tick_top()
ax.tick_params(labeltop='off')
ax2.xaxis.tick_bottom()

rects1 = ax.bar(ind, Random, width, color='blue')
rects2 = ax.bar(ind+width, Batch100, width, color='orange', hatch="/")
rects3 = ax.bar(ind+2*width, Batch1K, width, color='red', hatch="x")
rects4 = ax.bar(ind+3*width, Batch10K, width, color='green', hatch="\\")
ax2.bar(ind, Random, width, color='blue')
ax2.bar(ind+width, Batch100, width, color='orange', hatch="/")
ax2.bar(ind+2*width, Batch1K, width, color='red', hatch="x")
ax2.bar(ind+3*width, Batch10K, width, color='green', hatch="\\")
ax.grid(True)
ax2.grid(True)

ax.set_yticklabels((500, 20000, 40000, 60000, 80000), size='large')
ax2.set_yticklabels((0, 100, 200, 300, 400, 500), size='large')

#args = dict(horizontalalignment='left', verticalalignment='bottom')
# add some text for labels, title and axes ticks
ax2.set_xlabel('Region Lineage Index Strategy', size='x-large')
ax2.set_ylabel('Query Turnaround (ms)', size='x-large', labelpad=20)
ax2.yaxis.set_label_coords(-0.1, 1.0)
ax.set_xticks(ind+0.45)
ax2.set_xticklabels( ('NoIndex', 'RTree', 'KMeans-1', 'KMeans-5'), size='x-large') 
ax.legend( (rects1[0], rects2[0], rects3[0], rects4[0]), ('Random', 'Batch100', 'Batch1K', 'Batch10K'), loc='best', ncol=2)
ax.yaxis.set_ticks((500, 20000, 40000, 60000, 80000))

d = .015
kwargs = dict(transform=ax.transAxes, color='k', clip_on=False)
ax.plot((-d,+d),(-d,+d), **kwargs)      # top-left diagonal
ax.plot((1-d,1+d),(-d,+d), **kwargs)    # top-right diagonal

kwargs.update(transform=ax2.transAxes)  # switch to the bottom axes
ax2.plot((-d,+d),(1-d,1+d), **kwargs)   # bottom-left diagonal
ax2.plot((1-d,1+d),(1-d,1+d), **kwargs) # bottom-right diagonal

plt.show()

