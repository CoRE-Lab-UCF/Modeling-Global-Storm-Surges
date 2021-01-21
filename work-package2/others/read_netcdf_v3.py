# -*- coding: utf-8 -*-
"""
Created on Mon Dec 16 10:10:09 2019

@author: Michael Tadesse
"""
import os
import pandas as pd
import numpy as np
from netCDF4 import Dataset


#####################
# Reading NetCDF file
#####################

def readnetcdf(path, predictor):
    """ 
    reads components of a netcdf file
    predictor: 'slp', 'uwnd', 'vwnd'
    year: start_end
    year_start: {1979, 1983, 1987, 1991, 1995, 1999, 2003, 2007, 2011}
    
    """
    var = {"slp":"msl", "uwnd":"u10", "vwnd":"v10"}
    
    os.chdir(path)
    files = pd.DataFrame(os.listdir())
    #filter files that contain the requested predictor
    
    pred_name = str('era_interim_')+str(predictor)
    checker = lambda x: x.startswith(pred_name)
    files_sub = files[list(map(checker, files[0]))]
    
    f = str() #define string for the nc file
    count = 0; 
    time = pd.DataFrame(); pred = []
    for ii in files_sub[0]:
        
        print(ii)
        
        f = ii
        g = Dataset(os.path.abspath(f))
        
        if count == 0:
            lon, lat = pd.DataFrame(g.variables['longitude'][:]), \
        pd.DataFrame(g.variables['latitude'][:])
        
        
        time = pd.concat([time, pd.DataFrame(g.variables['time'][:])], axis = 0)
        #concatenate 3D arrays
        pred = np.concatenate([pred, g.variables[var[predictor]][:]],1)
        
        print(pred.shape)
        
        count +=1
  
    return lon, lat, time, pred



