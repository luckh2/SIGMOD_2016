#!/usr/bin/env python
# a bar plot with errorbars
import numpy as np
import matplotlib.pyplot as plt

N = 2
Kira = (2127, 1295)
Dis = (2280, 1565)
Dis_meta = (148, 139)
Rep = (4918, 3175)
Rep_meta = (1991, 1553)

ind = 0.125+np.arange(N)  # the x locations for the groups
width = 0.25       # the width of the bars

ax = plt.subplot()
ax.set_ylim([0, 7500])
rects1 = ax.bar(ind, Kira, width, color='b')
rects2 = ax.bar(ind+width, Dis, width, color='orange', hatch="/")
rects3 = ax.bar(ind+width, Dis_meta, width, color='red', bottom=Dis, hatch="x")

rects4 = ax.bar(ind+width*2, Rep, width, color='green', hatch="\\")
rects5 = ax.bar(ind+width*2, Rep_meta, width, color='red', bottom=Rep, hatch="x")

ax.grid(True)

# add some text for labels, title and axes ticks
ax.set_xlabel('Scale (number of cores)', size='x-large')
ax.set_ylabel('Time-to-solution (seconds)', size='x-large')
ax.set_xticks(ind+width*1.5)
ax.set_xticklabels( ('128', '256'), size='x-large') 
plt.yticks(size='large')
ax.legend( (rects1[0], rects2[0], rects4[0], rects3[0]), ('Kira SE', 'Distributed (no resilience)', 'Replicated', 'Metadata Overhead') )

plt.show()

