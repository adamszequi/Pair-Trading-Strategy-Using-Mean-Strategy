# -*- coding: utf-8 -*-
"""
Created on Wed Jan 29 12:40:31 2020

@author: Dell
"""


'''
pair trading—mean reversion is based on the
correlation between two instruments. If a pair of stocks already has a high
correlation and, at some point, the correlation is diminished, it will come back to
the original level (correlation mean value). If the stock with the lower price
drops, we can long this stock and short the other stock of this pair.
'''
import pandas as pd
import scipy as sp 
import numpy as np
from statsmodels.tsa.statstools import  coint


def getdata(ticker):
    for _ in ticker:
        datalist=[]
        data=pd.read_pickle(r'C:\Users\Dell\Desktop\data\yanMonthly (2).pkl')
        x=data[data.index==_]
        datalist.append(x)
    return datalist
       
def findCointegratedPairs(ticker):
    data=getdata(ticker)
    dataShape=data.shape[1]#find shape of the data
    pvalueMatrix=np.ones((dataShape,dataShape))#create matrix of shape of data
    keys=data.keys()
    pairs=[]
    for i in range(dataShape):
        for j in range(i+1,dataShape):
            result=coint(data[keys[i]],data[keys[j]])#coint function
            pvalueMatrix[i,j]=result[1]
            if result[1]<0.02:
               pairs.append(keys[i],keys[j])
    return pvalueMatrix,pairs          
            
symbolsIds = ['SPY','AAPL','ADBE','LUV','MSFT','SKYW','QCOM',\
             'HPQ','JNPR','AMD','IBM']   

print(getdata(symbolsIds))  
     
    
    
    
    
