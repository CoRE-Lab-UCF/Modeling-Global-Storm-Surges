# -*- coding: utf-8 -*-
"""
Created on Mon Nov 18 15:24:13 2019
Lag time series - to consider autocorrelation
@author: mi292519
"""
import pandas as pd
import datetime

def time_lag(data, lags):
    """
    Transforms the dataset to  a time series of grid information 
    and spits back the time lagged time series
    data - the full name of the csv file
    """
    time_original = pd.to_datetime('1900-01-01')

    dat = pd.read_csv(data)
    dat.columns = ['time', 'u10', 'v10', 'slp', 'weight', 'surge'] 
    
    #reorganize the matrix
    dat_new = dat.loc[dat['weight'] == dat['weight'].unique()[0]]
    dat_new.drop(['weight'], axis = 1, inplace=True) #, 'surge'
    
    for ii in range(1,10):
        dat_sub = dat.loc[dat['weight'] == dat['weight'].unique()[ii]]
        dat_sub.drop(['weight', 'surge'], axis = 1, inplace=True)
        dat_new = pd.merge(dat_new, dat_sub, on='time')
    
    
    #lag the time series
    lagged = dat_new.copy() #to prevent modifying original matrix
    for jj in range(lags):
        #lagged.drop(jj, axis = 0, inplace = True)
        lagged['time'] = lagged['time'] + 6
        #remove the last row since there is no match for it in dat_new
        lagged.drop(lagged.tail(1).index.item(), axis = 0, inplace = True)
        #remove the topmost row from dat_new to match lagged
        dat_new.drop(dat_new.head(1).index.item(), axis = 0, inplace = True)
        #merge lagged and dat_new
        dat_new = pd.merge(dat_new, lagged, on = 'time', how = 'outer', \
                       suffixes = ('_left', '_right'))
    dat_new = dat_new.T.reset_index(drop=True).T
    ind = dat_new.loc[pd.isna(dat_new[dat_new.shape[1]-1]), :].index
    dat_new.drop(ind,inplace=True)
    
    
    #surge time series
    surge_ts = pd.DataFrame(dat.loc[dat['weight'] == \
                                dat['weight'].unique()[0]][['time', 'surge']])
    #remove nan values
    surge_ts.reset_index(inplace=True) #reset index for subsetting isnans
    surge_ts.drop(['index'], axis = 1, inplace=True)    
    indx = surge_ts.loc[pd.isna(surge_ts["surge"]), :].index
    dat_new.drop(indx,inplace=True)
    surge_ts.drop(indx,inplace=True)
    #filter surge accoring to dat_new
    lagged_time = list(dat_new[0])
    time_dat_new = [float(x) for x in dat_new[0]]
    time_surge_ts = [float(x) for x in surge_ts['time']]
    time_both = []
    for kk in lagged_time:
        if ((kk in time_dat_new) & (kk in time_surge_ts)):
            time_both.append(int(kk))
            
    surge_ts = surge_ts[surge_ts['time'].isin(time_both)]
    
    dt = pd.DataFrame(columns = ['date']);
    for ii in surge_ts.index:
        dt.loc[ii, 'date'] = time_original + \
            datetime.timedelta(hours = int(surge_ts.loc[ii, 'time']))
            
    surge_ts['date'] = dt
    dat_new = dat_new[dat_new[0].isin([x*1.0 for x in time_both])]
    dat_new.drop(4, axis = 1, inplace = True) #remove the un-lagged surge 
    return dat_new, surge_ts


