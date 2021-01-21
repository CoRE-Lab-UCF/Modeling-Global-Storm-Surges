# -*- coding: utf-8 -*-
"""
Created on Mon May  7 11:39:00 2020

This program is designed to reconstruct
daily max surge using RF

@author: Michael Tadesse
"""
def reconstructRF():
    """
    run KFOLD method for random forest regression 
    """
    #import packages
    import os
    import numpy as np
    import pandas as pd
    #from sklearn import metrics
    #from scipy import stats
    #import seaborn as sns
    #import matplotlib.pyplot as plt
    #from sklearn.model_selection import KFold
    from datetime import datetime
    from sklearn.ensemble import RandomForestRegressor
    from sklearn.decomposition import PCA
    from sklearn.preprocessing import StandardScaler
    
    
   #defining directories    
    dir_in = "/lustre/fs0/home/mtadesse/merraAllLagged"
    dir_out = "/lustre/fs0/home/mtadesse/rfReconstruction"
    surge_path = "/lustre/fs0/home/mtadesse/05_dmax_surge_georef"

    # #load KFOLD result csv file
    # os.chdir('F:\\06_eraint_results\\sonstig')
    # kf_dat = pd.read_csv('eraint_randForest_kfold.csv')
    # #edit the tg names to be usable later on
    # editName = lambda x: x.split('.csv')[0]
    # kf_dat['tg'] = pd.DataFrame(list(map(editName, kf_dat['tg'])), columns= ['tg'])
    
    
    
    #cd to the lagged predictors directory
    os.chdir(dir_in)
    

    x = 48
    y = 49

    #looping through 
    for tg in range(x,y):
        
        os.chdir(dir_in)

        tg_name = os.listdir()[tg]
        print(tg, tg_name)
        
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
        #get the number of PCs used during validation
        # pc_num = kf_dat.loc[kf_dat['tg'] == tg_name]['num_95pcs']
        pca = PCA(0.95)
        pca.fit(X)
        X_pca = pca.transform(X)
        
        
        {# #apply 10 fold cross validation
        # kf = KFold(n_splits=10, random_state=29)
        
        # metric_corr = []; metric_rmse = []; #combo = pd.DataFrame(columns = ['pred', 'obs'])
        # for train_index, test_index in kf.split(X):
        #     X_train, X_test = X_pca[train_index], X_pca[test_index]
        #     y_train, y_test = y['surge'][train_index], y['surge'][test_index]
            
        #     #train regression model
        #     rf = RandomForestRegressor(n_estimator = 50, min_samples_leaf = 1)
        #     lm.fit(X_train, y_train)
            
        #     #predictions
        #     predictions = lm.predict(X_test)
        #     # pred_obs = pd.concat([pd.DataFrame(np.array(predictions)), \
        #     #                       pd.DataFrame(np.array(y_test))], \
        #     #                      axis = 1)
        #     # pred_obs.columns = ['pred', 'obs']
        #     # combo = pd.concat([combo, pred_obs], axis = 0)    
            
        #     #evaluation matrix - check p value
        #     if stats.pearsonr(y_test, predictions)[1] >= 0.05:
        #         print("insignificant correlation!")
        #         continue
        #     else:
        #         #print(stats.pearsonr(y_test, predictions))
        #         metric_corr.append(stats.pearsonr(y_test, predictions)[0])
        #         #print(np.sqrt(metrics.mean_squared_error(y_test, predictions)))
        #         metric_rmse.append(np.sqrt(metrics.mean_squared_error(y_test, predictions)))
            
        
        # #number of years used to train/test model
        # num_years = np.ceil((pred_surge['date'][pred_surge.shape[0]-1] -\
        #                       pred_surge['date'][0]).days/365)
            }
        
        longitude = surge['lon'][0]
        latitude = surge['lat'][0]
        num_pc = X_pca.shape[1] #number of principal components
        # corr = np.mean(metric_corr)
        # rmse = np.mean(metric_rmse)
        
        # print('num_year = ', num_years, ' num_pc = ', num_pc ,'avg_corr = ',\
        #       np.mean(metric_corr), ' -  avg_rmse (m) = ', \
        #       np.mean(metric_rmse), '\n')
        
        #%%
        #surge reconstruction
        pred_for_recon = pred[~pred.isna().any(axis = 1)]
        pred_for_recon = pred_for_recon.reset_index().drop('index', axis = 1)
        
        
        #standardize predictor data
        dat = pred_for_recon.iloc[:,1:]
        scaler = StandardScaler()
        print(scaler.fit(dat))
        dat_standardized = pd.DataFrame(scaler.transform(dat), \
                                        columns = dat.columns)
        pred_standardized = pd.concat([pred_for_recon['date'], dat_standardized], axis = 1)
        
        X_recon = pred_standardized.iloc[:, 1:]
        
        #apply PCA
        pca = PCA(num_pc) #use the same number of PCs used for training
        pca.fit(X_recon)
        X_pca_recon = pca.transform(X_recon)
    
        #%%
        #model preparation
        #defining the rf model with number of trees and minimum leaves
        rf = RandomForestRegressor(n_estimators=50, min_samples_leaf=1, \
                                   random_state = 29)
        rf.fit(X_pca, y)
        
        #get prediction interval
        def pred_ints(model, X_pca_recon, percentile = 95):
            """
            function to construct prediction interval
            taking into account the result of each 
            regression tree
            """
            err_down = [];
            err_up = [];
            preds= [];
            
            for pred in model.estimators_:
                preds.append(pred.predict(X_pca_recon))
            preds = np.vstack(preds).T
            err_down = np.percentile(preds, (100 - percentile)/2., axis = 1, \
                                     keepdims = True)
            err_up = np.percentile(preds, 100 - (100 - percentile)/2., axis =1, \
                                   keepdims = True)
        
            return err_down.reshape(-1), err_up.reshape(-1)
        
        
        #compute 95% prediction intervals
        err_down, err_up = pred_ints(rf, X_pca_recon, percentile = 95);
        #reconstructed surge goes here
        truth = rf.predict(X_pca_recon);
        
        correct = 0.;
        for i, val in enumerate(truth):
            if err_down[i] <= val <= err_up[i]:
                correct +=1
        print(correct*100/len(truth), '\n')
        
        
        #final dataframe
        final_dat = pd.concat([pred_standardized['date'], \
                               pd.DataFrame([truth, err_down, err_up]).T], axis = 1)
        final_dat['lon'] = longitude
        final_dat['lat'] = latitude
        final_dat.columns = ['date', 'surge_reconsturcted', 'pred_int_lower',\
                             'pred_int_upper', 'lon', 'lat']
        
        {#plot - optional
        # time_stamp = lambda x: (datetime.strptime(x, '%Y-%m-%d %H:%M:%S'))
        # final_dat['date'] = pd.DataFrame(list(map(time_stamp, final_dat['date'])), columns = ['date'])
        # surge['date'] = pd.DataFrame(list(map(time_stamp, surge['date'])), columns = ['date'])
        # sns.set_context('notebook', font_scale = 2)
        # plt.figure()
        # plt.plot(final_dat['date'], final_dat['mean'], color = 'green')
        # plt.scatter(surge['date'], surge['surge'], color = 'blue')
        #prediction intervals
        # plt.plot(final_dat['date'], final_dat['obs_ci_lower'], color = 'red',  linestyle = "--", lw = 0.8)
        # plt.plot(final_dat['date'], final_dat['obs_ci_upper'], color = 'red',  linestyle = "--", lw = 0.8)
        #confidence intervals
        # plt.plot(final_dat['date'], final_dat['mean_ci_upper'], color = 'black',  linestyle = "--", lw = 0.8)
        # plt.plot(final_dat['date'], final_dat['mean_ci_lower'], color = 'black',  linestyle = "--", lw = 0.8)
        }

        #save df as cs - in case of interruption
        os.chdir(dir_out)
        final_dat.to_csv(tg_name)
        
        #cd to dir_in
        os.chdir(dir_in)
        
        
reconstructRF()
        
        
        
        
        
        
        
        
        
        
        
        
        