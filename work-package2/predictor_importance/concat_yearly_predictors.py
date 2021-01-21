# -*- coding: utf-8 -*-
"""
Created on Tue Mar 31 12:01:36 2020

This script concatenates yearly predictor files


@author: Michael Tadesse
"""
import os
import pandas as pd

home = 'D:\data\era_interim\eraint_localized'
out = 'F:\eraint_D5'

#cd to the home dir to get TG information
os.chdir(home)
tg_list = os.listdir()

#looping through TG folders
for tg in tg_list:
    os.chdir(home)
    print(tg)
    
    #cd to the D5 directory
    #concatenate folder paths
    os.chdir(os.path.join(home, tg, 'D5'))
    
    #defining the folders for predictors
    where = os.getcwd()
    csv_path = {'prcp' : os.path.join(where, 'prcp'), \
               'slp' : os.path.join(where, 'slp'),\
               'sst' : os.path.join(where, 'sst'), \
               "wnd_u": os.path.join(where, 'wnd_u'),\
               'wnd_v' : os.path.join(where, 'wnd_v')}
    
    #looping through predictors in D5
    for pred in csv_path.keys():
        os.chdir(os.path.join(home, tg, 'D5'))
        print(pred)
        
        #cd to the chosen predictor
        os.chdir(pred)
        
        #looping through the yearly csv files
        count = 1
        for yr in os.listdir():
            print(yr)
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
        os.chdir(out)
        try:
            os.makedirs(tg)
            os.chdir(tg) #cd to it after creating it
        except FileExistsError:
            #directory already exists
            os.chdir(tg)
        #save as csv
        pred_name = '.'.join([pred, 'csv'])
        dat.to_csv(pred_name)
        
            
 
            
            
        

