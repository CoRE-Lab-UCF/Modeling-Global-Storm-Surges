# -*- coding: utf-8 -*-
"""
Created on Fri May 08 15:43:00 2020

This is the master script that runs the following processes for ERA20C predictors

#1 Reading the observed surge time series for 902 tide gauges

#2 Reading netcdf files to extract predictors for each tide gauge
  
#3 Saving the dataframe as a .csv in the ../pred

*delta: distance (in degrees) from the tide gauge - this will form 
        a grid of delta x delta box around each tide gauge

@author: Michael Tadesse
"""

import os 
os.chdir("D:\\data\\scripts\\modeling_storm_surge\\wp2\\era20C_scripts")
from b_era20c_extract_data import extract_data
         
#del_options = [5, 4, 3, 2, 1.5]
#looping through different grid size options
delta = 3;
extract_data(delta)
