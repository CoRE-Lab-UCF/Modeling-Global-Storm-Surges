# -*- coding: utf-8 -*-
"""
Created on Tue May 13 10:02:00 2020
---------------------------------------------------------
This script concatenates yearly predictor files

Browses the predictor folders for the chosen TG

Concatenates the yearly csvs for the chosen predictor

Saves the concatenated csv in a separate directory

---------------------------------------------------------

@author: Michael Tadesse
"""
#%% import packages
import os
import pandas as pd

#%% define directories
home = '/lustre/fs0/home/mtadesse/erafive_localized'
out_path = '/lustre/fs0/home/mtadesse/eraFiveConcat'


#cd to the home dir to get TG information
os.chdir(home)
tg_list = os.listdir()



x = 201
y = 202


#looping through TGs
for t in range(x, y): 
    
    tg = tg_list[t]
    print(tg)
            
    #concatenate folder paths
    os.chdir(os.path.join(home, tg))
        
    #defining the folders for predictors
    #choose only u, v, and slp
    where = os.getcwd()
    
    csv_path = {'slp' : os.path.join(where, 'slp'),\
                "wnd_u": os.path.join(where, 'wnd_u'),\
                'wnd_v' : os.path.join(where, 'wnd_v')}
    
    #%%looping through predictors
    for pred in csv_path.keys():
        os.chdir(os.path.join(home, tg))
        # print(tg, ' ', pred, '\n')
        
        #cd to the chosen predictor
        os.chdir(pred)
        
        #%%looping through the yearly csv files
        count = 1
        for yr in os.listdir():
            print(pred, ' ', yr)
            if count == 1:
                dat = pd.read_csv(yr)
                # print('original size is: {}'.format(dat.shape))
                
            else:
                #remove the header of the subsequent csvs before merging
                # dat_yr = pd.read_csv(yr, header=None).iloc[1:,:]
                dat_yr = pd.read_csv(yr)
                dat_yr.shape
                dat = pd.concat([dat, dat_yr], axis = 0)
                # print('concatenated size is: {}'.format(dat.shape))
            count+=1
    
        print(dat.shape)
        #saving concatenated predictor
        #cd to the saving location
        os.chdir(out_path)
        
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
    