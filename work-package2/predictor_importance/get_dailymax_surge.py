# -*- coding: utf-8 -*-
"""
Created on Wed Apr  1 17:25:43 2020
Get daily maximum surge from hourly obs_surge
@author: Michael Tadesse
"""

import os
import time 
import pandas as pd
from datetime import datetime

dir_in = 'F:\obs_surge'
dir_out = 'F:\dmax_surge'

#cd to the original csvs
os.chdir(dir_in)

#looping through each csv file
for tg in os.listdir():
    print(tg)
    surge = pd.read_csv(tg)
    surge.drop('Unnamed: 0', axis = 1, inplace = True)
    
    #change its date to readable format
    convertor = lambda x: datetime.strptime(x, '%Y-%m-%d %H:%M:%S')
    surge['date'] = list(map(convertor, surge['date']))
    
    #shorten date to just year,month,day
    ymd_convertor = lambda x: x.date()
    surge['ymd'] = list(map(ymd_convertor, surge['date']))
    
    #pick the daily max
    day_unique = surge['ymd'].unique()
    
    
    #looping through the unique dates
    surgemax = pd.DataFrame(columns = ['date', 'surge', 'ymd'])
    for dd in day_unique:
        # print(dd)
        day_surge = surge[surge['ymd'] == dd]
        
        #taking only positive maximum surge per day
        dayMax_surge = day_surge[day_surge['surge'] == day_surge['surge'].max()]
        surgemax = pd.concat([surgemax, dayMax_surge], axis = 0)
    
    #save name
    os.chdir(dir_out)
    tg_name = '.'.join([tg.split('.csv')[0], 'csv'])
    surgemax.to_csv(tg_name)
    
    #cd to the original csvs
    os.chdir(dir_in)