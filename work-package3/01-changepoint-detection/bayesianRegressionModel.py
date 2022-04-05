# -*- coding: utf-8 -*-
"""
Created on Mon Nov  2 19:20:45 2020

Simple Bayesian Linear Regression Model
https://docs.pymc.io/notebooks/getting_started.html
@author: PyMC3
"""

import arviz as az
import matplotlib.pyplot as plt
import numpy as np
import pymc3 as pm


# %config InlineBackend.figure_format = 'retina'
# Initialize random number generator
RANDOM_SEED = 8927
np.random.seed(RANDOM_SEED)
az.style.use('arviz-darkgrid')


# True parameter values
alpha, sigma = 1, 1
beta = [1, 2.5]

# Size of dataset
size = 100

# Predictor variable
X1 = np.random.randn(size)
X2 = np.random.randn(size) * 0.2

# Simulate outcome variable
Y = alpha + beta[0] * X1 + beta[1] * X2 + np.random.randn(size) * sigma


## Model Specification

#create a Model object which is a container for 
#the model random variables
basic_model = pm.Model()

#create context manager - include all statements
#until the indented block ends
with basic_model:
    # Priors for unknown model parameters
    alpha = pm.Normal("alpha", mu=0, sigma=10)
    beta = pm.Normal("beta", mu=0, sigma=10, shape=2)
    sigma = pm.HalfNormal("sigma", sigma=1)
    
    # Expected value of outcome
    mu = alpha + beta[0] * X1 + beta[1] * X2
    
    # Likelihood (sampling distribution) of observations
    Y_obs = pm.Normal("Y_obs", mu=mu, sigma=sigma, observed=Y)