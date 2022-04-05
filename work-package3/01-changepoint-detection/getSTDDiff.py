# -*- coding: utf-8 -*-
"""
Created on Fri Jan 22 13:31:33 2021

get STD difference time series
and apply changepoint detection method

@author: Michael Tadesse
"""

#read obsSTD and reconSTD csvs - name as obs and recon

# preprocess time series
obs.drop(['Unnamed: 0'], axis = 1, inplace = True)
recon.drop(['Unnamed: 0'], axis = 1, inplace = True)
obs.columns = ['year', 'obsSTD']
recon.columns = ['year', 'reconSTD']
stdMerge = pd.merge(obs, recon, on='year', how = "left")
stdMerge['diff'] = stdMerge['obsSTD'] - stdMerge['reconSTD']

#remove nans from dat
#find rows that have nans and remove them
row_nan = stdMerge[stdMerge.isna().any(axis =1)]
stdMerge.drop(row_nan.index, axis = 0, inplace = True)
stdMerge.reset_index(inplace = True)
stdMerge.drop('index', axis = 1, inplace = True)

#plot
plt.figure(figsize = (10,4))
plt.plot(obs['year'], obs['obsSTD'], label = "obsSTD", color = "blue")
plt.plot(recon['year'], recon['reconSTD'], label = "reconSTD", color = "red")
plt.plot(stdMerge['year'], stdMerge['diff'], label = "diff", color = "black")
plt.legend()

#save as csv
stdMerge.to_csv('stdDiff.csv')
