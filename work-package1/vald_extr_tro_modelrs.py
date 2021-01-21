# -*- coding: utf-8 -*-
"""
Created on Thu Feb 27 16:34:10 2020
Supplementary Section Plot - ET and TR validation
@author: mi292519
"""
import matplotlib.pyplot as plt
import matplotlib.lines as mlines
import seaborn as sns
import pandas as pd
import numpy as np
import os
#browse to comment5 folder
dat = pd.read_csv('model_ar.csv', header=None)
dat.drop('Unnamed: 0', axis = 1, inplace = True)
dat.columns = ['lon', 'lat', 'corr', 'pval', 'rmse', 'rel_rmse', 'nse', 'model']

dat['model'].replace(1, 'lrrs', inplace = True)
dat['model'].replace(2, 'lrrslag', inplace = True)
dat['model'].replace(3, 'rfrslag', inplace = True)

def region(lat):
    """
    To classify a coordinate as extratropical/tropical
    """
    if (lat >=-30) and (lat<=30):
        return 'tr'
    elif ((lat >=-60) and (lat<-30)) or ((lat>30) and (lat<=60)):
        return 'et'
    else:
        return 'N/A'
    
dat['region'] = [region(x) for x in dat['lat']]

dat_et = dat.loc[dat['region'] == 'et']
dat_tr = dat.loc[dat['region'] == 'tr']


#melting dataframe for boxplot
mdf_et = pd.melt(dat_et, id_vars=['model'], value_vars=['corr', 'rmse', 'nse'])
mdf_tr = pd.melt(dat_tr, id_vars=['model'], value_vars=['corr', 'rmse', 'nse'])


#plotting
sns.set_context('notebook', font_scale=3)

plt.figure(figsize=(14,10))
sns.boxplot(x = 'model', y ='value', hue = 'variable',  \
            data = mdf_et, palette="husl")
plt.ylabel('Correlation/RMSE/NSE')
plt.xlabel('')
plt.legend('')


plt.figure(figsize=(14,10))
sns.boxplot(x = 'model', y ='value', hue = 'variable',  \
            data = mdf_tr, palette="husl")
plt.ylabel('Correlation/RMSE/NSE')
plt.xlabel('')
plt.legend(loc = 'lower left', ncol = 3)
