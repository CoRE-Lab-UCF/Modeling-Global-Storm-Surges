# -*- coding: utf-8 -*-
"""
Created on Fri Apr 17 08:40:16 2020

***********************************************
Master script - lagging of predictors 20thCR
***********************************************

@author: Michael Tadesse
"""

import os 
dir_in = 'D:\\data\\scripts\\modeling_storm_surge\\wp2\\20cr_scripts\\02_preprocessing'
os.chdir(dir_in)
from c_20cr_lag_predictors_v3 import lag

lag()












