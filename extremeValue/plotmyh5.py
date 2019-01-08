#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov  9 12:33:06 2018

@author: xliang
"""
import pandas as pd
import readmyh5 as rh
import numpy as np
import matplotlib.pyplot as plt

#dfraw=rh.dataread()
dfraw=pd.read_csv("sum.csv",index_col=[0],dtype={'Orientation': object, 'Roughness': object})


dfraw=dfraw.drop(["HM_elt","Huyen-Morel"],axis=1)

#dfraw=dfraw.drop(['0.013DV NonLocal','0.050DV NonLocal','0.100DV NonLocal','DV_elt',"HM_elt","Huyen-Morel",'0.013Pap NonLocal','0.050Pap NonLocal','0.100Pap NonLocal','Pap_elt','PAPADOPOULOS','0.013Matake NonLocal','0.050Matake NonLocal','0.100Matake NonLocal','Matake_elt','MATAKE'],axis=1)



def rearrange_dataframe_single(df,critere):
    if(critere=="D"):
        df=df[['0.013DV NonLocal','0.050DV NonLocal','0.100DV NonLocal','DV_elt','DV']]
    elif(critere=="M"):
        df=df[['0.013Matake NonLocal','0.050Matake NonLocal','0.100Matake NonLocal','Matake_elt','MATAKE']]    
    elif(critere=="P"):
        df=df[['0.013Pap NonLocal','0.050Pap NonLocal','0.100Pap NonLocal','Pap_elt','PAPADOPOULOS']]
    else:
        print("wrong criterion")    
    return df

def normlizethestress(df):
    
    df=df.transform(lambda s:116.4/s*73.84)
    
    return df


def fcertain(sr):
    t=sr.dtype
    if(t=="float64"):
        sr=sr.iloc[0]/sr
        return sr
    else:
        return sr
def comparesmooth(df):
    dgroup=df.groupby((['Morphology','Loading','Orientation']))
    df=dgroup.transform(fcertain)
    return df


def rearrange_dataframe_plural(df,critere):
    col=list(df.columns)
    thelist=[]
    if(critere=="D"):
        thelist=thelist+[val for val in col if val[0]=="0.013DV NonLocal"]
        thelist=thelist+[val for val in col if val[0]=="0.050DV NonLocal"]
        thelist=thelist+[val for val in col if val[0]=="0.100DV NonLocal"]        
        thelist=thelist+[val for val in col if val[0]=="DV_elt"] 
        thelist=thelist+[val for val in col if val[0]=="DV"] 
    elif(critere=="M"):
        thelist=thelist+[val for val in col if val[0]=="0.013Matake NonLocal"]
        thelist=thelist+[val for val in col if val[0]=="0.050Matake NonLocal"]
        thelist=thelist+[val for val in col if val[0]=="0.100Matake NonLocal"]        
        thelist=thelist+[val for val in col if val[0]=="Matake_elt"] 
        thelist=thelist+[val for val in col if val[0]=="MATAKE"]
    elif(critere=="P"):
        thelist=thelist+[val for val in col if val[0]=="0.013Pap NonLocal"]
        thelist=thelist+[val for val in col if val[0]=="0.050Pap NonLocal"]
        thelist=thelist+[val for val in col if val[0]=="0.100Pap NonLocal"]        
        thelist=thelist+[val for val in col if val[0]=="Pap_elt"] 
        thelist=thelist+[val for val in col if val[0]=="PAPADOPOULOS"]
    else:
        print("wrong criterion")    
    return df[thelist]



def orientation_list_generator(atype):
    if (atype=="homo"):
        homogenerous_orientation_list=['0']
        return homogenerous_orientation_list
    elif(atype=='iso'):
        isotropic_orientation_list=[str(i) for i in range(1,6) ]+[str(i) for i in range(11,56) ]
        return isotropic_orientation_list
    elif(atype=='real'):
        realistic_orientation_list=[str(i) for i in range(6,11) ]+[str(i) for i in range(56,101) ]
        return realistic_orientation_list
    elif(atype=='all'):
        return [str(i) for i in range(0,101)]
    else:
        print("wrong type")
    pass
      
def ori_lookup(sr):
    homo=orientation_list_generator("homo")
    iso=orientation_list_generator("iso")
    real=orientation_list_generator("real")
    thelist=[]
    for i in sr:
        if (i in homo):
            thelist.append('homo')
        elif(i in iso):
            thelist.append('iso')
        elif(i in real):
            thelist.append('real')
        else:
            print("Wrong ORI",i)
    return thelist
            
def set_ori(dfraw):
    dfraw=dfraw.assign(OriType=ori_lookup(dfraw.Orientation))
    dfraw=dfraw.drop(['Orientation'],axis=1)
    return dfraw


def morphology_list_generator(atype):
    if(atype=='v'):
        voronoi_list=['V']
        return voronoi_list
    elif(atype=='q'):
        quadrangle_list=['Q']
        return quadrangle_list
    elif(atype=='all'):
        return ['Q','V']
    else:
        print("wrong type")
    pass

def loading_list_generator(atype):
    if(atype=='t'):
        tension_list=['T']
        return tension_list
    elif(atype=='f'):
        flexion_list=['F']
        return flexion_list
    elif(atype=='all'):
        return ['T','F']
    else:
        print("wrong type")
    pass

def roughness_list_generator(*numbers):
    roughness_list=[str(i) for i in numbers]
    return roughness_list

def slicemydataframe(df,roughness=[1],morphology='all',loading='all',orientation='all'):
    '''
    a complicated method as an alternative of groupby...
    '''
    dfnew=df[(df['Roughness'].isin(roughness_list_generator(*roughness))) &
             (df['Morphology'].isin(morphology_list_generator(morphology))) & 
             (df['Loading'].isin(loading_list_generator(loading))) &
             (df['Orientation'].isin(orientation_list_generator(orientation)))]
    return dfnew

def drawmyfigure(df,name="ex"):
    
    #df=df.fillna(150.0)
    
    n=df.columns.size
    bins=df.index.size
    
    if (n==3):
        fig, ax1 = plt.subplots(2,2,figsize=(12,12))
#        axes1=df.hist(bins=bins,
#                      density=True,
#                      histtype='step',
#                      cumulative=True,
#                      ax=[ax1[0,0],ax1[0,1],ax1[1,0]])
#        axes2=df.plot.kde(ax=ax1[1,1])
        
    elif(n==5):
        fig, ax1 = plt.subplots(2,3,figsize=(18,12))
    temp=ax1.flatten()
    axes1=df.hist(grid=False,
                  bins=bins,
                  density=True, 
                  histtype='step',
                  cumulative=True,
                  ax=temp[0:-1:1])
    axes2=df.plot.kde(ax=temp[-1],grid=True)

    for i in axes1:
        i.set_xlabel("Fatigue Limit (MPa)")
        i.set_ylabel("Probability")
  
    axes2.set_xlabel("Fatigue Limit (MPa)")
    
    import seaborn as sns
    counter=0
    for i in df.columns:
        sns.kdeplot(df[i],cumulative=True,ax=temp[counter],legend=False)
        counter+=1
    fig.savefig(name+".png")
    pass

def drawmyfigure_mod(df,name="ex"):
    
    #df=df.fillna(150.0)
    
    n=df.columns.size
    bins=df.index.size
    
    if (n==3):
        fig, ax1 = plt.subplots(2,2,figsize=(12,12))
#        axes1=df.hist(bins=bins,
#                      density=True,
#                      histtype='step',
#                      cumulative=True,
#                      ax=[ax1[0,0],ax1[0,1],ax1[1,0]])
#        axes2=df.plot.kde(ax=ax1[1,1])
        
    elif(n==5):
        fig, ax1 = plt.subplots(2,3,figsize=(18,12))
    temp=ax1.flatten()
#    axes1=df.hist(grid=False,
#                  bins=bins,
#                  density=True, 
#                  histtype='step',
#                  cumulative=True,
#                  ax=temp[0:-1:1])
#    axes2=df.plot.kde(ax=temp[-1],grid=True)
#
#    for i in axes1:
#        i.set_xlabel("Fatigue Limit (MPa)")
#        i.set_ylabel("Probability")
#  
#    axes2.set_xlabel("Fatigue Limit (MPa)")
#    
    import seaborn as sns
    counter=0
    for i in df.columns:
        sns.distplot(df[i],norm_hist=True,kde=False,ax=temp[counter],hist_kws=dict(cumulative=True))
        axes1=sns.kdeplot(df[i],cumulative=True,ax=temp[counter],legend=False)
        counter+=1
    
    
    axes2=df.plot.kde(ax=temp[-1],grid=True)
    for i in axes1:
        i.set_xlabel("Fatigue Limit (MPa)")
        i.set_ylabel("Probability")
  
    axes2.set_xlabel("Fatigue Limit (MPa)")
    fig.savefig(name+".png")
    pass

def drawmyfigure2(df,name="ex"):
    
    #df=df.fillna(150.0)
    
    n=df.columns.size
    bins=df.index.size
    
    if (n==3):
        fig, ax1 = plt.subplots(2,2,figsize=(12,12))
#        axes1=df.hist(bins=bins,
#                      density=True,
#                      histtype='step',
#                      cumulative=True,
#                      ax=[ax1[0,0],ax1[0,1],ax1[1,0]])
#        axes2=df.plot.kde(ax=ax1[1,1])
        
    elif(n==5):
        fig, ax1 = plt.subplots(2,3,figsize=(18,12))
    temp=ax1.flatten()
    axes1=df.hist(grid=False,
                  bins=bins,
                  density=True, 
                  histtype='bar',
                  
                  ax=temp[0:-1:1])
    axes2=df.plot.kde(ax=temp[-1],grid=True)

    for i in axes1:
        i.set_xlabel("Normlized Fatigue Limit")
        i.set_ylabel("Probability")
  
    axes2.set_xlabel("Normlized Fatigue Limit")
    
    import seaborn as sns
    counter=0
    for i in df.columns:
        sns.kdeplot(df[i],ax=temp[counter],legend=False)
        counter+=1
    fig.savefig(name+".png")
    pass





def test():
    rlist=list(range(1,61))   
    
    
    a=slicemydataframe(dfraw,
                       roughness=rlist,
                       morphology='all',
                       loading='f',
                       orientation='homo')
    b=set_ori(a)
    c=b.groupby((['Roughness','Morphology','Loading','OriType']))
    ckey=[key for key,df in c]
    d=c.agg(np.mean)
    e=rearrange_dataframe_single(b,'D')
    #d=c.agg([np.mean,np.max,np.min])
    #e=rearrange_dataframe_plural(d,'D')
    e.to_csv("check.csv")
    f1=e.drop(["DV_elt","DV"],axis=1)
    f1=normlizethestress(f1)
    
    name="test"
    #drawmyfigure(f1,name)
    
    
    #f1.plot.bar()
    #f1.hist(density=True, histtype='step',cumulative=True)
#    a=slicemydataframe(dfraw,
#                       roughness=[1,2,3,4,5],
#                       morphology='all',
#                       loading='t',
#                       orientation='real')
#    b=set_ori(a)
#    c=b.groupby((['Roughness','Morphology','Loading','OriType']))
#    ckey=[key for key,df in c]
#    d=c.agg(np.mean)
#    e=rearrange_dataframe_single(d,'D')
#    #d=c.agg([np.mean,np.max,np.min])
#    #e=rearrange_dataframe_plural(d,'D')
#    e.to_csv("check.csv")
#    f2=e.drop(["DV_elt","DV"],axis=1)
#    
#    
#    aaa=pd.concat([f1,f2])
#    figure=aaa.plot.bar()
    
#    
#    fig = figure.get_figure()
#    fig.savefig('fig.png')
    
    #plt.figure(1,figsize=(8,8))
    
  #  fig, ax1 = plt.subplots(2,2,figsize=(12,12))    
    # plot the cumulative histogram
  #  axes1=f1.hist(bins=1000,density=True, histtype='step',cumulative=True,ax=[ax1[0,0],ax1[0,1],ax1[1,0]])
   
    
    
    
    
#    fig2,ax2=plt.subplots(figsize=(3,3))
#    axes2=f1.plot.kde(ax=ax2)
    # Overlay a reversed cumulative histogram.
    #ax.hist(x, bins=bins, density=True, histtype='step', cumulative=-1,label='Reversed emp.')
    
    
    #aaa=fig.add_subplot(224)
    
    #print(aaa.axis('off'))
   # axes2=f1.plot.kde(ax=ax1[1,1])

    #aaa.autoscale()
    #print(aaa.axis())
    
    
  #  fig.savefig("ex.png")
    
    return f1




    

if __name__ =='__main__':

    rlist=list(range(1,61))   
    
    
    a=slicemydataframe(dfraw,
                       roughness=rlist,
                       morphology='all',
                       loading='t',
                       orientation='homo')
    b=set_ori(a)
    c=b.groupby((['Roughness','Morphology','Loading','OriType']))
    ckey=[key for key,df in c]
    d=c.agg(np.mean)
    e=rearrange_dataframe_single(b,'D')
    #d=c.agg([np.mean,np.max,np.min])
    #e=rearrange_dataframe_plural(d,'D')
    e.to_csv("check.csv")
    f1=e.drop(["DV_elt","DV"],axis=1)
    f1=normlizethestress(f1)
    
    
#    
#    bb=comparesmooth(a)
#    ee=rearrange_dataframe_single(bb,'D')
#    f1=ee.drop(["DV_elt","DV"],axis=1)

    
    name="test"
    drawmyfigure(f1,name)
    
    
    #f1.hist(density=True,bins=30)
    
    
    
    import gevmyh5
    
    gevmyh5.gevfitdf(f1)
    
    
    pass





    
    
    
    
    
    
    
    
    
    
    