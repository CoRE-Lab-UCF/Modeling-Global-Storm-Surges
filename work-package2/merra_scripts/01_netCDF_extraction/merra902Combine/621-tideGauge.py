# -*- coding: utf-8 -*-
"""
Created on Tue Jun 17 11:28:00 2020
--------------------------------------------
Load predictors for each TG and combine them
--------------------------------------------

@author: Michael Tadesse
"""

import os 
import pandas as pd

#define directories
# dir_name = 'F:\\01_erainterim\\01_eraint_predictors\\eraint_D3'
dir_in = "/lustre/fs0/home/mtadesse/merraLocalized"
dir_out = "/lustre/fs0/home/mtadesse/merraAllCombined"

def combine():
    os.chdir(dir_in)
    
    #get names
    tg_list_name = os.listdir()
    
    
    x = 621
    y = 622
    
    
    for tg in range(x, y):
        os.chdir(dir_in)
        tg_name = tg_list_name[tg]
        print(tg_name, '\n')
        
        
        #looping through each TG folder
        os.chdir(tg_name)
        
        #check for empty folders
        if len(os.listdir()) == 0:
            continue
        
        #defining the path for each predictor
        where = os.getcwd()
        
    
        csv_path = {'slp' : os.path.join(where, 'slp.csv'),\
                    "wnd_u": os.path.join(where, 'wnd_u.csv'),\
                    'wnd_v' : os.path.join(where, 'wnd_v.csv')}
        
     
        
        first = True   
        for pr in csv_path.keys():
            print(tg_name, ' ', pr)
              
            #read predictor
            pred = pd.read_csv(csv_path[pr])
            
            #remove unwanted columns
            pred.drop(['Unnamed: 0'], axis = 1, inplace=True)
            #sort based on date as merra files are scrambled
            pred.sort_values(by = 'date', inplace=True)
            
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
        tg_name = str(tg)+"_"+tg_name;
        pred_combined.to_csv('.'.join([tg_name, 'csv']))
        os.chdir(dir_in)
        print('\n')

#run script
combine()


