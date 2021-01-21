# -*- coding: utf-8 -*-
"""
Created on Thu Apr 16 16:14:16 2020

--------------------------------------------
Master script for combining predictors for 
all grid size csvs
--------------------------------------------
@author: Michael
"""

import os 
dir_in = 'D:\\data\\scripts\\modeling_storm_surge\\wp2\\grid_size_sa\\preprocess'
os.chdir(dir_in)

from b_combined_predictors_v3 import combine


#define dolder name
folder_name = ['eraint_D4', 'eraint_D3', 'eraint_D2', 'eraint_D1.5', \
               'eraint_D1', 'eraint_D0.5']

#loop through the folder_name
for ii in folder_name:
    combine(ii)
