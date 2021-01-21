# -*- coding: utf-8 -*-
"""
Created on Tue Apr 16 16:11:00 2020
--------------------------------------------
Load predictors for each TG and combine them
--------------------------------------------

@author: Michael Tadesse
"""

import os 
import pandas as pd

#define directories
dir_in = 'F:\\01_eraint_predictors'
dir_out = 'F:\\02_eraint_combined_predictors'

folder_name = 'eraint_D0.5'

def combine(folder_name):
    #looping through tide gauges
    os.chdir(os.path.join(dir_in, folder_name))
    
    for tg in ['le_havre-france-refmar']:
        print(tg, '\n')
        
        
        #looping through each TG folder
        os.chdir(tg)
        
        #defining the path for each predictor
        where = os.getcwd()
        csv_path = {'slp' : os.path.join(where, 'slp.csv'),\
                   "wnd_u": os.path.join(where, 'wnd_u.csv'),\
                   'wnd_v' : os.path.join(where, 'wnd_v.csv')}
            
        first = True   
        for pr in csv_path.keys():
            print(folder_name, ' ', tg, ' ', pr)
              
            #read predictor
            pred = pd.read_csv(csv_path[pr])
            
            #remove unwanted columns
            pred.drop(['Unnamed: 0', 'Unnamed: 0.1'], axis = 1, inplace=True)
            
            
            #give predictor columns a name
            pred_col = list(pred.columns)
            for pp in range(len(pred_col)):
                if pred_col[pp] == 'date':
                    continue
                pred_col[pp] = pr + str(pred_col[pp])
            pred.columns = pred_col
            
            #merge all predictors
            if first:
                pred_combined = pred
                first = False
            else:
                pred_combined = pd.merge(pred_combined, pred, on = 'date')
            
        #saving pred_combined
        os.chdir(os.path.join(dir_out, folder_name))
        pred_combined.to_csv('.'.join([tg, 'csv']))
        os.chdir(os.path.join(dir_in, folder_name))
        print('\n')




