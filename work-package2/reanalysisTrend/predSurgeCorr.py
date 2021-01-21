# -*- coding: utf-8 -*-
"""
Created on Fri Sep  4 17:38:13 2020

@author: WahlInstall
"""


slpSurge.to_csv('atlSlpSurge.csv')

dat = slpSurge.copy()

dat['year'] = pd.DataFrame(list(map(getYear, dat['ymd'])))

years = dat.year.unique().tolist()

metric = pd.DataFrame(columns = ['year', 'corr'])

dat = dat[~dat.isna().any(axis = 1)]

for year in years:
    print(year)
    blockYear = dat[dat['year'] == year];
    #print(blockDay, '\n')
    
    corrn = stats.pearsonr(blockYear['0'], 
                                blockYear['surge'])[0]
    currentMetric = [year, corrn]
    #print(dailyMin)
    
    metric.loc[len(metric)] = currentMetric