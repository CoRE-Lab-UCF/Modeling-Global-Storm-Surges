# -*- coding: utf-8 -*-
"""
Created on Fri Mar 23 11:48:00 2020

@author: Michael Tadesse
"""
import time
import os 
import pandas as pd
from d_define_grid import Coordinate, findPixels, findindx
#from surgets import add_date
#from e_compiler import compile_predictors
from c_read_netcdf import readnetcdf
from f_subset import subsetter

def extract_data(delta):
    """
    This is the master function that calls subsequent functions
    to extract uwnd, vwnd, slp, sst, prcp for the specified
    tide gauges
    
    delta: distance (in degrees) from the tide gauge
    """
    
    print('Delta =  {}'.format(delta), '\n')
    
    #defining the folders for predictors
    nc_path = {'prcp' : "D:\data\era_interim\era_interim_netcdf\prcp", \
               'slp' : "D:\data\era_interim\era_interim_netcdf\slp",\
               'sst' : "D:\data\era_interim\era_interim_netcdf\sst", \
               "wnd_u": "D:\data\era_interim\era_interim_netcdf\wnd_u",\
               'wnd_v' : "D:\data\era_interim\era_interim_netcdf\wnd_v"}
    surge_path = "D:\data\obs_surge"
    csv_path = "D:\data\era_interim\eraint_localized"
    
    #cd to the obs_surge dir to get TG information
    os.chdir(surge_path)
    tg_list = os.listdir()
    
    
    #looping through the predictor folders
    #prcp; slp; sst; uwnd; vwnd
    for pf in nc_path.keys():
        
        print(pf, '\n')
        os.chdir(nc_path[pf])
        
        #looping through the years of the chosen predictor
        for py in os.listdir():
            
            os.chdir(nc_path[pf]) #back to the predictor folder
            print(py, '\n')
            #get netcdf components  - give predicor name and predictor file
            nc_file = readnetcdf(pf, py)
            lon, lat, time, pred = nc_file[0], nc_file[1], nc_file[2], \
                nc_file[3]
            
            
            #looping through individual tide gauges
            for t in range(0, len(tg_list)):
                
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
                
                
                #subset predictor on selected grid size
                pred_new = subsetter(pred, ind_grids, time)
                
                #create directories to save pred_new
                os.chdir(csv_path)
                
                #tide gauge directory
                tg_name = tg.split('.mat.mat.csv')[0]
                
                try:
                    os.makedirs(tg_name)
                    os.chdir(tg_name) #cd to it after creating it
                except FileExistsError:
                    #directory already exists
                    os.chdir(tg_name)
                
                #delta directory
                del_name = 'D' + str(delta)
                
                try:
                    os.makedirs(del_name)
                    os.chdir(del_name) #cd to it after creating it
                except FileExistsError:
                    #directory already exists
                    os.chdir(del_name)
                
                #predictor directory
                pred_name  = pf
                
                try:
                    os.makedirs(pred_name)
                    os.chdir(pred_name) #cd to it after creating it
                except FileExistsError:
                    #directory already exists
                    os.chdir(pred_name)
                
                #save as csv
                yr_name = py.split('_')[3]
                save_name = '_'.join([tg_name, pred_name, del_name,yr_name])\
                    + ".csv"
                pred_new.to_csv(save_name)
            
            #return to the predictor directory
            os.chdir(nc_path[pf])
                        
        