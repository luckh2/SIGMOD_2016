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

ax = plt.subplot()
ax.set_ylim([1, 100000])
ax.set_yscale("log", nonposx='clip')
rects1 = ax.bar(ind, Random, width, color='blue', log='True', yerr=np.multiply(RandomSDV,3), ecolor='black')
rects2 = ax.bar(ind+width, Batch100, width, color='orange', hatch="/", log='True', yerr=np.multiply(Batch100SDV,3), ecolor='black')
rects3 = ax.bar(ind+2*width, Batch1K, width, color='red', hatch="x", log='True', yerr=np.multiply(Batch1KSDV,3), ecolor='black')
rects4 = ax.bar(ind+3*width, Batch10K, width, color='green', hatch="\\", log='True', yerr=np.multiply(Batch10KSDV,3), ecolor='black')

ax.grid(True)

# add some text for labels, title and axes ticks
ax.set_xlabel('Region Lineage Index Strategy', size='x-large')
ax.set_ylabel('Query Turnaround (miliseconds)', size='x-large')
ax.set_xticks(ind+0.4)
ax.set_xticklabels( ('NoIndex', 'RTree', 'KMeans-1', 'KMeans-5'), size='x-large') 
plt.yticks(size='large')
ax.legend( (rects1[0], rects2[0], rects3[0], rects4[0]), ('Random', 'Batch100', 'Batch1000', 'Batch10000'), loc='best')

plt.show()

