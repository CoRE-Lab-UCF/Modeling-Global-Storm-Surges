# -*- coding: utf-8 -*-
"""
Created on Thu Jul 30 15:28:20 2020

Moving average trend analysis

@author: Michael Tadesse
"""
from sklearn import metrics
from scipy import stats
import pandas as pd
import numpy as np

#load files from the following folder
#cd to main folder
os.chdir('G:\\data\\reanalysisTrendFiles\\reconSurgeFiles')





#adjust surge time format to match that of pred
time_str = lambda x: str(datetime.strptime(x, '%Y-%m-%d'))
surge_time = pd.DataFrame(list(map(time_str, vicSurge['ymd'])), columns = ['date'])
time_stamp = lambda x: (datetime.strptime(x, '%Y-%m-%d %H:%M:%S'))
vicSurge = pd.concat([surge_time, vicSurge[['surge', 'lon', 'lat']]], axis = 1)


#merge files
vicMergedEra20c = pd.merge(vicEra20c, vicSurge.iloc[:,:2], on='date', how='right')
vicMergedEra20c.sort_values(by = 'date', inplace = True)
vicMergedEra20c.reset_index(inplace=True)


#get the year
getYear = lambda x: x.split('-')[0]
vicMergedEra20c['year'] = pd.DataFrame(list(map(getYear, vicMergedEra20c['date'])))

vicMergedEra20c.to_csv('victoriaEra20cMerged.csv')


#get yearly metric values
dat = pd.read_csv('victoriaEra20cMerged.csv')
dat = dat[~dat.isna().any(axis = 1)]
years = dat.year.unique().tolist()

metric = pd.DataFrame(columns = ['year', 'corr', 'rmse', 'nse'])

for year in years:
    blockYear = dat[dat['year'] == year];
    #print(blockYear, '\n')
    metricCorr = stats.pearsonr(blockYear['surge_reconsturcted'], 
                                blockYear['surge'])[0]
    metricRmse = np.sqrt(metrics.mean_squared_error(
        blockYear['surge_reconsturcted'], blockYear['surge']))
    metricNSE = getNSE(blockYear)
    
    currentMetric = [year, metricCorr, metricRmse, metricNSE]
    print(year, " - ", metricCorr, metricRmse, metricNSE)
    
    metric.loc[len(metric)] = currentMetric
    
    
#to get moving average 
twcrBrest['ma10Corr'] = twcrBrest['corr'].rolling(10).mean()

sns.set_context('notebook', font_scale = 1.5)

plt.figure()
plt.plot(twcrBrest['year'], twcrBrest['ma10Rmse'])
plt.title('Brest - 10 year moving average - RMSE')


def getNSE(surgeMerged):
    """
    this function computes the Nash-Sutcliffe
    Efficiency (NSE)
    """
    if surgeMerged.empty:
        print("no common period")
        metricNSE = 'nan'
    else:
        numerator = sum((surgeMerged['surge_reconsturcted'] - surgeMerged['surge'])**2)
        denominator = sum((surgeMerged['surge'] - surgeMerged['surge'].mean())**2)
        metricNSE = 1 - (numerator/denominator)

    return metricNSE
    
    