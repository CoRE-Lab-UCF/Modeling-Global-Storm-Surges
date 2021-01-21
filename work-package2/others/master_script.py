# -*- coding: utf-8 -*-
"""
Created on Fri Dec 20 15:32:21 2019

This is the master script that runs the following processes

#1 Reading the observed surge time series for 902 tide gauges

#2 Reading netcdf files to extract predictors for each tide gauge

#3 Concatenating predictors with corresponding surge time series 
   for each tide gauge and save as a dataframe
   
#4 Saving the dataframe as a .csv in the ../pred_and_surge

*delta: distance (in degrees) from the tide gauge - this will form 
        a grid of delta x delta box around each tide gauge
@author: Master Script
"""

import os 
os.chdir("E:\data\scripts\modeling_storm_surge")
from extract_data import extract_data
         
delta = 5
extract_data(delta)

         



