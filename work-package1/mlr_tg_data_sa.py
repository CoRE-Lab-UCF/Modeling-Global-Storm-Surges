# -*- coding: utf-8 -*-
"""
Created on Fri Jan 17 09:47:02 2020
-----------------------------------------
To test the sensitivity of model accuracy 
with data availability - linear regression
-----------------------------------------
@author: Michael Tadesse
"""
import os
import pandas as pd
import numpy as np
from sklearn import metrics
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression


os.chdir('D:\\data\\era_interim_pred_and_surge')
tg_lst = os.listdir()

ind = 0;
err_lst = pd.DataFrame(columns =['gauge', 'year', 'corr', 'rmse']); 
for ii in tg_lst:
    
    print(ii, '\n')
    
    #load data first
    dat_org = pd.read_csv(ii)
    
    yr_ind = 0; dat = pd.DataFrame(); 
    
    
    #run until there is one year left
    while yr_ind <= dat_org.shape[0] - (365*4):
        
        print(ind, yr_ind)
        #subset the data by removing a year time ser
        dat = dat_org.tail(dat_org.shape[0] - yr_ind)
        
        #predictors
        x = dat.iloc[:, 2:dat.shape[1]-1];
        
        #predictand
        y = dat.iloc[:,dat.shape[1]-1]
        #split to training and testing
        x_train, x_test, y_train, y_test, = \
            train_test_split(x,y, test_size = 0.3, random_state = 101)
            
        #linear regression model
        lm = LinearRegression() 
        lm.fit(x_train, y_train)   
        
            
        #Predictions
        preidicions = lm.predict(x_test)
        
        #Evaluation metircs
        #metrics.mean_absolute_error(y_test,preidicions)
        #metrics.mean_squared_error(y_test, preidicions)
        rmse = np.sqrt(metrics.mean_squared_error(y_test, preidicions))
        corrl = np.corrcoef(y_test, preidicions)[1,0]
        # metrics.r2_score(y_test, preidicions)
        
        err_lst.loc[ind,'gauge'] = ii
        err_lst.loc[ind,'year'] = (dat_org.shape[0] - yr_ind)/(365*4)
        err_lst.loc[ind,'corr'] = corrl
        err_lst.loc[ind,'rmse'] = rmse
    
        ind += 1
        yr_ind += (365*4)
        

#changing corr and rmse to be floats

err_lst['corr'] = [float(x) for x in err_lst['corr']]
err_lst['rmse'] = [float(x) for x in err_lst['rmse']]

#plotting 
sns.set_context('notebook', font_scale=2)
plt.figure(figsize = (15,10))
g = sns.lineplot(x= 'year', y = 'corr', hue= "gauge", data = err_lst)
g.legend().remove()

plt.figure(figsize = (15,10))
h = sns.lineplot(x= 'year', y = 'rmse', hue= "gauge", data = err_lst)
h.legend().remove()

 






