#!/usr/bin/env python
# a bar plot with errorbars
import numpy as np
import matplotlib.pyplot as plt

N = 4
SEMeta = (58.56666667, 37.94, 40.29666667, 48.41666667)
SEAll = (481.7466667, 244.1666667, 154.1066667, 104.15)


ind = 0.1+np.arange(N)  # the x locations for the groups
width = 0.4       # the width of the bars

ax = plt.subplot()
#ax.set_ylim([1000, 80000])


rects1 = ax.bar(ind, SEMeta, width, color='blue')
rects2 = ax.bar(ind+width, SEAll, width, color='orange', hatch="/")
ax.grid(True)

#ax.set_yticklabels((500, 20000, 40000, 60000, 80000), size='large')


ax.set_xlabel('Scale (Number of Machines)', size='x-large')
ax.set_ylabel('Wall Clock Time (seconds)', size='x-large', labelpad=20)
ax.set_xticks(ind+0.4)
ax.set_xticklabels( ('8', '16', '32', '64'), size='x-large') 
ax.legend( (rects1[0], rects2[0]), ('SE Meta-only', 'SE Meta+Data'), loc='best', ncol=2)
ax.set_yticklabels((0, 100, 200, 300, 400, 500), size='large')


plt.show()