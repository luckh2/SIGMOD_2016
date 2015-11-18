#!/usr/bin/env python
# a bar plot with errorbars
import numpy as np
import matplotlib.pyplot as plt

N = 7
Random = (249.27, 184.2233333, 163.9866667, 202.3233333, 153.7066667, 266.7366667, 143.9500317)
Batch1K = (236.36, 212.9, 190.8266667, 195.2566667, 233.94, 335.9233333, 325.55882)
Batch10K = (261.57, 237.16, 208.7866667, 235.7366667, 264.9266667, 354.4, 3120.267287)
Batch100K = (686.6566667, 738.6166667, 801.4833333, 824.5833333, 1212.776667, 1142.623333, 14974.48)
Batch1M = (5929.41, 7668.692857, 7344.086667, 7335.143333, 14678.38333, 10686.97667, 132887.5867)

RandomSDV = (8.605039221, 3.990054302, 3.296927863, 6.900813962, 1.887361474, 9.142107707, 6.365963769)
Batch1KSDV = (14.15085863, 6.842682223, 8.338203244, 15.58000107, 16.07252003, 4.263922294, 10.45354461)
Batch10KSDV = (5.839768831, 0.6766830868, 3.528545498, 14.22426565, 13.64859456, 6.227543657, 214.938404)
Batch100KSDV = (6.290980316, 4.054088471, 17.98857786, 12.01829577, 22.74252038, 22.66141287, 600.5253666)
Batch1MSDV = (126.840803, 1221.368218, 42.23203681, 93.21184546, 203.0923035, 484.7924923, 402.2884688)



ind = 0.1+np.arange(N)  # the x locations for the groups
width = 0.18       # the width of the bars

ax = plt.subplot()
ax.set_ylim([1, 1000000])

rects1 = ax.bar(ind, Random, width, color='green', yerr=RandomSDV, ecolor='black', error_kw=dict(elinewidth=2))
rects2 = ax.bar(ind+width, Batch1K, width, color='blue', hatch="x", yerr=Batch1KSDV, ecolor='black', error_kw=dict(elinewidth=2))
rects3 = ax.bar(ind+2*width, Batch10K, width, color='yellow', hatch="\\", yerr=Batch10KSDV,ecolor='black', error_kw=dict(elinewidth=2))
rects4 = ax.bar(ind+3*width, Batch100K, width, color='orange', hatch="/", yerr=Batch100KSDV, ecolor='black', error_kw=dict(elinewidth=2))
rects5 = ax.bar(ind+4*width, Batch1M, width, color='red', hatch="-", yerr=Batch1MSDV, ecolor='black', error_kw=dict(elinewidth=2))
ax.grid(True)

#ax.set_yticklabels((500, 20000, 40000, 60000, 80000), size='large')
#ax2.set_yticklabels((0, 100, 200, 300, 400, 500), size='large')

#args = dict(horizontalalignment='left', verticalalignment='bottom')
# add some text for labels, title and axes ticks
ax.set_xlabel('Lineage Type', size='x-large')
ax.set_ylabel('Query Latency (ms)', size='x-large', labelpad=20)
ax.set_yscale('log')
ax.set_xticks(ind+0.45)
ax.set_xticklabels( ('All', 'Identity', 'LinCom', 'Expansion', 'Collapse', 'Join', 'Geometry'), size='x-large') 
ax.legend( (rects1[0], rects2[0], rects3[0], rects4[0], rects5[0]), ('Random', 'Batch1K', 'Batch10K', 'Batch100K', 'Batch1M'), loc='best', ncol=3)

#d = .015
#kwargs = dict(transform=ax.transAxes, color='k', clip_on=False)
#ax.plot((-d,+d),(-d,+d), **kwargs)      # top-left diagonal
#ax.plot((1-d,1+d),(-d,+d), **kwargs)    # top-right diagonal

#kwargs.update(transform=ax2.transAxes)  # switch to the bottom axes
#ax2.plot((-d,+d),(1-d,1+d), **kwargs)   # bottom-left diagonal
#ax2.plot((1-d,1+d),(1-d,1+d), **kwargs) # bottom-right diagonal

plt.show()

