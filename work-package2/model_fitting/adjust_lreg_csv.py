# -*- coding: utf-8 -*-
"""
Created on Thu May  7 09:24:29 2020

This script loads reconstructed surge
csv files and save

@author: Michael Tadesse
"""
import os 

dir_in = 'F:\\08_eraint_surge_reconstruction\\linear_regression'
dir_out = 'F:\\08_eraint_surge_reconstruction\\lreg'

os.chdir(dir_in)

for tg in os.listdir():
    
    print(tg)
    dat = pd.read_csv(tg)
    dat.drop(['Unnamed: 0', 'mean_se', 'mean_ci_lower','mean_ci_upper'],\
             axis = 1, inplace = True)
    dat.columns = ['date', 'surge_reconsturcted', \
                   'pred_int_lower', 'pred_int_upper', 'lon', 'lat']
    #save new csv
    os.chdir(dir_out)
    dat.to_csv(tg)
    
    os.chdir(dir_in)
    