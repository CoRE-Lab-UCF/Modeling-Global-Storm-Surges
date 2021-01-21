# -*- coding: utf-8 -*-
"""
Created on Tue Mar 31 17:12:23 2020
Load predictors & predictands + predictor importance
@author: Michael Tadesse
"""

import os 
import pandas as pd
import datetime as dt #used for timedelta
from datetime import datetime

dir_in = 'F:\eraint_D5'
dir_out = 'F:\eraint_combined_predictors'

#load predictors
#load corresponding surge time series
os.chdir('F:\\dmax_surge')
surge = pd.read_csv('abashiri-japan-jma.csv')

os.chdir('F:\\eraint_combined_predictors')
pred = pd.read_csv('abashiri-japan-jma.csv')

"""
check redundancy of surge timeseries
some tide gauges have more than one daily max surge
"""
duplicate = surge.duplicated(subset='ymd', keep='first')
surge = surge[~duplicate]


#in some cases the surge ts might start earlier than pred ts
#use the join function to filter the overlapping period

surge_time = pd.DataFrame(surge['ymd'])
surge_time.columns = ['date']


 


#need to change the string format of dates to datetime
#these will be the time lagging dataframes
time_str = lambda x: str(datetime.strptime(x, '%Y-%m-%d'))
time_stamp = lambda x: datetime.strptime(x, '%Y-%m-%d')
time_converted_str = pd.DataFrame(map(time_str, surge_time['date']), columns = ['date'])
time_converted_stamp = pd.DataFrame(map(time_stamp, surge_time['date']), columns = ['timestamp'])

#prepare lagged time series for time only
time_lagged = pd.DataFrame()
lag_hrs = [0, 6, 12, 18, 24, 30]
for lag in lag_hrs:
    lag_name = 'lag'+str(lag)
    lam_delta = lambda x: str(x - dt.timedelta(hours = lag))
    lag_new = pd.DataFrame(map(lam_delta, time_converted_stamp['timestamp']), \
                           columns = [lag_name])
    time_lagged = pd.concat([time_lagged, lag_new], axis = 1)
    
#datafrmae that contains all lagged time series  (just time)
time_all = pd.concat([time_converted_str, time_lagged], axis = 1)



#find overlapping period for surge and predictors
pred_subset = pd.merge(pred, time_all['date'], on = ['date'], how = 'right')
pred_subset.sort_values(by = 'date', inplace=True)


#remove rows that have nans
is_nan = pred_subset.isnull()
row_has_nan = is_nan.any(axis = 1)
pred_subset_wo_nans = pred_subset[~row_has_nan]

"""
#but how can I subset pred based on the surge time
#for instance, how can I use the lambda function to
#select pred values that match '1979-01-02 00:00:00'
#witout using a for loop
"""


"""
first prepare the six time lagging dataframes  
then use the merge function to merge the original 
predictor with the lagging dataframes
"""

pred_lagged = pd.DataFrame()
for ii in range(1,time_all.shape[1]): #to loop through the lagged time series
    print(ii)
    #extracting corresponding tag time series
    lag_ts = pd.DataFrame(time_all.iloc[:,ii]) 
    lag_ts.columns = ['date']
    #merge the selected tlagged time with the predictor on = "date"
    pred_new = pd.merge(pred_subset_wo_nans, lag_ts, on = ['date'], how = 'left')
    pred_new.drop('Unnamed: 0', axis = 1, inplace = True)
    #sometimes nan values go to the bottom of the dataframe
    pred_new.sort_values(by = 'date', inplace=True)
    
    #concatenate lagged dataframe
    if ii == 1:
        pred_lagged = pred_new
    else: 
        pred_lagged = pd.merge(pred_lagged, pred_new, on = ['date'], how = 'left')
    
    








































