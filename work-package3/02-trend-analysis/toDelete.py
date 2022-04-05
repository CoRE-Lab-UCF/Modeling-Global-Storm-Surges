"""  
to check the validity of the percent availability in europe tide gauges
"""
from math import nan
import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy import stats
import statsmodels.api as sm
import pymannkendall as mk
import statsmodels.stats.stattools as stools
from scipy.stats import normaltest
from datetime import datetime


dirHome = {
    "twcr" : "G:\\report\\year-3\\07-Fall-2020\\#3Paper\\data\\"\
        "trend-analysis\\data\\01-twcr\\02-percentiles\\99",
    "era20c" : "G:\\report\\year-3\\07-Fall-2020\\#3Paper\\data\\"\
        "trend-analysis\\data\\02-era20c\\02-percentiles\\"
}


os.chdir(dirHome["twcr"])


def simpleReg(dat, ar):
    """ implements simple linear regression """
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
    
    # print(est2.summary(), "\n")

    # confidence intervals 
    lbCI = est2.conf_int(alpha = 0.05, cols = None).iloc[1,0]
    ubCI = est2.conf_int(alpha = 0.05, cols = None).iloc[1,1]

    # checking pval and existence of 0 between intervals
    if ((lbCI * ubCI) < 0) & (est2.pvalues[1] <= 0.05):
        print("es gibt problem!")

    # get fitted values
    predVal = est2.fittedvalues.copy()
    residual = y - predVal

    return est2.params[1]*1000, est2.pvalues[1], stderr


tgList = os.listdir()

for tg in tgList:
    # print(tg)

    # load data
    dat = pd.read_csv(tg)

    simpleReg(dat, "HAC")


