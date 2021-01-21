# -*- coding: utf-8 -*-
"""
Created on Wed May 13 10:40:00 2020

--------------------------------------------
Master script - combining predictors 20thCR
--------------------------------------------
@author: Michael
"""

import os 
dir_in = 'D:\\data\\scripts\\modeling_storm_surge\\wp2\\20cr_scripts\\02_preprocessing'
os.chdir(dir_in)

from b_20cr_combined_predictors_v3 import combine

combine()
