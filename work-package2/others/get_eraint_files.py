# -*- coding: utf-8 -*-
"""
Created on Thu Dec 19 16:20:40 2019

@author: Michael Tadesse
"""

import os
import pandas as pd
from read_netcdf_v4 import readnetcdf
from subset import subsetter
from define_grid import findPixels, findindx

def get_eraint_files(pred_name, tg_cord, delta, path):
    """
    This iterates through netCDF files and extracts
    predictor data along with lon/lat/time
    
    pred_name: 'slp', 'uwnd', 'vwnd'
    
    tg_cord: longitude and latitude of the tide gauge
    
    delta: distance (in degrees) from the tide gauge
    
    path: location of the netcdf files
    
    source for data is always in seagate (E:\data\...)
    """
    os.chdir(path)
    files = pd.DataFrame(os.listdir())
    
    pred_string = str('era_interim_')+str(pred_name)
    checker = lambda x: x.startswith(pred_string)
    files_sub = files[list(map(checker, files[0]))]
    
    print(len(files_sub), "netCDF files found for this preditcor.")
    
    
    count = 0; 
    time = pd.DataFrame(); pred_sub = pd.DataFrame()
    
    for ii in files_sub[0]:
        print(ii)
        if count == 0:
            lon,lat = readnetcdf(pred_name, ii)[0], readnetcdf(pred_name, ii)[1]
            close_grids = findPixels(tg_cord, delta, lon, lat)
            ind_grids = findindx(close_grids, lon, lat)
        
        
        
        time_new = readnetcdf(pred_name, ii)[2]
        pred = readnetcdf(pred_name, ii)[3]
        
        pred_new = subsetter(pred, ind_grids, time_new)
        
        time = pd.concat([time, time_new], axis = 0)
        pred_sub = pd.concat([pred_sub, pred_new], axis = 0)
        
        count += 1
    return lon, lat, time, pred_sub
        
        
    

    
    
    
    
    
    