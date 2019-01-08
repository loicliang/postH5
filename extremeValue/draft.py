#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov 14 13:02:33 2018

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

def findmax(h5name,totalframes=4):
    Result_dict={}
    fo=h5py.File(h5name,'r')
    path1="Frames"
    path2="00000"+str(totalframes)
    path2=path2[-5:]
    path3="Elements"
    path4="Fatigue"

    resIndex=fo[path1][path2][path3][path4].keys()

    for k in resIndex:
        #print(k)
        T=np.array(fo[path1][path2][path3][path4][k])
        valuemax=T.max()
        #print(valuemax)
        Result_dict[k]=valuemax
    fo.close()
    return Result_dict
               
def dataread():
    
    inputdir=os.getcwd()
    
    roughlist=list(range(1,2))
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
    
                            summary[nom]=findmax(nom)
                        else:
                            print("Not a file!")
                    else:
                        print("Wrong path!")
     
    df=pd.DataFrame.from_dict(summary,orient="index")
    
    os.chdir(inputdir)
    df.to_csv("summary.csv")
    
    return df
dfraw=dataread()

dfraw=dfraw.drop(["HM_elt","Huyen-Morel"],axis=1)
print(dfraw)

dfraw.index = pd.MultiIndex.from_tuples([str(c[:-3]).split("_") for c in dfraw.index],
                                         names=["roughness",
                                                "morpholopy",
                                                "loading",
                                                "constitution",
                                                "orientation"])

def extrait_dataframe(df,roughness,morphology,loading,constitution,orientation):
    '''
    roughness is an integer ranged(1-10)
    morphology is a string with the content of "Q" or "V"
    loading is "T" or "F"
    constitution is "ISO" or "CUB"
    orientation is an integer ranged(1-10)
    '''
    mdict={"q":"MQ","Q":"MQ","v":"MV","V":"MV"}
    ldict={"f":"F","F":"F","t":"T","T":"T"}
    cdict={"iso":"ISO","cub":"CUB","ISO":"ISO","CUB":"CUB"}
    
    rDF="R"+str(roughness)
    mDF=mdict[morphology]
    lDF=ldict[loading]
    cDF=cdict[constitution]
    isoflag=False
    
    if (cDF=="CUB"):
        oDF="OR"+str(orientation)
    else:
        isoflag=True
    
    if(isoflag):
        dfnew=df.xs((rDF,mDF,lDF,cDF),
                    level=["roughness","morpholopy","loading","constitution"])
        dfnew
    else:
        dfnew=df.xs((rDF,mDF,lDF,cDF,oDF),
                    level=["roughness","morpholopy","loading","constitution","orientation"])
    
    return dfnew

def sort_dataframe(df,orilabel):
    pass

        
def alliso_dataframe(df):
    newdf=[]
    roughrange=list(range(1,2))
    for i in roughrange:
        newdf.append(extrait_dataframe(df,i,'v','f','iso',0))
        newdf.append(extrait_dataframe(df,i,'v','t','iso',0))
        newdf.append(extrait_dataframe(df,i,'q','f','iso',0))
        newdf.append(extrait_dataframe(df,i,'q','t','iso',0))
    newdf=pd.concat(newdf)
    return newdf





#
#
#[c for c in df.index]
#[c for c in dfraw.index]
#a=[c for c in dfraw.index]
#a=[c[:-3] for c in dfraw.index]
#a=[str(c[:-3]) for c in dfraw.index]
#a=[str(c[:-3]).split("_") for c in dfraw.index]
##mindex=dfraw.index
#aa=dfraw.xs("OR10",level="orientation")
#dfnew=dfraw.xs(key="ISO",axis=0,level=3)
#a=[]
#a.append(dfnew)

b=dfraw["Roughness"]
b=dfraw.Roughness
a=dfraw[(dfraw['Morphology']=="Q") & (dfraw['Loading']=='T')]
a=dfraw[(dfraw['Morphology'].isin(['Q'])) & (dfraw['Loading'].isin(['T']))]





#201811151440
def mydefinefunc(sr):
#    keys=df.keys()
#    types=df.dtypes()
#    for (key,typ) in (keys,types):
#        if typ=='float64':
#            a=df[key].mean()
#        else:
#            a="N/A"
#    return a
    t=sr.dtype
    if(t=='float64'):
        r=sr.mean()
    else:
        r="N/A"
    return r

h=dfg.agg(mydefinefunc)

def merge_orientation_set(dfraw):
    dffinal=[]
    dfg=dfraw.groupby(['Roughness','Morphology','Loading'])
    
    for key,adataframe in dfg:
        df=dfg.getgroup(key)
        
        A=df[df['Orientation'].isin(orientation_list_generator('real'))]   
        B=df[df['Orientation'].isin(orientation_list_generator('iso'))] 
        C=df[df['Orientation'].isin(orientation_list_generator('homo'))] 
        
#        A=A.mean()
#        B=B.mean()
#        C=C.mean()
        df.loc["homo"]=df.apply()
        
        
        dfnew=pd.concat([A,B,C])
    dffinal.append(dfnew)
    dffinal=pd.concat(dffinal)
    return dffinal 



    #a=rearrange_dataframe(a,'D')
    #gg=dfraw.groupby(['Roughness','Morphology','Loading'])
    #a=[key for key,df in gg]



ee=d.columns
ee=d.columns.name
ee=d.columns.names
e=[c for c in d]
ee=d.columns
list(ee)
ee=list(ee)
gg=[e for e in c for c in ee]
gg=[c for c in ee if c[0]=="DV"]


def rearrange_dataframe(df,critere):
    if(critere=="D"):
        df=df[['0.013DV NonLocal','0.050DV NonLocal','0.100DV NonLocal','DV_elt','DV']]
    elif(critere=="M"):
        df=df[['0.013Matake NonLocal','0.050Matake NonLocal','0.100Matake NonLocal','Matake_elt','MATAKE']]    
    elif(critere=="P"):
        df=df[['0.013Pap NonLocal','0.050Pap NonLocal','0.100Pap NonLocal','Pap_elt','PAPADOPOULOS']]
    else:
        print("wrong criterion")    
    return df


