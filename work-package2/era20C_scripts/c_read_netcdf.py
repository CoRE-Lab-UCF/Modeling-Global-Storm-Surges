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

def readnetcdf(pred_name, pred_file):
    """ 
    reads components of a netcdf file
    
    pred_file: the name of the netCDF file to read from for instance 
    ('era_interim_uwnd_2011_2014.nc')

    """
    var = {"slp":"msl", "wnd_u":"u10", "wnd_v":"v10", "prcp":"tp","sst":"sst"}
    
    #print(f)
    g = Dataset(pred_file)
    #print(g.variables)
    
    lon, lat, time, pred = pd.DataFrame(g.variables['longitude'][:]), \
        pd.DataFrame(g.variables['latitude'][:]),\
            pd.DataFrame(g.variables['time'][:]), g.variables[var[pred_name]][:]
  
    return lon, lat, time, pred



