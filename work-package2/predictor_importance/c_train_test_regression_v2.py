# -*- coding: utf-8 -*-
"""
Created on Mon Apr 13 10:28:07 2020

Apply PCA on data set 
Train and Test linear regression model 

@author: Michael Tadesse
"""
import numpy as np
from sklearn import metrics
from scipy import stats
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt


def lr_reg(X_train, X_test, y_train, y_test):

    #train regression model
    lm = LinearRegression()
    lm.fit(X_train, y_train)
    
    
    #predictions
    predictions = lm.predict(X_test)
    plt.scatter(y_test, predictions)
    
    #evaluation matrix
    rmse = np.sqrt(metrics.mean_squared_error(y_test, predictions))
    corrn = stats.pearsonr(y_test, predictions)
    print('correlation = ',corrn, 'RMSE (m) = ',rmse, '\n')
    
    return corrn, rmse