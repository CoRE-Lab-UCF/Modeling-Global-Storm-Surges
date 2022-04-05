# -*- coding: utf-8 -*-
"""
Created on Mon Nov  2 08:57:41 2020

Get Annual RMSE

@author: Michael Tadesse
"""
from sklearn import metrics
import pandas as pd
import numpy as np
import os

#merge obs and recon  - name it dat
#change their respective dates before merging


dat = dfMerged.copy()
getYear = lambda x: x.year
dat['year'] = pd.DataFrame(list(map(getYear, dat['date'])))
dat = dat[['date', 'surge', 'surge_reconsturcted', 'year']]
# dat.columns = ['date', 'surge', 'year_x', 'Unnamed: 0', 'surge_reconsturcted',
#        'pred_int_lower', 'pred_int_upper', 'lon', 'lat', 'year']


#remove nans from dat
#find rows that have nans and remove them
row_nan = dat[dat.isna().any(axis =1)]
dat.drop(row_nan.index, axis = 0, inplace = True)
dat.reset_index(inplace = True)
dat.drop('index', axis = 1, inplace = True)

#get annual rmse
rmse = pd.DataFrame(columns=['year', 'value'])
years = dat['year'].unique()
for ii in years:
    currentYear = dat[dat['year'] == ii]
    rmseValue = np.sqrt(metrics.mean_squared_error(currentYear['surge_reconsturcted'], 
                                              currentYear['surge']))
    df = pd.DataFrame([ii, rmseValue]).T
    df.columns = ['year', 'value']
    rmse = pd.concat([rmse, df], axis = 0)
    print(rmse)


os.chdir("D:\\OneDrive - Knights - University of Central Florida\\UCF\\Projekt.28\\Report\\07-Fall-2020\\#3Paper\\data\\changePointTimeSeries\\era20CRMSE")
rmse.to_csv("bostonRMSE.csv")