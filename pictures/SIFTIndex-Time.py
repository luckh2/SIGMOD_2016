#!/usr/bin/env python
# a bar plot with errorbars
import numpy as np
import matplotlib.pyplot as plt

N = 5
Baseline = (61.32, 61.32, 61.32, 61.32, 61.32)
Metadata = (0, 89.78, 89.78, 89.78, 89.78)
Data = (0, 68.84, 67.92, 79.26, 73.49)
Index = (0, 0, 33.9, 69.93, 348.95)


ind = 0.125+np.arange(N)  # the x locations for the groups
width = 0.75       # the width of the bars

ax = plt.subplot()
#ax.set_ylim([0, 4000])
rects1 = ax.bar(ind, Baseline, width, color='blue')
rects2 = ax.bar(ind, Metadata, width, color='orange', bottom=Baseline, hatch="/")
rects3 = ax.bar(ind, Data, width, color='green', bottom=np.add(Metadata,Baseline), hatch="\\")
rects4 = ax.bar(ind, Index, width, color='red', bottom=np.add(np.add(Metadata,Baseline),Data), hatch="x")

ax.grid(True)

# add some text for labels, title and axes ticks
ax.set_xlabel('Region Lineage Index Strategy', size='x-large')
ax.set_ylabel('Time-to-solution (seconds)', size='x-large')
ax.set_xticks(ind+0.375)
ax.set_xticklabels( ('NoLineage', 'NoIndex', 'RTree', 'KMeans-1', 'KMeans-5'), size='x-large') 
plt.yticks(size='large')
ax.legend( (rects1[0], rects2[0], rects3[0], rects4[0]), ('Baseline', 'Metadata', 'Data', 'Index'), loc='best')

plt.show()

