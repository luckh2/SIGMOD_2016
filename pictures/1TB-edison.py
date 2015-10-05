#!/usr/bin/env python
# a bar plot with errorbars
import numpy as np
import matplotlib.pyplot as plt

N = 1
Kira = (1295)
Idle = (938)
Idle_meta = (118)
Busy = (1983)
Busy_meta = (284)

ind = 0.35+np.arange(N)  # the x locations for the groups
width = 0.1       # the width of the bars

ax = plt.subplot()
#ax.set_ylim([0, 2500])
rects1 = ax.bar(ind, Kira, width, color='b')
rects2 = ax.bar(ind+width, Idle, width, color='orange', hatch="/")
rects3 = ax.bar(ind+width, Idle_meta, width, color='red', bottom=Idle, hatch="x")

rects4 = ax.bar(ind+width*2, Busy, width, color='green', hatch="\\")
rects5 = ax.bar(ind+width*2, Busy_meta, width, color='red', bottom=Busy, hatch="x")

ax.grid(True)

# add some text for labels, title and axes ticks
ax.set_xlabel('Scale (number of cores)', size='x-large')
ax.set_ylabel('Time-to-solution (seconds)', size='x-large')
ax.set_xticks(ind+width*1.5)
ax.set_xticklabels( ('512', ''), size='x-large') 
plt.yticks(size='large')
ax.legend((rects1[0], rects2[0], rects4[0], rects3[0]), ('Kira SE', 'Edison Idle', 'Edison Busy', 'Metadata Overhead'),loc='best')

plt.show()

