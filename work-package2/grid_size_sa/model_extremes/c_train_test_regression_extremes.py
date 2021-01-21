# -*- coding: utf-8 -*-
"""
Created on Thu Apr 17 14:29:00 2020

Apply PCA on data set 
Train and Test linear regression model 

@author: Michael Tadesse
"""
import pandas as pd
import numpy as np
from sklearn import metrics
from scipy import stats
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt


def lr_reg(X_train, X_test, y_train, y_test):

    #train regression model
    lm = LinearRegression()
    lm.fit(X_train, y_train)
    
    
    #getting 95th and 99th %ile observed surges
    y95 = y_test.quantile(0.95)
    y99 = y_test.quantile(0.99)
    
    y_test95 = pd.DataFrame(y_test[y_test >=y95])
    y_test95.columns = ['surge_obs']
    y_test95.reset_index(inplace = True)
    y_test99 = pd.DataFrame(y_test[y_test >=y99])
    y_test99.columns = ['surge_obs']
    y_test99.reset_index(inplace = True)

    
    
    #predictions
    predictions = pd.DataFrame(lm.predict(X_test), columns = ['surge_pred'])
    predictions.reset_index(inplace = True)
    # plt.scatter(y_test, predictions)

    #filter out corresponding prediction values to the percentile surges
    y_test = pd.DataFrame(y_test)
    #reset index to get the index of y_test to match it with percentile surges
    y_test.reset_index(inplace = True)
    y_test95_merge = pd.merge(y_test, y_test95, on = 'index', how = 'left')
    y_test95_merge.drop('surge', axis = 1, inplace = True)
    
    #drop nans
    nan95 = y_test95_merge[y_test95_merge['surge_obs'].isna()]
    y_test95_new = y_test95_merge.drop(nan95.index)
    y_test95_new.drop('index', axis = 1, inplace = True)
    y_test95_new.reset_index(inplace = True)
    
    
    y_test99_merge = pd.merge(y_test, y_test99, on = 'index', how = 'left')
    y_test99_merge.drop('surge', axis = 1, inplace = True)
    
    #drop nans
    nan99 = y_test99_merge[y_test99_merge['surge_obs'].isna()]
    y_test99_new = y_test99_merge.drop(nan99.index)
    y_test99_new.drop('index', axis = 1, inplace = True)
    y_test99_new.reset_index(inplace = True)
    
    #merge these to predictions to filter 
    validation95 = pd.merge(predictions, y_test95_new, on= 'index', how = 'right')
    validation99 = pd.merge(predictions, y_test99_new, on= 'index', how = 'right')

    
    #evaluation matrix
    #check if there is at least two rows of data
    if validation95.shape[0] < 2:
        corrn95 = 'nan'
        rmse95 = 'nan'
    #check if the correlation is significant
    elif stats.pearsonr(validation95['surge_obs'], validation95['surge_pred'])[1] >= 0.05:
        corrn95 = 'nan'
        rmse95 = 'nan'
    else:
        rmse95 = np.sqrt(metrics.mean_squared_error(validation95['surge_obs'], \
                                                    validation95['surge_pred']))
        corrn95 = stats.pearsonr(validation95['surge_obs'], validation95['surge_pred'])
        
        
    if validation99.shape[0] < 2:
        corrn99 = 'nan'
        rmse99 = 'nan'
    #check if the correlation is significant
    elif stats.pearsonr(validation99['surge_obs'], validation99['surge_pred'])[1] >= 0.05:
        corrn99 = 'nan'
        rmse99 = 'nan'
    else:
       rmse99 = np.sqrt(metrics.mean_squared_error(validation99['surge_obs'], \
                                                validation99['surge_pred']))
       corrn99 = stats.pearsonr(validation99['surge_obs'], validation99['surge_pred'])
    

    
    print('correlation 95%ile = ',corrn95, 'RMSE (m) 95%ile = ',rmse95)
    print('correlation 99%ile = ',corrn99, 'RMSE (m) 99%ile = ',rmse99, '\n')

    return corrn95, rmse95, corrn99, rmse99