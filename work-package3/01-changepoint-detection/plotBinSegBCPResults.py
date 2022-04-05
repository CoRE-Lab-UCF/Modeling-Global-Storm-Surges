# -*- coding: utf-8 -*-
"""
Created on Mon Nov  9 17:14:11 2020

@author: Michael Tadesse 
"""
import os 
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt 


#for BinSeg results - add the mean RMSE on
#additional column 
#manually or proramatically 

#read the rmse time series - name it dat

#for BCP results change column names
dat.columns = ['Unnamed: 0', 'year', 'postMean', 'prob']


#create an empty year column
year = pd.DataFrame(np.arange(1900,2011))  
year.columns = ['year']

#merge RMSE or BinSeg or BCP dataframe with empty year
df = pd.merge(year, dat, on="year", how="left")

#plotting binary segmentation result
plt.figure(figsize = (10, 4))
plt.plot(df['year'], df['value'], color = "black")
plt.plot(df['year'], df['mean'], color = "red", label = "RMSE mean", lw = 4)
plt.ylabel("RMSE")
plt.legend()

#plotting BCP results
#posterior mean plot
plt.figure(figsize = (10, 4))
plt.plot(df['year'], df['postMean'], color = "brown")
plt.ylabel("Posterior Mean RMSE (m)")
#plt.ylim(0.14,0.19)
plt.legend()

#probability plot
plt.figure(figsize = (10, 4))
plt.plot(df['year'], df['prob'], color = "black")
plt.ylabel("Changepoint Probability")
plt.ylim(0,1)
plt.legend()