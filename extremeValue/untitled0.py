#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov 21 11:09:26 2018

@author: xliang
"""

# Thickness of the gradient
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

#
## Fixing random state for reproducibility
#np.random.seed(19680801)
#
#
## create some data to use for the plot
#dt = 0.001
#t = np.arange(0.0, 10.0, dt)
#r = np.exp(-t[:1000] / 0.05)  # impulse response
#x = np.random.randn(len(t))
#s = np.convolve(x, r)[:len(x)] * dt  # colored noise
#
## the main axes is subplot(111) by default
#plt.plot(t, s)
#plt.axis([0, 1, 1.1 * np.min(s), 2 * np.max(s)])
#plt.xlabel('time (s)')
#plt.ylabel('current (nA)')
#plt.title('Gaussian colored noise')
#
## this is an inset axes over the main axes
#a = plt.axes([.65, .6, .2, .2])
##n, bins, patches = plt.hist(s, 400, density=True)
##plt.title('Probability')
#plt.xticks([])
#plt.yticks([])
#
## this is another inset axes over the main axes
#a = plt.axes([0.2, 0.6, .2, .2])
#plt.plot(t[:len(r)], r)
#plt.title('Impulse response')
#plt.xlim(0, 0.2)
#plt.xticks([])
#plt.yticks([])
#
#plt.show()


x=pd.Series(np.exp(np.arange(20)))
x.plot(label=u'原始数据图',legend=True)
plt.grid(True)
plt.show()

x.plot(logy=True,label=u'对数数据图',legend=True) #这个函数里的参数logy=True时，是以10为底的
plt.grid(True)
plt.show()

import matplotlib.lines as mlines


plt.figure()
x=pd.Series(np.exp(np.arange(20)))
p1=x.plot(label=u'原始数据图')
plt.ylabel('正常坐标')
x2=pd.Series(np.log10(x)) #np.log()是以e为底的
p2=x2.plot(secondary_y=True,style='--',color='r',)
#plt.yticks(plt.yticks()[0],['$10^%d$'%w for w in range(len(plt.yticks()[0]))])
#plt.ylabel('指数坐标')
#blue_line = mlines.Line2D([],[],linestyle='-',color='blue',markersize=2, label=u'原始数据图')
#red_line= mlines.Line2D([],[],linestyle='--',color='red',markersize=2, label=u'对数数据图')
plt.legend(handles=[blue_line,red_line],loc='upper left')
plt.grid(True)
plt.show()


