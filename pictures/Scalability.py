#!/usr/bin/env python
import numpy as np
import matplotlib.pyplot as plt

fig,(ax1,ax2,ax3) = plt.subplots(1, 3)

xlabels = ("4","8", "16", "32", "64")
ylabels = ("0.25", "1/2", "1", "2", "4", "8")
scale = (8,16,32,64)
Ideal = (1, 2, 4, 8)
VOC = (1, 1.24, 1.32, 1.32)
VOCLower = (1, 2.06, 2.49, 2.97)
VOCUpper = (1, 2.4, 4.16, 5.63)

SE = (1, 1.06, 0.81, 0.55)
SELower = (1, 1.54, 1.45, 1.21)
SEUpper = (1, 1.97, 3.13, 4.62)

MNIST = (1, 1.08, 1.26, 0.95)
MNISTLower = (1, 1.14, 1.15, 1.16)
MNISTUpper = (1, 1.07, 1.12, 1.12)


ax1.set_xlim(8, 64)
ax1.set_ylim(0.5, 8)
line1 = ax1.loglog(scale, VOC, basex=2, basey=2, lw=3, marker='s', mew=0, ms=10)
line2 = ax1.loglog(scale, VOCLower, basex=2, basey=2, lw=3, marker='^', mew=0, ms=10)
line3 = ax1.loglog(scale, VOCUpper, basex=2, basey=2, lw=3, marker='D', mew=0, ms=10)
line4 = ax1.loglog(scale, Ideal, basex=2, basey=2, lw=3)
ax1.set_xticklabels(xlabels, size='xx-large')
ax1.set_yticklabels(ylabels, size='xx-large')
#ax1.legend((line1[0], line2[0], line3[0], line4[0]), ('NoLineage', 'Meta', 'Meta+Data', 'Ideal'), loc='best', prop={'size':20})
ax1.grid(True)
ax1.set_title('VOCSIFTFisher', size='xx-large', y=1.2)
ax1.set_ylabel('Speedup over 8 nodes (x)', size='xx-large')

ax2.set_xlim(8, 64)
ax2.set_ylim(0.5, 8)
line5 = ax2.loglog(scale, SE, basex=2, basey=2, lw=3, marker='s', mew=0, ms=10)
line6 = ax2.loglog(scale, SELower, basex=2, basey=2, lw=3, marker='^', mew=0, ms=10)
line7 = ax2.loglog(scale, SEUpper, basex=2, basey=2, lw=3, marker='D', mew=0, ms=10)
line8 = ax2.loglog(scale, Ideal, basex=2, basey=2, lw=3)
ax2.set_xticklabels(xlabels, size='xx-large')
ax2.set_yticklabels(ylabels, size='xx-large')
ax2.legend((line5[0], line6[0], line7[0], line8[0]), ('NoLineage', 'Meta', 'Meta+Data', 'Ideal'), loc='upper center', prop={'size':20}, bbox_to_anchor=(0.5, 1.2), ncol=4)
ax2.grid(True)
ax2.set_title('Source Extractor', size='xx-large', y=1.2)
ax2.set_xlabel("Number of nodes", size='xx-large')

ax3.set_xlim(8, 64)
ax3.set_ylim(0.5, 8)
line9 = ax3.loglog(scale, MNIST, basex=2, basey=2, lw=3, marker='s', mew=0, ms=10)
line10 = ax3.loglog(scale, MNISTLower, basex=2, basey=2, lw=3, marker='^', mew=0, ms=10)
line11 = ax3.loglog(scale, MNISTUpper, basex=2, basey=2, lw=3, marker='D', mew=0, ms=10)
line12 = ax3.loglog(scale, Ideal, basex=2, basey=2, lw=3)
ax3.set_xticklabels(xlabels, size='xx-large')
ax3.set_yticklabels(ylabels, size='xx-large')
#ax3.legend((line9[0], line10[0], line11[0], line12[0]), ('NoLineage', 'Meta', 'Meta+Data', 'Ideal'), loc='best', prop={'size':20})
ax3.grid(True)
ax3.set_title('MNIST', size='xx-large', y=1.2)

plt.show()
