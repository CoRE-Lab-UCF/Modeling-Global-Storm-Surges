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

from b_preprocess_v2 import preprocess

#predictors to remove from the predictor matrix as per the case
# pred_case = {'base_case':['sst', 'prcp'],'prcp_case':['sst'], \
#              'sst_case':['prcp']}

#for extra testing
pred_case = {'u_v_case': ['sst', 'prcp', 'slp']}
for ii in pred_case.keys():
    print(ii)
    validation = preprocess(ii)

