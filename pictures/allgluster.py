#!/usr/bin/env python
# a bar plot with errorbars
import numpy as np
import matplotlib.pyplot as plt

N = 2
Kira = (268.1, 152.3)
Dis = (198.7, 119.3)
Dis_meta = (15, 10)
Rep = (197.3, 163.4)
Rep_meta = (39, 64)
Str = (144.9, 82.7)
Str_meta = (98, 128)
Str_Rep = (189.5, 143.4)
Str_Rep_meta = (156, 104)

ind = 0.1+np.arange(N)  # the x locations for the groups
width = 0.16       # the width of the bars

ax = plt.subplot()
ax.set_ylim([0, 450])
rects1 = ax.bar(ind, Kira, width, color='b')
rects2 = ax.bar(ind+width, Dis, width, color='orange', hatch="/")
rects3 = ax.bar(ind+width, Dis_meta, width, color='red', bottom=Dis, hatch="x")

rects4 = ax.bar(ind+width*2, Rep, width, color='green', hatch="\\")
rects5 = ax.bar(ind+width*2, Rep_meta, width, color='red', bottom=Rep, hatch="x")

rects6 = ax.bar(ind+width*3, Str, width, color='yellow', hatch="+")
rects7 = ax.bar(ind+width*3, Str_meta, width, color='red', bottom=Str, hatch="x")

rects8 = ax.bar(ind+width*4, Str_Rep, width, color='purple', hatch="-")
rects9 = ax.bar(ind+width*4, Str_Rep_meta, width, color='red', bottom=Str_Rep, hatch="x")
ax.grid(True)

# add some text for labels, title and axes ticks
ax.set_xlabel('Scale (number of cores)', size='x-large')
ax.set_ylabel('Time-to-solution (seconds)', size='x-large')
ax.set_xticks(ind+width*2.5)
ax.set_xticklabels( ('128', '256'), size='x-large') 
plt.yticks(size='large')
ax.legend( (rects1[0], rects2[0], rects4[0], rects6[0], rects8[0], rects3[0]), ('Kira SE', 'Distributed (no resilience)', 'Replicated', 'Striped (no resilience)', 'Striped Rplicated', 'Metadata Overhead') )

plt.show()

