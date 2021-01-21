# -*- coding: utf-8 -*-
"""
Created on Fri Dec 20 09:07:00 2019

@author: Michael Tadesse
"""
from get_eraint_files import get_eraint_files

def compile_predictors(tg_cord, delta, path):
    """
    compiles a larger dataframe that contains 
    uwnd, vwnd, and slp for the selected tide gauge
    
    pred_name: 'slp', 'uwnd', 'vwnd'
    
    delta: distance (in degrees) from the tide gauge
    
    path: location of the netcdf files
    
    source for data is always in seagate (E:\data\...)
    
    pred_combo: the concatenation of all three predictors
    """
    var = {1:"uwnd", 2:"vwnd", 3:"slp"}
    
    print("Extracting uwnd")
    print("\n"*2)
    pred_uwnd = get_eraint_files(var[1], tg_cord, delta, path)
    print("Extracting vwnd")
    print("\n"*2)
    pred_vwnd = get_eraint_files(var[2], tg_cord, delta, path)
    print("Extracting slp")
    print("\n"*2)
    pred_slp = get_eraint_files(var[3], tg_cord, delta, path)
    
    #concatenate predictors
    pred_uwnd_u10 = pred_uwnd[3]
    pred_vwnd_v10 = pred_vwnd[3]
    pred_slp_msl = pred_slp[3]
    
    uwnd_vwnd = pred_uwnd_u10.merge(pred_vwnd_v10, on='date', \
                              how = 'inner', suffixes=('_uwnd', '_vwnd'))
    
    uwnd_vwnd_slp = uwnd_vwnd.merge(pred_slp_msl, on='date', \
                                    how = 'inner', suffixes=('_', '_slp'))

    
    return pred_uwnd, pred_vwnd, pred_slp, uwnd_vwnd_slp