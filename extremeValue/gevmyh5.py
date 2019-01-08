#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Dec 13 15:33:09 2018

@author: xliang
"""

import numpy as np
import matplotlib.pyplot as plt 
from scipy.stats import genextreme as gev
import pandas as pd

def gevfit(sr):
    gev_fit=gev.fit(sr)
    c=gev_fit[0]
    mu=gev_fit[1]
    sigma=gev_fit[2]
    
    print("""
          GEV Fit Parameters:
          shape parameter c: %s
          location parameter mu: %s
          scale parameter sigma: %s
          """%(c,sigma,mu)
    )
        
    print( "Median",gev.median(c,mu,sigma)  )  
    print( "Mean",gev.mean(c,mu,sigma)    )
    print( "Std dev",gev.std(c,mu,sigma))
    print( "95% interval: ",gev.interval(0.95,c,mu,sigma))
    
    if (c>0):
        lBnd=mu-sigma/c
    else:
        lBnd=mu+sigma/c
    srmax=np.max(sr)*1.1
    
    bins=sr.size
    
    x = np.linspace(np.min(sr)-5,np.max(sr)+5,500)
    #x=np.linspace(lBnd,srmax,500)
    gev_pdf = gev.pdf(x, c, mu, sigma)
    gev_cdf = gev.cdf(x,c,mu,sigma)
    
   
    
    plt.figure(figsize=(12,6))
    
    ax1=plt.subplot(1,2,1)
    plt.hist(sr, normed=True, alpha=0.2, label='Raw Data',bins='auto' )
    plt.plot(x, gev_pdf, 'r--', label='GEV Fit')
    plt.legend(loc='upper left')
    ax1.set_title('%s_Probability Density Fraction'%(sr.name))
    ax1.set_xlabel('Predicted Fatigue Limit (MPa)')
    ax1.set_ylabel('Probability')
    ax1.grid()
    
    ax2=plt.subplot(1,2,2)
    plt.hist(sr, normed=True, alpha=0.2, label='Raw Data',cumulative=True,bins='auto')
    plt.plot(x, gev_cdf, 'r--', label='GEV Fit')
    plt.legend(loc='upper left')
    ax2.set_title('%s_Cumulative Density Fraction'%(sr.name))
    ax2.set_xlabel('Predicted Fatigue Limit (MPa)')
    ax2.set_ylabel('Density')
    ax2.grid()
    
    plt.show()
    pass
    
def gevfitdf(df):
    for i in df.columns:
        gevfit(df[i])
    pass