# -*- coding: utf-8 -*-
"""
Created on Wed May  6 10:46:14 2020

------------------------------------------------------------------
This function computes the prediction interval 
for a random forest regression

adopted from
https://blog.datadive.net/prediction-intervals-for-random-forests/
------------------------------------------------------------------

@author: Michael Tadesse
"""
from sklearn.ensemble import RandomForestRegressor
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

#first cross validate model using the RandomForestRegressor
# rf = RandomForestRegressor(n_estimators=1000, min_samples_leaf=1)
# rf.fit(X[idx[:trainsize]], Y[idx[:trainsize]])

#------------------------------------------------------------------------------
#proabably faster method
def pred_ints(model, X, percentile = 95):
    err_down = [];
    err_up = [];
    preds= [];
    
    for pred in model.estimators_:
        preds.append(pred.predict(X))
    preds = np.vstack(preds).T
    err_down = np.percentile(preds, (100 - percentile)/2., axis = 1, \
                             keepdims = True)
    err_up = np.percentile(preds, 100 - (100 - percentile)/2., axis =1, \
                           keepdims = True)

    return err_down.reshape(-1), err_up.reshape(-1)
#------------------------------------------------------------------------------

#compute 95% prediction intervals
err_down, err_up = pred_ints(rf, X, percentile = 95);
#reconstructed surge goes here
truth = rf.predict(X_pca);

correct = 0.;
for i, val in enumerate(truth):
    if err_down[i] <= val <= err_up[i]:
        correct +=1
print(correct*100/len(truth))
#------------------------------------------------------------------------------
#plotting results
plt.figure(figsize = (16,12));
plt.scatter(test, truth, color = 'green')
plt.errorbar(test, truth, yerr= pd.Series(err_up) - \
             pd.Series(err_down), ecolor= 'blue', \
                 alpha = 0.6, capsize = 20, ls = '')
    
    

    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    