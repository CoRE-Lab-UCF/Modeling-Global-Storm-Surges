"""  
Created on Fri Aug 06 10:11:00 2021
Modified on Wed Jan 26 12:37:00 2022

this script computes regional trends for 
twcr recon - era20c recon by incorporating the heteroscedasticity 
and autocorrelation robus covariance matrix (Newey-West)

trends can be computed for different years
1875 - present, 1900 - present etc 

@author: Michael Getachew Tadesse

"""

from math import nan
import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy import stats
import statsmodels.api as sm
import statsmodels.stats.stattools as stools
from scipy.stats import normaltest
from datetime import datetime

# pick percentile + adjust directory
dirHome = "G:\\report\\year-3\\07-Fall-2020\\#3Paper\\data\\"\
    "trend-analysis\\data\\04-regionalStormFreq_v3"

dirOut = "G:\\report\\year-3\\07-Fall-2020\\#3Paper\\data\\"\
    "trend-analysis\\data\\05-regionalStormFreqTrends_v3"

# write the code to accomodate recon + percentile

def getTrends(year, *args):
    """ 
    this function computes the trends after 
    args: HAC - heteroskedasticity-autocorrelation robust covariance
    maxlag: integer - number of lags
    year: starting year to compute trends {1875, 1900, 1950}
    """
    os.chdir(dirHome)

    tgList = os.listdir()

    # create empty dataframe
    df = pd.DataFrame(columns = ['tg', 'normality', 
                'trend(storms/year)', 'intercept',
                        'pval', 'dw', 'stderr'])

    for tg in tgList:
        print(tg)

        # load data
        dat = pd.read_csv(tg)

        ##################################
        # check year
        print(dat)
        yr = dat['year'][0]
        if yr > year:
            print("{} - not enough data".format(tg))
            continue
        else:
            dat = dat[dat['year'] >= year]
            # print(dat)
        ##################################

        # fit trends 

        if args:
            for ar in args:
                annualTrend, intercept,  pval, durbinStat, stderr = simpleReg(dat, ar)
        else:
            ar = ""
            annualTrend, intercept, pval, durbinStat, stderr = simpleReg(dat, ar)
        # print(tg, " - ", dubrinWatson)
        newDf = pd.DataFrame([tg, True, annualTrend, intercept, pval, durbinStat, stderr]).T
        newDf.columns = ['tg', 'normality', 'trend(storms/year)', 
                                'intercept', 'pval', 'dw', 'stderr']
        df = pd.concat([df, newDf])
    

    # check significance at 95% confidence level
    df['significance'] = (~df['pval'].isnull()) & (df['pval'] <= 0.05)

    # print(df)

    # save file
    os.chdir(dirOut)
    df.to_csv("regionalTrends_{}_{}.csv".format(year, ar)) # adding heteroscedasticity-consistent standard errors
    
def checkNormality(x):
    """ checks normality of the time series """
    shapiro_test = stats.shapiro(x) # shapiro test
    stat, p = normaltest(x) # D'Agostino test

    # print("shapiro pvalue = {}".format(shapiro_test.pvalue))
    # print("D'Agostino pvalue = {} \n".format(p))

    return shapiro_test.pvalue, p

def simpleReg(dat, ar):
    """ implements simple linear regression """
    x = dat['year']
    y = dat['avg']

    x2 = sm.add_constant(x)
    est = sm.OLS(y, x2)
    if ar == "HAC":
        lag = int(4*(len(dat)*0.01)**(2/9))
        print("lag = ", lag)
        est2 = est.fit(cov_type = 'HAC', cov_kwds={'maxlags':lag}) # adding heteroscedasticity-consistent standard errors
        stderr = est2.bse[1] # stderr for trend coefficient
    else:
        est2 = est.fit() # default - without heteroscedasticity checking
        stderr = est2.bse[1] # stderr for trend coefficient
    
    # get fitted values
    predVal = est2.fittedvalues.copy()
    residual = y - predVal
    # plt.scatter(residual, predVal)
    # plt.ylabel("predVal")
    # plt.ylabel("trueVal")
    # plt.show()


    # print("pvalue = {}".format(est2.pvalues[1]))
    print(est2.summary())
    durbinStat = stools.durbin_watson(residual)
    print(durbinStat)

    # get coeff, intercept, pval, durbin, std
    return est2.params[1], est2.params[0], est2.pvalues[1], durbinStat, stderr

def plotIt(dat, tg):
    # plot data
    plt.figure(figsize=(10,4))
    plt.plot(dat['year'], dat['value'])
    plt.title(tg)
    plt.show()


# fun function
getTrends(1950,'HAC')