# -*- coding: utf-8 -*-
"""
Created on Mon Jun 01 11:54:00 2020

@author: Michael Tadesse
"""
import pandas as pd
from netCDF4 import Dataset


#####################
# Reading NetCDF file
#####################

def readnetcdf(pred_file):
    """ 
    reads components of a netcdf file
    
    pred_file: the name of the netCDF file to read from for instance 
    ('era_interim_uwnd_2011_2014.nc')

    """
    var = {"slp":"SLP", "wnd_u":"U10M", "wnd_v":"V10M", "prcp":"tp","sst":"sst"}
    
    #print(f)
    g = Dataset(pred_file, mode = 'r')
    #print(g.variables)
    
    lon, lat, time_raw, predSLP, predU10, predV10 = pd.DataFrame(g.variables['lon'][:]), \
        pd.DataFrame(g.variables['lat'][:]),\
            g.variables['time'], g.variables[var['slp']],\
                g.variables[var['wnd_u']], g.variables[var['wnd_v']]
  
    #extracting time values (in minutes)
    timeClean = pd.DataFrame(time_raw[:], columns=['minutes'])
    
    return lon, lat, timeClean, predSLP, predU10, predV10


