#!/usr/bin/env python
# a bar plot with errorbars
import numpy as np
import matplotlib.pyplot as plt

N = 5
VOCMeta = (1422.526667, 466.52, 225.9766667, 187.7, 156.86)
VOCAll = (2221.25, 1313.92, 548.04, 316.1166667, 233.2533333)




ind = 0.1+np.arange(N)  # the x locations for the groups
width = 0.4       # the width of the bars

ax = plt.subplot()
#ax.set_ylim([1000, 80000])


rects1 = ax.bar(ind, VOCMeta, width, color='blue')
rects2 = ax.bar(ind+width, VOCAll, width, color='orange', hatch="/")
ax.grid(True)



ax.set_xlabel('Scale (Number of Machines)', size='x-large')
ax.set_ylabel('Wall Clock Time (seconds)', size='x-large', labelpad=20)
ax.set_xticks(ind+0.4)
ax.set_xticklabels( ('4', '8', '16', '32', '64'), size='x-large') 
ax.legend( (rects1[0], rects2[0]), ('SIFTFisher Meta-only', 'SIFTFisher Meta+Data'), loc='best')
ax.set_yticklabels((0, 500, 1000, 1500, 2000, 2500), size='large')
#ax.yaxis.set_ticks((500, 20000, 40000, 60000, 80000))

plt.show()

