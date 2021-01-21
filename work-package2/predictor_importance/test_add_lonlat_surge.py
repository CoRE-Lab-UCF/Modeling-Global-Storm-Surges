# -*- coding: utf-8 -*-
"""
Created on Wed Apr  8 17:31:11 2020

Add lon-lat data to dmax_surge csv files

@author: Michael Tadesse
"""

import os
import pandas as pd


dir_in = 'F:\\dmax_surge'
dir_out = 'F:\\dmax_surge_georef'
surge_path = 'D:\\data\\obs_surge'

#cd to dmax surge directory
os.chdir(dir_in)

#looping through TGs
for tg in range(len(os.listdir())):
    
    tg_name = os.listdir()[tg]
    
    print(tg_name)

    #load dmax surge
    surge = pd.read_csv(tg_name)
    surge.drop('Unnamed: 0', axis = 1, inplace = True)
    
    
    #cd to obs_surge directory
    os.chdir(surge_path)
    old_name = tg_name.split('.csv')[0] + '.mat.mat.csv'
    print(old_name, '\n')
    old_surge = pd.read_csv(old_name)
    
    #concatenate lon and lat to dmax surge
    surge['lon'], surge['lat'] = old_surge.iloc[0,0], old_surge.iloc[0,1]
    
    #save the new dmax surg csv
    os.chdir(dir_out)
    surge.to_csv(tg_name)
    os.chdir(dir_in)
    