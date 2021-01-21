# -*- coding: utf-8 -*-
"""
Created on Fri Apr 17 08:40:16 2020

***********************************************
Master script - lagging of predictors ERA20C
***********************************************

@author: Michael Tadesse
"""

import os 
dir_in = 'D:\\data\\scripts\\modeling_storm_surge\\wp2\\era20C_scripts\\preprocessing'
os.chdir(dir_in)
from c_era20c_lag_predictors_v2 import lag

lag()












