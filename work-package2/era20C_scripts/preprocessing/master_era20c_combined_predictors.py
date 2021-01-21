# -*- coding: utf-8 -*-
"""
Created on Wed May 13 10:40:00 2020

--------------------------------------------
Master script - combining predictors ERA20C
--------------------------------------------
@author: Michael
"""

import os 
dir_in = 'D:\\data\\scripts\\modeling_storm_surge\\wp2\\era20C_scripts\\preprocessing'
os.chdir(dir_in)

from b_era20c_combined_predictors_v3 import combine

combine()
