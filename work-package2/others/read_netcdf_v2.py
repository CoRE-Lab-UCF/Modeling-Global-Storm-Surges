# -*- coding: utf-8 -*-
"""
Created on Mon Dec 16 10:10:09 2019

@author: Michael Tadesse
"""
import os
import pandas as pd
from netCDF4 import Dataset


#####################
# Reading NetCDF file
#####################

def readnetcdf(path, predictor, year):
    """ 
    reads components of a netcdf file
    predictor: 'slp', 'uwnd', 'vwnd'
    year: start_end
    year_start: {1979, 1983, 1987, 1991, 1995, 1999, 2003, 2007, 2011}
    
    """
    var = {"slp":"msl", "uwnd":"u10", "vwnd":"v10"}
    
    os.chdir(path)
    pred_year = str(predictor)+"_"+str(year)+".nc"
    #print(pred_year)
    
    f = str()
    for ii in os.listdir():
        if ii.endswith(pred_year):
            f = ii
    #print(f)
    g = Dataset(os.path.abspath(f))
    #print(g.variables)
    
    lon, lat, time, pred = pd.DataFrame(g.variables['longitude'][:]), \
        pd.DataFrame(g.variables['latitude'][:]),\
            pd.DataFrame(g.variables['time'][:]), g.variables[var[predictor]][:]
  
    return lon, lat, time, pred



