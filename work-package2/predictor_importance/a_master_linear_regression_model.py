# -*- coding: utf-8 -*-
"""
Created on Thu Apr  9 16:33:43 2020

Master script to run linear regression model 

base_case = wnd_u, wnd_v, slp
prcp_case =  wnd_u, wnd_v, slp, prcp
sst_case =  wnd_u, wnd_v, slp, sst

@author: Michael Tadesse
"""

import os 
os.chdir('D:\\data\\scripts\\modeling_storm_surge\\wp2\\predictor_importance')

from b_preprocess import preprocess

validation = preprocess('base_case')

