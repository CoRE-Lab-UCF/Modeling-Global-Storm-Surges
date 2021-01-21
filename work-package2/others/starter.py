# -*- coding: utf-8 -*-
"""
Created on Thu Dec 19 09:30:37 2019

@author: Michael Tadesse
"""
import time 
import os 
import pandas as pd

script_path = "C:/Users/WahlInstall/Documents/ml_project_v3/scripts/modeling_storm_surge"
os.chdir(script_path)

nc_path = "E:\data\era_interim" #where netcdf files are stored
surge_path = "E:\data\obs_surge"
csv_path = "E:\data\pred_and_surge"

from define_grid import Coordinate
from surgets import add_date
from compiler import compile_predictors


#define tide gauge
tg_cord = Coordinate(8.7167, 53.867)

#provide the observed surge
os.chdir(surge_path)
surge = pd.read_csv('cuxhaven-germany-bsh.mat.mat.csv', header=None)
#add date column to the surge time series
surge_with_date = add_date(surge)


#get nc files
t0 = time.time()
nc_files = compile_predictors(tg_cord, 5, data_path)
print(time.time() - t0)

#concatenated predictors
pred_combo = nc_files[3]


#concatenate predictors with obs_surge
pred_and_surge = pd.merge(pred_combo, surge_with_date.iloc[:,8:], \
                          on="date", how="inner")

#save as csv
os.chdir(csv_path)
pred_and_surge.to_csv('cuxhaven.csv')

