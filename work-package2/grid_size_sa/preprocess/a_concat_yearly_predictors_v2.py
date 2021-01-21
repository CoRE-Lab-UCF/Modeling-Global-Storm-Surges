# -*- coding: utf-8 -*-
"""
Created on Tue Apr 16 10:02:00 2020
---------------------------------------------------------
This script concatenates yearly predictor files

Browses the different grid size folders for the chosen TG

Browses the predictor folders for the chosen TG

Concatenates the yearly csvs for the chosen predictor

Saves the concatenated csv in a separate directory

It perpetuates the concatenation for several grid sizes
---------------------------------------------------------

@author: Michael Tadesse
"""
#%% import packages
import os
import pandas as pd

#%% define directories
home = 'D:\\data\\era_interim\\eraint_localized'
out_path = 'F:\\01_eraint_predictors'


#cd to the home dir to get TG information
os.chdir(home)
tg_list = os.listdir()



#%%looping through grid size folders 

#define the folder names for the grid sizes
#avoid D5 as results have already been computed
grid_size = ['D4', 'D3', 'D2', 'D1.5', 'D1', 'D0.5']

for grid in grid_size:
    #cd to home in case there is an interruption    
    os.chdir(home)
    print('*'*88)
    print('Grid Size = {}'.format(grid))
    print('*'*88, '\n')

    #looping through TGs inside the D folders
    for tg in tg_list:
        print(grid, ' ', tg)
                
        #concatenate folder paths
        os.chdir(os.path.join(home, tg, grid))
            
        #defining the folders for predictors
        #choose only u, v, and slp
        where = os.getcwd()
        csv_path = {'slp' : os.path.join(where, 'slp'),\
                   "wnd_u": os.path.join(where, 'wnd_u'),\
                   'wnd_v' : os.path.join(where, 'wnd_v')}
        
        #%%looping through predictors in the chosen grid
        for pred in csv_path.keys():
            os.chdir(os.path.join(home, tg, grid))
            print(grid, ' ', tg, ' ', pred, '\n')
            
            #cd to the chosen predictor
            os.chdir(pred)
            
            #%%looping through the yearly csv files
            count = 1
            for yr in os.listdir():
                print(grid, ' ', tg, ' ', pred, ' ', yr)
                if count == 1:
                    dat = pd.read_csv(yr)
                    print('original size is: {}'.format(dat.shape))
                    
                else:
                    #remove the header of the subsequent csvs before merging
                    # dat_yr = pd.read_csv(yr, header=None).iloc[1:,:]
                    dat_yr = pd.read_csv(yr)
                    dat_yr.shape
                    dat = pd.concat([dat, dat_yr], axis = 0)
                    print('concatenated size is: {}'.format(dat.shape))
                count+=1
        
            #saving concatenated predictor
            #cd to the saving location
            os.chdir(out_path)
            
            #create/cd to the grid folder
            #save name for grid size folder
            grid_name = '_'.join(['eraint', grid])
            try:
                os.makedirs(grid_name)
                os.chdir(grid_name) #cd to it after creating it
            except FileExistsError:
                #directory already exists
                os.chdir(grid_name)
            
            #create/cd to the tg folder
            try:
                os.makedirs(tg)
                os.chdir(tg) #cd to it after creating it
            except FileExistsError:
                #directory already exists
                os.chdir(tg)
            #save as csv
            pred_name = '.'.join([pred, 'csv'])
            dat.to_csv(pred_name)
        