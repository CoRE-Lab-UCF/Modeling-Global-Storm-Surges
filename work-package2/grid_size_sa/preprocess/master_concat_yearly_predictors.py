# -*- coding: utf-8 -*-
"""
Created on Thu Apr 16 10:49:37 2020

master script to initiate grouping
of yearly predictor csvs

@author: Michael Tadesse
"""

import os 
dir_in = 'D:\\data\\scripts\\modeling_storm_surge\\wp2\\grid_size_sa\\preprocess'
os.chdir(dir_in)
import a_concat_yearly_predictors_v2 
