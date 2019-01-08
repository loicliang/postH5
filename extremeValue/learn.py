#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov 14 16:41:03 2018

@author: xliang
"""
import matplotlib.pyplot as plt
import numpy as np

import pandas as pd


import plotmyh5 as pm


#df1 = pd.DataFrame({'key':['b','b','a','c','a','a','b'],'data1':range(7)}) 
#df2 = pd.DataFrame({'key':['a','b','d'],'data2':range(3)}) 
#df3=pd.merge(df1,df2)
#
#
#tips = pd.read_csv('tips.csv')
#tips['tip_pct'] = tips['tip'] / tips['total_bill']
#grouped = tips.groupby(['sex','smoker'])
#grouped_pct = grouped['tip_pct']
#c=grouped_pct.agg(['mean','std'])







#import numpy as np
#import matplotlib.pyplot as plt
#
#men_means, men_std = (20, 35, 30, 35, 27), (2, 3, 4, 1, 2)
#women_means, women_std = (25, 32, 34, 20, 25), (3, 5, 2, 3, 3)
#
#ind = np.arange(len(men_means))  # the x locations for the groups
#width = 0.35  # the width of the bars
#
#fig, ax = plt.subplots()
#rects1 = ax.bar(ind - width/2, men_means, width, yerr=men_std,
#                color='SkyBlue', label='Men')
#rects2 = ax.bar(ind + width/2, women_means, width, yerr=women_std,
#                color='IndianRed', label='Women')
#
## Add some text for labels, title and custom x-axis tick labels, etc.
#ax.set_ylabel('Scores')
#ax.set_title('Scores by group and gender')
#ax.set_xticks(ind)
#ax.set_xticklabels(('G1', 'G2', 'G3', 'G4', 'G5'))
#ax.legend()
#
#
#def autolabel(rects, xpos='center'):
#    """
#    Attach a text label above each bar in *rects*, displaying its height.
#
#    *xpos* indicates which side to place the text w.r.t. the center of
#    the bar. It can be one of the following {'center', 'right', 'left'}.
#    """
#
#    xpos = xpos.lower()  # normalize the case of the parameter
#    ha = {'center': 'center', 'right': 'left', 'left': 'right'}
#    offset = {'center': 0.5, 'right': 0.57, 'left': 0.43}  # x_txt = x + w*off
#
#    for rect in rects:
#        height = rect.get_height()
#        ax.text(rect.get_x() + rect.get_width()*offset[xpos], 1.01*height,
#                '{}'.format(height), ha=ha[xpos], va='bottom')
#
#
#autolabel(rects1, "left")
#autolabel(rects2, "right")
#
#plt.show()










#fig = plt.figure()  # an empty figure with no axes
#fig.suptitle('No axes on this figure')  # Add a title so we know which it is
#
#fig, ax_lst = plt.subplots(1, 1)  # a figure with a 2x2 grid of Axes
#


#
#x = np.linspace(0, 2, 100)
#
#plt.plot(x, x, label='linear')
#plt.plot(x, x**2, label='quadratic')
#plt.plot(x, x**3, label='cubic')
#
#plt.xlabel('x label')
#plt.ylabel('y label')
#
#plt.title("Simple Plot")
#
#plt.legend()
#
#plt.show()
#
#
#
#

fig, ax=plt.subplots()

a=pm.test()

b=a[a.columns[1]]

for i in a.columns:
    b=a[i]
    ax.hist(x=b.values,bins=100,label=i,density=True,cumulative=True,histtype='step')



ax.grid(True)
ax.legend(loc='right')

