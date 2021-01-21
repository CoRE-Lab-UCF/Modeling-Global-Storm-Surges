# -*- coding: utf-8 -*-
"""
Created on Tue Mar 31 17:12:23 2020

****************************************************
Load predictors & predictands + predictor importance
****************************************************

@author: Michael Tadesse
"""

#import packages
import os 
import pandas as pd
import datetime as dt #used for timedelta
from datetime import datetime

#define directories
dir_in = 'F:\\02_eraint_combined_predictors'
dir_out = 'F:\\03_eraint_lagged_predictors'

def lag(folder_name):
    #looping through tide gauges
    os.chdir(os.path.join(dir_in, folder_name))

    for tg in ['le_havre-france-refmar.csv']:
        tg_name = tg
        print(tg, ' ', tg_name, '\n')
    
        pred = pd.read_csv(tg_name)
    
    
        #create a daily time series - date_range
        #get only the ymd of the start and end times
        start_time = pred['date'][0].split(' ')[0]
        end_time = pred['date'].iloc[-1].split(' ')[0]
        
        print(start_time, ' - ', end_time, '\n')
        
        date_range = pd.date_range(start_time, end_time, freq = 'D')
        
        
        #defining time changing lambda functions
        time_str = lambda x: str(x)
        time_converted_str = pd.DataFrame(map(time_str, date_range), columns = ['date'])
        time_converted_stamp = pd.DataFrame(date_range, columns = ['timestamp'])
        
                
        """
        first prepare the six time lagging dataframes  
        then use the merge function to merge the original 
        predictor with the lagging dataframes
        """
        
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
        

        pred_lagged = pd.DataFrame()
        for ii in range(1,time_all.shape[1]): #to loop through the lagged time series
            print(time_all.columns[ii], '\n')
            #extracting corresponding tag time series
            lag_ts = pd.DataFrame(time_all.iloc[:,ii]) 
            lag_ts.columns = ['date']
            #merge the selected tlagged time with the predictor on = "date"
            pred_new = pd.merge(pred, lag_ts, on = ['date'], how = 'right')
            pred_new.drop('Unnamed: 0', axis = 1, inplace = True)
            #sometimes nan values go to the bottom of the dataframe
            #sort df by date -> reset the index -> remove old index
            pred_new.sort_values(by = 'date', inplace=True)
            pred_new.reset_index(inplace=True)
            pred_new.drop('index', axis = 1, inplace= True)
            
            #concatenate lagged dataframe
            if ii == 1:
                pred_lagged = pred_new
            else: 
                pred_lagged = pd.concat([pred_lagged, pred_new.iloc[:,1:]], axis = 1)
                
        
        #cd to saving directory
        os.chdir(os.path.join(dir_out, folder_name))
        pred_lagged.to_csv(tg_name)
        os.chdir(os.path.join(dir_in, folder_name))

    
    








































