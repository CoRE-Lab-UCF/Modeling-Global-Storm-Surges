# -*- coding: utf-8 -*-
"""
Created on Fri Apr 17 08:40:16 2020

***********************************************
Master script to run the lagging of predictors 
for different grid sizes
***********************************************

@author: Michael Tadesse
"""

import os 
dir_in = 'D:\\data\\scripts\\modeling_storm_surge\\wp2\\grid_size_sa\\preprocess'
os.chdir(dir_in)
from c_lag_predictors_v2 import lag

folder_name = ['eraint_D4', 'eraint_D3', 'eraint_D2', 'eraint_D1.5', \
               'eraint_D1', 'eraint_D0.5'] 

#loop through the folders
for grid in folder_name:
    lag(grid)












