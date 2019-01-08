#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov  7 17:01:59 2018

@author: xliang
"""

#import sys
import os
import h5py
import numpy as np
import pandas as pd
#os.getcwd()
#os.chdir("/home/xliang/examples/")


def namingit(a,b,c,d):
    if (d==0):
        nom="R%s_M%s_%s_ISO.h5"%(a,b,c)
    else:
        nom="R%s_M%s_%s_CUB_OR%s.h5"%(a,b,c,d)
    return nom

def mypath(a,b,c,d):
    morphodict={"V":"Voronoi","Q":"Quadrangle"}
    if (d==0):
        chemin="/Rough%s/%s/iso/"%(a,morphodict[b])
    else:
        chemin="/Rough%s/%s/ori%s/"%(a,morphodict[b],d)
    return chemin

def findmax(h5name,resultdict,totalframes=4):
    Result_dict=resultdict
    fo=h5py.File(h5name,'r')
    path1="Frames"
    path2="00000"+str(totalframes)
    path2=path2[-5:]
    path3="Elements"
    path4="Fatigue"

    resIndex=fo[path1][path2][path3][path4].keys()

    for k in resIndex:
        print(k)
        T=np.array(fo[path1][path2][path3][path4][k])
        valuemax=T.max()
        ####################
        if("_T_" in h5name):
            valuemax=valuemax*116.4/232.5
        elif("_F_" in h5name):
            valuemax=valuemax*116.4/225.625
        ####################
        
        print(valuemax)
        Result_dict[k]=valuemax
    fo.close()
    return Result_dict
               
def dataread():
    
    inputdir=os.getcwd()
    
    roughlist=list(range(1,11))
    morpholist=["V","Q"]
    loadlist=["F","T"]
    orilist=list(range(0,11))
    summary={}
    
    for i in roughlist:    
        for j in morpholist:    
            for k in loadlist:
                for l in orilist:
                    nom=namingit(i,j,k,l)
                    tgtpath=inputdir+mypath(i,j,k,l)
    
                    if (os.path.isdir(tgtpath)):
                        os.chdir(tgtpath)
                        if(os.path.isfile(nom)):    
                            print(tgtpath+nom)
                            resultdict={}
                            resultdict["Roughness"]=str(i)
                            resultdict["Morphology"]=j
                            resultdict["Loading"]=k
                            resultdict["Orientation"]=str(l)
                            summary[nom]=findmax(nom,resultdict)
                        else:
                            print("Not a file!")
                    else:
                        print("Wrong path!")
     
    df=pd.DataFrame.from_dict(summary,orient="index")
    
    os.chdir(inputdir)
    df.to_csv("summary.csv")
    return df

if __name__ == '__main__':
    dataread()
    
    pass
