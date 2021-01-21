# -*- coding: utf-8 -*-
"""
Created on Wed Apr  1 16:17:58 2020
Saving observed surges with readable time format
@author: Michael Tadesse
"""

import os
import pandas as pd
from surgets import add_date #might need to cd to the folder 


dir_in = 'D:\data\obs_surge'
dir_out = 'F:\obs_surge'

#cd to the original csvs
os.chdir(dir_in)

#looping through each csv file
for tg in os.listdir():
    print(tg)
    if os.stat(tg).st_size == 0:
        print('\n', "This tide gauge has no surge data!", '\n')
        continue
    surge = pd.read_csv(tg, header = None)
    
    #change its date to readable format
    surge_with_date = add_date(surge)
    surge_ts = pd.concat([surge_with_date['date'], surge_with_date[8]], axis = 1)
    surge_ts.columns = ['date', 'surge']
    
    #save name
    os.chdir(dir_out)
    tg_name = '.'.join([tg.split('.mat.mat.csv')[0], 'csv'])
    surge_ts.to_csv(tg_name)
    
    #return to dir_in
    os.chdir(dir_in)

    
    
    
        