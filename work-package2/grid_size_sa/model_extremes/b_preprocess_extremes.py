# -*- coding: utf-8 -*-
"""
Created on Thu Apr 17 14:29:00 2020

--------------------------------------------------------------------
This script standardizes the predictor data 
and trains a linear regression model

This script might be used for reconstructing surges also

*Notice that K-Fold CV was not used and thus reconstruction cannot 
be done here - Adjust script for later use - 
if reconstruction is needed
--------------------------------------------------------------------

@author: Michael Tadesse
"""

import os 
from datetime import datetime
import pandas as pd
from sklearn.decomposition import PCA
from c_train_test_regression_extremes import lr_reg
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split

    
#defining directories    
dir_in = 'F:\\03_eraint_lagged_predictors'
dir_out = 'F:\\04_eraint_lrreg_validation\\extremes'
surge_path = 'F:\\05_dmax_surge_georef'
    

def preprocess(folder_name):
    """
    This function loads lagged predictors - loads surge time series 
    standardizes predictors - prepares the predictors belonging to each case
    prepare data for training/testing
    
    
    output: training and testing predictor and predictand data
    """
    
    #load predictors
    #cd to the lagged predictors directory
    os.chdir(os.path.join(dir_in, folder_name))
    
    #empty dataframe for model validation
    df = pd.DataFrame(columns = ['tg', 'lon', 'lat', 'corrn95', 'rmse95', 'corrn99', 'rmse99',\
                          'original_size', 'pca_size'])
    
    #looping through TGs
    for tg in range(len(os.listdir())):
        
        os.chdir(os.path.join(dir_in, folder_name))
        
        tg_name = os.listdir()[tg]
        print(tg, folder_name, tg_name)

        #load predictor
        pred = pd.read_csv(tg_name)
        pred.drop('Unnamed: 0', axis = 1, inplace = True)
        
        #standardize predictor data
        dat = pred.iloc[:,1:]
        scaler = StandardScaler()
        print(scaler.fit(dat))
        dat_standardized = pd.DataFrame(scaler.transform(dat), \
                                        columns = dat.columns)
        pred_standardized = pd.concat([pred['date'], dat_standardized], axis = 1)
        
        #load surge data
        os.chdir(surge_path)
        surge = pd.read_csv(tg_name)
        surge.drop('Unnamed: 0', axis = 1, inplace = True)
        
        
        #adjust surge time format to match that of pred
        time_str = lambda x: str(datetime.strptime(x, '%Y-%m-%d'))
        surge_time = pd.DataFrame(list(map(time_str, surge['ymd'])), columns = ['date'])
        surge_new = pd.concat([surge_time, surge[['surge', 'lon', 'lat']]], axis = 1)
    
        #merge predictors and surge to find common time frame
        pred_surge = pd.merge(pred_standardized, surge_new.iloc[:,:2], on='date', how='right')
        pred_surge.sort_values(by = 'date', inplace = True)
        
        #find rows that have nans and remove them
        row_nan = pred_surge[pred_surge.isna().any(axis =1)]
        pred_surge.drop(row_nan.index, axis = 0, inplace = True)
        
       
        #in case pred and surge don't overlap
        if pred_surge.shape[0] == 0:
            print('-'*80)
            print('Predictors and Surge don''t overlap')
            print('-'*80)
            continue
        
        """
        #remove predictors of choice - as per chosen case
        test = lambda x: x.startswith(ii)
        for ii in pred_case[case]:
            print(case,'- now removing: ' , ii)
            remove_cols = pred_surge.columns[list(map(test, pred_surge.columns))]
            # pred_remove = pred_surge.loc[:, remove_cols]
            pred_surge = pred_surge.drop(remove_cols, axis = 1)
        """
        
        
        #split data to training and testing 
        X = pred_surge.iloc[:,1:-1]
        y = pred_surge['surge']
        
        
                
        #make an instance of the model - explained variance == 95%
        pca = PCA(.95)
        pca.fit(X)
        X_pca = pca.transform(X)

        #adding original and post-pca matrix size
        sz_orgn = X.shape[1]
        sz_pca = X_pca.shape[1]
        
        print('pca ', sz_orgn, '-', sz_pca)
        
        
        X_train, X_test, y_train, y_test, = \
            train_test_split(X_pca,y, test_size = 0.2, random_state = 101)

        #model validation
        [corrn95, rmse95, corrn99, rmse99] = lr_reg(X_train, X_test, y_train, y_test)
        lon = surge.lon[0]
        lat = surge.lat[0]
         
        
        #original size and pca size of matrix added
        new_df = pd.DataFrame([tg_name, lon, lat, corrn95, rmse95, corrn99, \
                               rmse99, sz_orgn, sz_pca]).T
        new_df.columns = ['tg', 'lon', 'lat', 'corrn95', 'rmse95', 'corrn99', 'rmse99',\
                          'original_size', 'pca_size']
        df = pd.concat([df, new_df], axis = 0)
        # print(df)
        
        
        #save df as csv - in case of interruption
        os.chdir(os.path.join(dir_out, folder_name))
        df.to_csv('eraint_lrreg_validation.csv')
            

        #cd to dir_in
        os.chdir(os.path.join(dir_in, folder_name))

    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    