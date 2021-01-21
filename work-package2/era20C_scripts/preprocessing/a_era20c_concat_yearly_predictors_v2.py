# -*- coding: utf-8 -*-
"""
Created on Tue May 13 10:02:00 2020
---------------------------------------------------------
This script concatenates yearly predictor files

Browses the different grid size folders for the chosen TG

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
home = 'F:\\era20C\\era20C_localized'
out_path = 'F:\\era20C\\01_era20C_predictors'


#cd to the home dir to get TG information
os.chdir(home)
tg_list = os.listdir()




#looping through TGs 
for tg in tg_list:
    print(tg)
            
    #concatenate folder paths
    os.chdir(os.path.join(home, tg))
        
    #defining the folders for predictors
    #choose only u, v, and slp
    where = os.getcwd()
    
    #run the two until wnd_v is prepared
    csv_path = {'wnd_v' : os.path.join(where, 'wnd_v')}
    
    # csv_path = {'slp' : os.path.join(where, 'slp'),\
    #            "wnd_u": os.path.join(where, 'wnd_u'),\
    #            'wnd_v' : os.path.join(where, 'wnd_v')}
    
    #%%looping through predictors
    for pred in csv_path.keys():
        os.chdir(os.path.join(home, tg))
        print(tg, ' ', pred, '\n')
        
        #cd to the chosen predictor
        os.chdir(pred)
        
        #%%looping through the yearly csv files
        count = 1
        for yr in os.listdir():
            print(tg, ' ', pred, ' ', yr)
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
    