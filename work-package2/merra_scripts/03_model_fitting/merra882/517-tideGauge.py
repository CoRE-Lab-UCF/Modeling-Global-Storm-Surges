# -*- coding: utf-8 -*-
"""
Created on Mon May  4 15:51:30 2020

This program is designed to validate a multiple
linear regression model by using the KFOLD method


@author: Michael Tadesse
"""
import os
import numpy as np
import pandas as pd
from sklearn import metrics
from scipy import stats
from datetime import datetime
from sklearn.linear_model import LinearRegression
from sklearn.decomposition import PCA
from sklearn.model_selection import KFold
from sklearn.preprocessing import StandardScaler

def validate():
    """
    run KFOLD method for regression 
    """
    #defining directories    
    dir_in = "/lustre/fs0/home/mtadesse/merraAllLagged"
    dir_out = "/lustre/fs0/home/mtadesse/merraLRValidation"
    surge_path = "/lustre/fs0/home/mtadesse/05_dmax_surge_georef"

    
    #cd to the lagged predictors directory
    os.chdir(dir_in)
    
    
    x = 517
    y = 518
    
    #empty dataframe for model validation
    df = pd.DataFrame(columns = ['tg', 'lon', 'lat', 'num_year', \
                                 'num_95pcs','corrn', 'rmse'])
    
    #looping through 
    for tg in range(x,y):
        
        os.chdir(dir_in)

        tg_name = os.listdir()[tg]
        print(tg, tg_name)
        
        ##########################################
        #check if this tg is already taken care of
        ##########################################
        os.chdir(dir_out)
        if os.path.isfile(tg_name):
            return "file already analyzed!"
        
        
        os.chdir(dir_in)

        #load predictor
        pred = pd.read_csv(tg_name)
        pred.drop('Unnamed: 0', axis = 1, inplace = True)
        
        #add squared and cubed wind terms (as in WPI model)
        pickTerms = lambda x: x.startswith('wnd')
        wndTerms = pred.columns[list(map(pickTerms, pred.columns))]
        wnd_sqr = pred[wndTerms]**2
        wnd_cbd = pred[wndTerms]**3
        pred = pd.concat([pred, wnd_sqr, wnd_cbd], axis = 1)

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
        
        #remove duplicated surge rows
        surge.drop(surge[surge['ymd'].duplicated()].index, axis = 0, inplace = True)
        surge.reset_index(inplace = True)
        surge.drop('index', axis = 1, inplace = True)
        
        
        #adjust surge time format to match that of pred
        time_str = lambda x: str(datetime.strptime(x, '%Y-%m-%d'))
        surge_time = pd.DataFrame(list(map(time_str, surge['ymd'])), columns = ['date'])
        time_stamp = lambda x: (datetime.strptime(x, '%Y-%m-%d %H:%M:%S'))
        surge_new = pd.concat([surge_time, surge[['surge', 'lon', 'lat']]], axis = 1)
    
        #merge predictors and surge to find common time frame
        pred_surge = pd.merge(pred_standardized, surge_new.iloc[:,:2], on='date', how='right')
        pred_surge.sort_values(by = 'date', inplace = True)
        
        #find rows that have nans and remove them
        row_nan = pred_surge[pred_surge.isna().any(axis =1)]
        pred_surge.drop(row_nan.index, axis = 0, inplace = True)
        pred_surge.reset_index(inplace = True)
        pred_surge.drop('index', axis = 1, inplace = True)
        
        
        #in case pred and surge don't overlap
        if pred_surge.shape[0] == 0:
            print('-'*80)
            print('Predictors and Surge don''t overlap')
            print('-'*80)
            continue
        
     
        pred_surge['date'] = pd.DataFrame(list(map(time_stamp, \
                                                   pred_surge['date'])), \
                                          columns = ['date'])
        
        #prepare data for training/testing
        X = pred_surge.iloc[:,1:-1]
        y = pd.DataFrame(pred_surge['surge'])
        y = y.reset_index()
        y.drop(['index'], axis = 1, inplace = True)
        
        #apply PCA
        pca = PCA(.95)
        pca.fit(X)
        X_pca = pca.transform(X)
        
        #apply 10 fold cross validation
        kf = KFold(n_splits=10, random_state=29)
        
        metric_corr = []; metric_rmse = []; #combo = pd.DataFrame(columns = ['pred', 'obs'])
        for train_index, test_index in kf.split(X):
            X_train, X_test = X_pca[train_index], X_pca[test_index]
            y_train, y_test = y['surge'][train_index], y['surge'][test_index]
            
            #train regression model
            lm = LinearRegression()
            lm.fit(X_train, y_train)
            
            #predictions
            predictions = lm.predict(X_test)
            # pred_obs = pd.concat([pd.DataFrame(np.array(predictions)), \
            #                       pd.DataFrame(np.array(y_test))], \
            #                      axis = 1)
            # pred_obs.columns = ['pred', 'obs']
            # combo = pd.concat([combo, pred_obs], axis = 0)    
            
            #evaluation matrix - check p value
            if stats.pearsonr(y_test, predictions)[1] >= 0.05:
                print("insignificant correlation!")
                continue
            else:
                print(stats.pearsonr(y_test, predictions))
                metric_corr.append(stats.pearsonr(y_test, predictions)[0])
                print(np.sqrt(metrics.mean_squared_error(y_test, predictions)))
                metric_rmse.append(np.sqrt(metrics.mean_squared_error(y_test, predictions)))
            
        
        #number of years used to train/test model
        num_years = (pred_surge['date'][pred_surge.shape[0]-1] -\
                             pred_surge['date'][0]).days/365
        longitude = surge['lon'][0]
        latitude = surge['lat'][0]
        num_pc = X_pca.shape[1] #number of principal components
        corr = np.mean(metric_corr)
        rmse = np.mean(metric_rmse)
        
        print('num_year = ', num_years, ' num_pc = ', num_pc ,'avg_corr = ',np.mean(metric_corr), ' -  avg_rmse (m) = ', \
              np.mean(metric_rmse), '\n')
        
        #original size and pca size of matrix added
        new_df = pd.DataFrame([tg_name, longitude, latitude, num_years, num_pc, corr, rmse]).T
        new_df.columns = ['tg', 'lon', 'lat', 'num_year', \
                                 'num_95pcs','corrn', 'rmse']
        df = pd.concat([df, new_df], axis = 0)
        
        
        #save df as cs - in case of interruption
        os.chdir(dir_out)
        df.to_csv(tg_name)
        
        #cd to dir_in
        os.chdir(dir_in)
        
        
#run script
validate()
        
        
        
        
        
        
        
        
        
        
        
        
        