# -*- coding: utf-8 -*-
"""
Created on Tue Dec 17 15:16:29 2019

@author: Michael Tadesse
"""
import pandas as pd
import datetime


#####################
# Subset predictors
#####################

def subsetter(pred, ind_grids, time):
    """
    subsets the given predictor for the provided
    indices of closest grids
    
    *pred = nc_files[3]
    -----------------------------------------------------------
    also these might be useful ...
    tg_cord = Coordinate(8.7167, 53.867)
    path = "C:/Users/WahlInstall/Documents/ml_project_v3/data"
    lon, lat, time = nc_files[0], nc_files[1], nc_files[2]
    -----------------------------------------------------------
    *ind_grids = findindx(close_grids, lon, lat)
    *close_grids = findPixels(tg_cord, 5, lon, lat)
    """
    pred_sub = pd.DataFrame(columns = list(range(len(ind_grids))));
    for kk in range(len(ind_grids)):
        #print(kk)
        pred_sub[kk] = pred[:, ind_grids[1][kk], ind_grids[0][kk]]
    print("total features: ", pred_sub.shape[1])
    time_original = pd.to_datetime('1900-01-01')
    int_changer = lambda x: int(x)
    time_int = pd.DataFrame(map(int_changer, time[0]))    
    time_convertor = lambda x: time_original + datetime.timedelta(hours = x)
    time_readable = pd.DataFrame(map(time_convertor, time_int[0]), columns = ['date'])
    pred_sub_concat = pd.concat([time_readable, pred_sub], axis = 1)
    
    
    return pred_sub_concat
    