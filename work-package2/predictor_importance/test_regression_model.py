# -*- coding: utf-8 -*-
"""
Created on Wed Apr  8 14:27:23 2020

Testing regression model

@author: Michael Tadesse
"""


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split



time_str = lambda x: str(datetime.strptime(x, '%Y-%m-%d'))
surge_time = pd.DataFrame(list(map(time_str, surge['ymd'])))
surge_new = pd.concat([surge_time, surge['surge']], axis = 1)
pred_surge = pd.merge(pred, surge_new, on='date', how='right')
pred_surge.drop('Unnamed: 0', axis = 1, inplace = True)

X = pred_surge.iloc[:,1:-1]
y = pred_surge['surge']

X_train, X_test, y_train, y_test, = \
    train_test_split(X,y, test_size = 0.3, random_state = 101)


#import linear regression model
from sklearn.linear_model import LinearRegression
lm = LinearRegression() #creating a linear regression object (instantiating)
lm.fit(X_train, y_train)

#evaluate model
print(lm.intercept_)

cdf = pd.DataFrame(lm.coef_, X.columns, columns = ['Coeff']) # display in a table format
lm.coef_ #prints the regression coefficients

#Predictions
preidicions = lm.predict(X_test)
preidicions
plt.scatter(y_test,preidicions) # scatter plot
sns.distplot((y_test - preidicions)) # plot residuals

#Evaluation metircs
from sklearn import metrics
metrics.mean_absolute_error(y_test,preidicions)
metrics.mean_squared_error(y_test, preidicions)
np.sqrt(metrics.mean_squared_error(y_test, preidicions))
metrics.r2_score(y_test, preidicions)
# metrics.matthews_corrcoef(y_test, preidicions)









