#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov 13 11:03:51 2018

@author: xliang
"""

#import numpy as np
#from matplotlib import pyplot as plt
#from scipy import optimize
#from scipy.stats import genextreme as gev
#
#dataN = [0.0, 0.0, 0.122194513716, 0.224438902743, 0.239401496259, 0.152119700748, 
#         0.127182044888, 0.069825436409, 0.0299251870324, 0.0199501246883, 0.00997506234414, 
#         0.00498753117207, 0.0]
#
#t = np.linspace(1,13,13)
#fit = gev.fit(dataN,0)
#pdf = gev.pdf(t, *fit)
##plt.plot(t, pdf)
#plt.plot(t, dataN, "o")
#print(fit)



#from scipy.stats import genextreme
#import matplotlib.pyplot as plt
#fig, ax = plt.subplots(1, 1)
#
#c = 0.0
#mean, var, skew, kurt = genextreme.stats(c, moments='mvsk')
#
#x = np.linspace(genextreme.ppf(0.01, c),
#                genextreme.ppf(0.99, c), 10)
#ax.plot(x, genextreme.pdf(x, c),
#       'r-', lw=5, alpha=0.6, label='genextreme pdf')
#rv = genextreme(c)
#ax.plot(x, rv.pdf(x), 'k-', lw=2, label='frozen pdf')
#
#vals = genextreme.ppf([0.001, 0.5, 0.999], c)
#np.allclose([0.001, 0.5, 0.999], genextreme.cdf(vals, c))
#
#r = genextreme.rvs(c, size=1000)
#
#ax.hist(r,bins=1000, density=True, histtype='stepfilled')
#ax.legend(loc='best', frameon=False)
#plt.show()



import numpy as np
import matplotlib.pyplot as plt 
from scipy.stats import genextreme as gev

#tides = np.array([204.25, 184.87, 164.15, 158.54, 194.47, 206.31, 212.04,
#209.24, 186.28, 176.27, 181.72, 199.49, 205.97, 198.42, 187.2, 170.42, 188.22, 
#193.66, 206.12, 204.03, 187.64, 188.66, 190.92, 191.3, 196.25, 191.91, 166.42, 
#188.73, 192.57, 199.81, 193.57, 193.28, 198.45, 192.17, 200.9, 212.57, 205.65,
#188.84, 175.5, 180.52, 199.2, 202.07, 209.27, 202.07, 187.95, 199.11, 206.81, 
#235.44, 204.04, 195.15, 173.85, 163.17, 191.7, 201.87, 212.38, 207.92, 171.61,
#186.32, 201.58, 222.89, 206.96, 200.68, 178.82, 183.91, 198.82, 209.23, 
#224.03, 230.06, 199.87, 201.07, 205.59, 211.58, 210.78, 205.9, 182.66, 199.49, 
#195.04, 196.12, 197.82, 203.91, 188.28, 196.81, 200.88, 201.25, 212.27, 
#178.33, 173.86, 185.71, 191.83, 202.56, 195.54, 189.08, 184.48, 199.92,
#206.66, 198.95, 188.12, 176.24, 161.95, 172.67, 196.1, 207.34, 208.96, 209.65,
#178.95, 188.49, 211.91, 218.64, 201.82, 193.37, 170.33, 185.98, 201.05, 
#212.28, 213.93, 204.78, 195.17, 196.68, 210.0, 211.09, 208.75, 191.5, 201.17,
#190.19, 195.78, 197.68, 209.58, 205.62, 190.79, 198.04, 206.89, 210.84,
#202.58, 180.44, 178.58, 191.25, 209.43, 205.74, 194.24, 192.74, 193.11, 
#209.92, 214.03, 220.04, 187.46, 191.46, 161.37, 180.56, 192.58, 205.59, 208.1,
#192.8, 180.27, 195.74, 201.17, 209.86, 201.87, 179.38, 167.11, 179.99, 208.07,
#212.23, 205.14, 201.21, 180.63, 176.36, 190.89, 206.73, 205.34, 188.07, 
#169.57, 176.18, 191.82, 194.07, 205.99, 204.98, 200.29, 190.52, 189.14, 
#194.65, 188.97, 198.19, 178.03, 182.65, 194.29, 196.0, 193.19, 194.43, 179.63,
#197.73, 204.24, 199.32, 209.48, 204.62, 193.44, 181.99, 196.02, 204.84, 209.4,
#194.12, 175.39, 194.88, 208.65, 205.94, 197.69, 184.47, 172.59, 183.86,
#199.14, 213.82, 206.46, 194.48, 175.3, 176.1, 194.91, 208.59, 209.01, 190.92,
#191.17, 175.59, 195.32, 206.8, 217.82, 212.64, 195.08, 180.13, 190.87, 203.0, 
#196.91, 189.42, 170.31, 170.07, 181.7, 187.96, 194.01, 207.64, 194.11, 192.11,
#202.95, 197.85])
#
#gev_fit = gev.fit(tides,0)
#
#x = np.linspace(np.min(tides)-10,np.max(tides)+10,1000)
#gev_pdf = gev.pdf(x, gev_fit[0], gev_fit[1], gev_fit[2])
#
#plt.subplot(1,2,1)
#plt.hist(tides, normed=True, alpha=0.2, label='Data')  
#plt.xlabel('Tides (cm)')
#
#plt.subplot(1,2,2)
#plt.hist(tides, normed=True, alpha=0.2, label='Data')
#plt.plot(x, gev_pdf, 'r--', label='GEV Fit')
#plt.xlabel('Tides (cm)')
#plt.legend(loc='upper left')
#plt.show()

import plotmyh5 as pmh


dfraw=pmh.test()

sr=dfraw[dfraw.columns[0]]
plt.figure()

gev_fit=gev.fit(sr)
x = np.linspace(np.min(sr),np.max(sr),200)
gev_pdf = gev.pdf(x, gev_fit[0], gev_fit[1], gev_fit[2])


plt.subplot(1,2,1)
plt.hist(sr,bins=20, normed=True, alpha=0.2, label='Data') 

plt.subplot(1,2,2)
plt.hist(sr, normed=True, alpha=0.2, label='Data')
plt.plot(x, gev_pdf, 'r--', label='GEV Fit')
plt.legend(loc='upper left')
plt.show()

#plt.hist(sr,bins=1000,density=True,histtype='step',cumulative=True)
#plt.hist(gev_pdf,bins=100,density=True,histtype='step',cumulative=True)



