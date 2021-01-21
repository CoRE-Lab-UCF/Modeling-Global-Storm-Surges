# -*- coding: utf-8 -*-
"""
Created on Thu May  7 15:25:34 2020

This script compares the kfold validation 
of the linear regression and Random Forest 
and chooses the model that should be used to 
reconstruct the surge for the given tide gauge

@author: Michael Tadesse
"""


def chooseModel():
    
    #import packages
    import os
    import pandas as pd
    import shutil
    
    #define directories
    dir_in = 'G:\\05_era5\\06_era5_results'
    dir_out_surge = 'G:\\05_era5\\08_era5_surge_reconstruction\\bestReconstruction\\surgeReconstructed'
   #dir_out_metadata = 'F:\\08_eraint_surge_reconstruction\\bestReconstruction\\metaData'
    
    #read kfold validation csvs
    os.chdir(dir_in)
    lr = pd.read_csv('erafiveMLRValidation.csv')
    rf = pd.read_csv('erafiveRFValidation.csv')
    
    #merge the two csvs
    comp = pd.merge(lr, rf, on = 'tg', how = 'right')
    comp = comp[['tg', 'lon_x', 'lat_x', 'num_year_x', 'num_95pcs_x',
       'corrn_x', 'rmse_x', 'corrn_y', 'rmse_y']]
    comp.columns = ['tg', 'lon', 'lat', 'num_year', 'num_95pcs',
       'corrn_lr', 'rmse_lr', 'corrn_rf', 'rmse_rf']
    comp['bestModel'] = 'nan'
    
    #filter comparison (lr/rf) based on RMSE results(as it says more about
    #the model accuracy than correlation)
    for ii in comp[comp['rmse_lr'] <= comp['rmse_rf']].index:
        comp['bestModel'][ii] = 'MLR'
    for jj in comp[comp['rmse_lr'] > comp['rmse_rf']].index:
        comp['bestModel'][jj] = 'RF'
    for kk in comp[comp['rmse_lr'].isna()].index:
        comp['bestModel'][kk] = 'RF'
    for rr in comp[comp['rmse_rf'].isna()].index:
        comp['bestModel'][rr] = 'MLR'
        
    #copy files to bestReconstruction based on RMSE value
    for ii in range(len(comp)):
        if comp['bestModel'][ii] == 'MLR':
            print(comp['bestModel'][ii])
            os.chdir('G:\\05_era5\\08_era5_surge_reconstruction\\mlr')
            source = os.path.join(os.path.abspath(os.getcwd()), comp['tg'][ii])
            destination = os.path.join(dir_out_surge, comp['tg'][ii])
            
            try:
                shutil.copyfile(source, destination)
                #print("file copied successfully!")
            except shutil.SameFileError:
                print("source and destination represent the same file")
            except:
                print("error occured while copying file")
        else:
            print(comp['bestModel'][ii])
            comp['bestModel'][ii]
            os.chdir('G:\\05_era5\\08_era5_surge_reconstruction\\rf')
            source = os.path.join(os.path.abspath(os.getcwd()), comp['tg'][ii])
            destination = os.path.join(dir_out_surge, comp['tg'][ii])
            
            try:
                shutil.copyfile(source, destination)
                #print("file copied successfully!")
            except shutil.SameFileError:
                print("source and destination represent the same file")
            except:
                print("error occured while copying file")
        
        
        
        
        
        
        
        
        
        
        
        
        