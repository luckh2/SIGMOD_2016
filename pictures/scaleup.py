#!/usr/bin/env python
# a bar plot with errorbars
import numpy as np
import matplotlib.pyplot as plt

N = 4
Kira = (4539, 2322, 1236, 819)
C = (612, 514, 408, 371)
Slowdown=(7.42, 4.52, 3.03, 2.21)

ind = 0.15+np.arange(N)  # the x locations for the groups
width = 0.35       # the width of the bars

ax = plt.gca()
ax.grid(True)
plt.yticks(size='large')
ax_c = ax.twinx()
ax_c.set_ylim([0, 9])
rects3 = ax_c.plot(ind+width, Slowdown, linestyle='-', marker='o', c='green', linewidth=4.0)
rects1 = ax.bar(ind, Kira, width, color='b')
rects2 = ax.bar(ind+width, C, width, color='orange', hatch="/")
plt.yticks(size='large')
# add some text for labels, title and axes ticks
ax.set_xlabel('Scale', size='x-large')
ax.set_ylabel('Time-to-solution (seconds)', size='x-large')
ax_c.set_ylabel('Slowdown', size='x-large')
ax.set_xticks(ind+width)
ax.set_xticklabels( ('1 core', '2 cores', '4 cores', '8 cores'), size='x-large') 

ax.legend( (rects1[0], rects2[0], rects3[0]), ('Kira SE', 'C', 'Slowdown') )

plt.show()

