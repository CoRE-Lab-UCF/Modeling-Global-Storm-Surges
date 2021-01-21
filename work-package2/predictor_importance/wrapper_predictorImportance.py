# -*- coding: utf-8 -*-
"""
Created on Mon Mar 30 17:33:04 2020
Wrapper Method - Predictor Importance
@author: WahlInstall
"""


#importing libraries
from sklearn.datasets import load_boston
import pandas as pd
import numpy as np
import matplotlib
import matplotlib.pyplot as plt
import seaborn as sns
import statsmodels.api as sm
from sklearn.model_selection import train_test_split
from sklearn.feature_selection import RFE
from sklearn.linear_model import LinearRegression
from sklearn.ensemble import RandomForestClassifier, RandomForestRegressor
from sklearn.metrics import roc_auc_score, mean_squared_error, mean_absolute_error
from mlxtend.feature_selection import SequentialFeatureSelector
from sklearn.linear_model import RidgeCV, LassoCV, Ridge, Lasso, LinearRegression

#read data
df = pd.read_csv('zhapo_a-635a-china-uhslc_prcp_D5_1979.csv')
X = df.iloc[:, 3:95]
y = df.iloc[:, 100]

# Train/test split
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.25, random_state=42)

y_train = y_train.ravel()
y_test = y_test.ravel()

# Build RF classifier to use in feature selection
lr = LinearRegression()
rf = RandomForestRegressor(n_estimators = 20)


# Build step forward feature selection
sfs1 = sfs(lr,
           k_features=10,
           forward=True,
           floating=False,
           verbose=2,
           scoring='r2',
           cv=5)

# Perform SFFS
sfs1 = sfs1.fit(X_train, y_train)