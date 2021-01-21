# -*- coding: utf-8 -*-
"""
Created on Mon Jun 01 10:00:00 2020

MERRAv2 netCDF extraction script - template
To create an extraction script for each tide gauge

@author: Michael Tadesse
""" 
import os 
import time as tt
import pandas as pd
from d_merra_define_grid import Coordinate, findPixels, findindx
from c_merra_read_netcdf import readnetcdf
from f_merra_subset import subsetter

def extract_data(delta= 3):
    """
    This is the master function that calls subsequent functions
    to extract uwnd, vwnd, slp for the specified
    tide gauges
    
    delta: distance (in degrees) from the tide gauge
    """
    
    print('Delta =  {}'.format(delta), '\n')
    
    #defining the folders for predictors
    dir_in = "D:\\data\\MERRAv2\\data"
    surge_path = "D:\data\obs_surge"
    csv_path = "G:\\04_merra\\merra_localized"
    
    #cd to the obs_surge dir to get TG information
    os.chdir(surge_path)
    tg_list = os.listdir()
    
    #cd to the obs_surge dir to get TG information
    os.chdir(dir_in)
    years = os.listdir()
    
    #################################
    #looping through the year folders
    #################################

    for yr in years:
        os.chdir(dir_in)
        print(yr, '\n')
        os.chdir(os.path.join(dir_in, yr))

        ####################################
        #looping through the daily .nc files
        ####################################

        for dd in os.listdir():
            
            os.chdir(os.path.join(dir_in, yr)) #back to the predictor folder
            print(dd, '\n')
            
            #########################################
            #get netcdf components  - predictor file            
            #########################################

            nc_file = readnetcdf(dd)
            lon, lat, time, predSLP, predU10, predV10 = \
                nc_file[0], nc_file[1], nc_file[2], nc_file[3], nc_file[4]\
                    , nc_file[5]
            
            
            x = 175
            y = 176
            
            #looping through individual tide gauges
            for t in range(x, y):
                
                #the name of the tide gauge - for saving purposes
                # tg = tg_list[t].split('.mat.mat.csv')[0] 
                tg = tg_list[t]
                
                #extract lon and lat data from surge csv file
                print(tg, '\n')
                os.chdir(surge_path)
                
                if os.stat(tg).st_size == 0:
                    print('\n', "This tide gauge has no surge data!", '\n')
                    continue
                
                surge = pd.read_csv(tg, header = None)
                #surge_with_date = add_date(surge)
        
                #define tide gauge coordinate(lon, lat)
                tg_cord = Coordinate(surge.iloc[0,0], surge.iloc[0,1])
                
                
                #find closest grid points and their indices
                close_grids = findPixels(tg_cord, delta, lon, lat)
                ind_grids = findindx(close_grids, lon, lat)                
                
                
                #loop through preds#
                #subset predictor on selected grid size
                predictors = {'slp':predSLP, 'wnd_u':predU10, \
                              'wnd_v':predV10}
                
                for xx in predictors.keys():
                    
                    start_time = tt.time()
                    
                    pred_new = subsetter(dd, predictors[xx], ind_grids, time)
                    
                    print("--- %s seconds ---" % (tt.time() - start_time))

                    
                    #create directories to save pred_new
                    os.chdir(csv_path)
                    
                    # #compressed folder 
                    # folderName = getFolderName
                    # try:
                    #     os.makedirs(folderName)
                    #     os.chdir(folderName) #cd to it after creating it
                    # except FileExistsError:
                    #     #directory already exists
                    #     os.chdir(folderName)
                    
                    
                    #tide gauge directory
                    tg_name_old = tg.split('.mat.mat.csv')[0]
                    tg_name = '-'.join([str(t), tg_name_old])
                    try:
                        os.makedirs(tg_name)
                        os.chdir(tg_name) #cd to it after creating it
                    except FileExistsError:
                        #directory already exists
                        os.chdir(tg_name)
                    
                    #predictor directory
                    pred_name  = xx
                    
                    try:
                        os.makedirs(pred_name)
                        os.chdir(pred_name) #cd to it after creating it
                    except FileExistsError:
                        #directory already exists
                        os.chdir(pred_name)
                    
                    #time for saving file
                    ncTime = dd.split('.')[2]
                    
                    #save as csv
                    save_name = '_'.join([tg_name, pred_name, ncTime])\
                        + ".csv"
                    pred_new.to_csv(save_name)
                            
            
            # #return to the predictor directory
            # os.chdir(nc_path[pf])                
#run script
extract_data(delta= 3)        