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
dir_name = 'F:\\01_erainterim\\01_eraint_predictors\\eraint_D3'
dir_in = 'E:\\03_20cr\\01_20cr_predictiors'
dir_out = 'E:\\03_20cr\\02_20cr_combined_predictors'

def combine():
    #get name of tide gauges from another folder that has the full names
    #checked 882 tgs in eraint folde; same ones in 20CR folder -> go ahead
    os.chdir(dir_name)
    
    #get names
    tg_list_name = os.listdir()
    
    #cd to where the actual file is 
    os.chdir(dir_in)
    
    
    for tg in tg_list_name:
        tg_name = tg
        print(tg_name, '\n')
        
        
        #looping through each TG folder
        os.chdir(tg)
        
        #defining the path for each predictor
        where = os.getcwd()
        
    
        csv_path = {'slp' : os.path.join(where, 'slp.csv'),\
                    "wnd_u": os.path.join(where, 'wnd_u.csv'),\
                    'wnd_v' : os.path.join(where, 'wnd_v.csv')}
        
     
        
        first = True   
        for pr in csv_path.keys():
            print(tg, ' ', pr)
              
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
        os.chdir(dir_out)
        pred_combined.to_csv('.'.join([tg, 'csv']))
        os.chdir(dir_in)
        print('\n')




