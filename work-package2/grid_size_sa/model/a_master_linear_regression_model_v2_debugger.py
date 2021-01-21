# -*- coding: utf-8 -*-
"""
Created on Thu Apr 17 14:29:00 2020

---------------------------------------------------------
Master script to run linear regression model 
for different grid sizes
---------------------------------------------------------

@author: Michael Tadesse
"""

import os 
os.chdir('D:\\data\\scripts\\modeling_storm_surge\\wp2\\grid_size_sa\\model')

from b_preprocess_v2 import preprocess

folder_name = ['eraint_D0.5']
    
for ii in folder_name:
    preprocess(ii)

