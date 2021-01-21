# -*- coding: utf-8 -*-
"""
Created on Tue Aug 11 17:00:10 2020

Plot window correlation and rmse for 
surge reconstruction


@author: Michael Tadesse
"""
import numpy as np
import pandas as pd
from scipy import stats
from sklearn import metrics

years = dat['year'].unique()
data = pd.DataFrame(columns = ['year','maCorr', 'maRmse'])

window = 30
for yr in years:
    currentStartYear = yr - window + 1
    currentData = dat[(dat['year'] >= currentStartYear) & (dat['year'] <= yr)]
    corr = stats.pearsonr(currentData['surge_reconsturcted'], currentData['surge'])[0]
    rmse = np.sqrt(metrics.mean_squared_error(currentData['surge_reconsturcted'], currentData['surge']))
    currentMetrics = pd.DataFrame([yr, corr, rmse]).T
    currentMetrics.columns = ['year','maCorr', 'maRmse']
    data = pd.concat([data, currentMetrics], axis = 0)