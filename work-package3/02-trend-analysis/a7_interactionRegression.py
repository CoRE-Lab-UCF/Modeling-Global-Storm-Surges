import os
import os.path
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy import stats
import statsmodels.stats.stattools as stools
import statsmodels.api as sm
from datetime import datetime



def getDummy(dat):
    """  
    get binary value for categorical variable
    """
    # get dummies 
    
    return pd.get_dummies(dat['data'], drop_first = False)
    # dat['dataDummy'] = pd.get_dummies(dat['data'], drop_first = True)
    # dat['interaction'] = dat['Input']*dat['conditionVar']
    # print(dat)

    # simpleReg(dat, "")



# simple linear regression with Newey-West estimator
def simpleReg(dat, ar):
    """ 
    implements simple linear regression 
    extracts coefficients 
    """
    x = dat[['year', 'dummy', 'interaction']]
    y = dat['value']

    x2 = sm.add_constant(x)
    est = sm.OLS(y, x2)

    if ar == "HAC":
        lag = int(4*(len(dat)*0.01)**(2/9))
        # print("lag = ", lag)
        est2 = est.fit(cov_type = 'HAC', cov_kwds={'maxlags':lag}) # adding heteroscedasticity-consistent standard errors
        stderr = est2.bse[1] # stderr for trend coefficient
    else:
        est2 = est.fit() # default - without heteroscedasticity checking
        stderr = est2.bse[1] # stderr for trend coefficient
    
    print(est2.summary())
    print(est2.pvalues[3]) # interaction term pval

    # get fitted values
    predVal = est2.fittedvalues.copy()
    residual = y - predVal

    durbinStat = stools.durbin_watson(residual)
    # print(durbinStat)

    return est2.pvalues[3]
