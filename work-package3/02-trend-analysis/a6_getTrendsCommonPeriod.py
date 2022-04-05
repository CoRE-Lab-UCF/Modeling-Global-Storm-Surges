"""  
Created on Fri Jul 21 10:32:00 2021

this script computes trends for observed surge - 
twcr recon - era20c recon for a common period

@author: Michael Tadesse

"""

import os
import os.path
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy import stats
import statsmodels.stats.stattools as stools
import statsmodels.api as sm
from datetime import datetime


def getTrends(obs, twcr, era20c, alpha):
    """         
    get trend values for each product
    """
    obsTrend, obsPval = simpleReg(obs, "HAC") 
    twcrTrend, twcrPval = simpleReg(twcr, "HAC") 
    era20cTrend, era20cPval = simpleReg(era20c, "HAC") 

    # only take signifcant trends
    if obsPval > alpha:
        obsTrend = 'nan'

    if twcrPval > alpha:
        twcrTrend = 'nan'

    if era20cPval > alpha:
        era20cTrend = 'nan'

    return obsTrend, twcrTrend, era20cTrend


# simple linear regression with Newey-West estimator
def simpleReg(dat, ar):
    """ 
    implements simple linear regression 
    extracts coefficients 
    """
    x = dat['year']
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

    # get fitted values
    predVal = est2.fittedvalues.copy()
    residual = y - predVal

    durbinStat = stools.durbin_watson(residual)
    # print(durbinStat)

    return est2.params[1]*1000, est2.pvalues[1]