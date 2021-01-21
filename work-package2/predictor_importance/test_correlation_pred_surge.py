# -*- coding: utf-8 -*-
"""
Created on Wed Apr  8 16:40:43 2020

Test correlation of predictors with surge

@author: Michael Tadesse
"""

import os
import pandas as pd
from datetime import datetime

dir_in = 'F:\\eraint_lagged_predictors'
dir_out = 'F:\\eraint_pred_surge_corr'
surge_path = 'F:\\dmax_surge_georef'
lonlat = 'D:\\data\\obs_surge'
#load predictors
#cd to the lagged predictors directory

os.chdir(dir_in)

#looping through TGs
for tg in range(len(os.listdir())):
    print(tg)
    
    tg_name = os.listdir()[tg]
    
    #load predictor
    pred = pd.read_csv(tg_name)
    pred.drop('Unnamed: 0', axis = 1, inplace = True)
    
    #load surge
    os.chdir(surge_path)
    surge = pd.read_csv(tg_name)
    surge.drop('Unnamed: 0', axis = 1, inplace = True)

    time_str = lambda x: str(datetime.strptime(x, '%Y-%m-%d'))
    surge_time = pd.DataFrame(list(map(time_str, surge['ymd'])))
    surge_new = pd.concat([surge_time, surge[['lon', 'lat','surge']]], axis = 1)
    surge_new.columns = ['date', 'lon', 'lat',  'surge']
    
    #filter pred with surge
    pred_surge = pd.merge(pred, surge_new, on='date', how='right')
    
    #compare correlation of predictors to surge
    cols = pred_surge.columns
    cols = pd.DataFrame(cols[1:-1], columns =['pred'])
    check_corr = lambda x: pred_surge[x].corr(pred_surge['surge'])
    corr_val = pd.DataFrame(map(check_corr, cols['pred']))
    pred_surge_corr = pd.concat([cols, corr_val], axis =1)
    pred_surge_corr.columns = ['pred', 'corrn']
    pred_surge_corr['abs_corrn'] = abs(pred_surge_corr['corrn'])
    
    #to sort the correlation values
    corr_sorted = pred_surge_corr.sort_values(by = 'abs_corrn', ascending= False)
    
    #predictor correlations - singled out
    prcp_corr = corr_sorted[list(map(lambda x: x.startswith('prcp'), \
                                    corr_sorted['pred']))]
    slp_corr = corr_sorted[list(map(lambda x: x.startswith('slp'), \
                                    corr_sorted['pred']))]
    u_corr = corr_sorted[list(map(lambda x: x.startswith('wnd_u'), \
                                    corr_sorted['pred']))]
    v_corr = corr_sorted[list(map(lambda x: x.startswith('wnd_v'), \
                                    corr_sorted['pred']))]
    sst_corr = corr_sorted[list(map(lambda x: x.startswith('sst'), \
                                    corr_sorted['pred']))]
    
    #getting description of all predictors
    d_prcp = prcp_corr['abs_corrn'].describe()
    d_slp = slp_corr['abs_corrn'].describe()
    d_u = u_corr['abs_corrn'].describe()
    d_v = v_corr['abs_corrn'].describe()
    d_sst = sst_corr['abs_corrn'].describe()
    
    #merge all descriptions
    description = pd.concat([d_prcp, d_slp, d_u, d_v, d_sst], axis = 1)
    description.columns = ['prcp', 'slp', 'wnd_u', 'wnd_v', 'sst']
    description.loc['lon'], description.loc['lat'] = \
        pred_surge['lon'][0],pred_surge['lat'][0]
    
    
    #save as csv
    os.chdir(dir_out)
    description.to_csv(tg_name)
    os.chdir(dir_in)
    







