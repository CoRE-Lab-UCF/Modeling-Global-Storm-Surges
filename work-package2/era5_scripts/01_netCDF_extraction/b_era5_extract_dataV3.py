# -*- coding: utf-8 -*-
"""
Created on Mon Jun 01 10:00:00 2020

ERA5 netCDF extraction script

@author: Michael Tadesse
""" 
import time as tt
import os 
import pandas as pd
from d_define_grid import Coordinate, findPixels, findindx
from c_read_netcdf import readnetcdf
from f_era5_subsetV3 import subsetter

def extract_data(delta= 3):
    """
    This is the master function that calls subsequent functions
    to extract uwnd, vwnd, slp for the specified
    tide gauges
    
    delta: distance (in degrees) from the tide gauge
    """
    
    print('Delta =  {}'.format(delta), '\n')
    
    #defining the folders for predictors
    nc_path = {'slp' : "/lustre/fs0/home/mtadesse/era_five/slp",\
           "wnd_u": "/lustre/fs0/home/mtadesse/era_five/wnd_u",\
           'wnd_v' : "/lustre/fs0/home/mtadesse/era_five/wnd_v"}
    surge_path = "/lustre/fs0/home/mtadesse/obs_surge"
    csv_path = "/lustre/fs0/home/mtadesse/era5Localized"
    
    #cd to the obs_surge dir to get TG information
    os.chdir(surge_path)
    tg_list = os.listdir()
    
    
    #################################
    #looping through the predictor folders
    #################################

    for pf in nc_path.keys():

        print(pf, '\n')
        os.chdir(nc_path[pf])

        ####################################
         #looping through the years of the chosen predictor
        ####################################

        for py in os.listdir():
            
            os.chdir(nc_path[pf]) #back to the predictor folder
            print(py, '\n')
            #get netcdf components  - give predicor name and predictor file
            nc_file = readnetcdf(pf, py)
            lon, lat, time, pred = nc_file[0], nc_file[1], nc_file[2], \
                nc_file[3]
            
            
            x = startVal
            y = endVal
            
            #looping through individual tide gauges
            #run until dutch_harbour inclusive
            for t in range(x, y):
                
                #the name of the tide gauge - for saving purposes
                # tg = tg_list[t].split('.mat.mat.csv')[0] 
                tg = tg_list[t]
                
                #extract lon and lat data from surge csv file
                print("tide gauge", tg, '\n')
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
                ind_grids.columns = ['lon', 'lat']
                
                #########################################
                #loop through preds#
                #subset predictor on selected grid size
                #########################################

                print("subsetting \n")
                
                #pick up unique values of ind_grids
                latInd = ind_grids.lat.unique()
                lonInd = ind_grids.lon.unique()
                
                count = 1
                for ii in lonInd:
                    print(count, " out of ", len(lonInd))
                    pred_new = subsetter(pred, latInd, ii, time)
                    
                    #create directories to save pred_new
                    os.chdir(csv_path)
                    
                    ####################
                    #tide gauge directory
                    ####################
                    tg_name = tg.split('.mat.mat.csv')[0]
                        
                    try:
                        os.makedirs(tg_name)
                        os.chdir(tg_name) #cd to it after creating it
                    except FileExistsError:
                        #directory already exists
                        os.chdir(tg_name)
                    
                    ####################
                    #predictor directory
                    ####################
                    pred_name  = pf
                    
                    try:
                        os.makedirs(pred_name)
                        os.chdir(pred_name) #cd to it after creating it
                    except FileExistsError:
                        #directory already exists
                        os.chdir(pred_name)
                        
                    
                    ####################
                    #predictorYear directory
                    ####################
                    yr_name = py.split('_')[3]
                    
                    try:
                        os.makedirs(yr_name)
                        os.chdir(yr_name) #cd to it after creating it
                    except FileExistsError:
                        #directory already exists
                        os.chdir(yr_name)
                    
                    
                    ####################
                    #blanket directory
                    ####################
                    
                    blanketName = "blankets"
                        
                    try:
                        os.makedirs(blanketName)
                        os.chdir(blanketName) #cd to it after creating it
                    except FileExistsError:
                        #directory already exists
                        os.chdir(blanketName)
                        
                        
                    #time for saving file
                    print("saving blanket ", ii , "as csv")
                    # save_name = '_'.join([tg_name, pred_name, yr_name])\
                    #     + ".csv"
                    save_name = "blanket"+str(ii)+".csv"
                    pred_new.to_csv(save_name)
                    
                    count+=1

            #return to the predictor directory
            os.chdir(nc_path[pf])
            

extract_data(delta= 3)