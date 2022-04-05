"""  
Created on Fri Jul 05 08:00:00 2021

this script computes trends for observed surge - 
twcr recon - era20c recon by incorporating the heteroscedasticity 
and autocorrelation robus covariance matrix (Newey-West)

@author: Michael Tadesse

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
dirHome = {
    "twcr" : "G:\\report\\year-3\\07-Fall-2020\\#3Paper\\data\\"\
        "trend-analysis\\data\\01-twcr\\02-percentiles\\50",
    "era20c" : "G:\\report\\year-3\\07-Fall-2020\\#3Paper\\data\\"\
        "trend-analysis\\data\\02-era20c\\02-percentiles\\50"
}

dirOut = {
    "twcr" : "G:\\report\\year-3\\07-Fall-2020\\#3Paper\\data\\"\
        "trend-analysis\\data\\01-twcr\\04-hacTrends",
    "era20c" : "G:\\report\\year-3\\07-Fall-2020\\#3Paper\\data\\"\
        "trend-analysis\\data\\02-era20c\\04-hacTrends"
}

# write the code to accomodate recon + percentile

def getTrends(recon, *args):
    """ 
    this function computes the trends after 
    args: HAC - heteroskedasticity-autocorrelation robust covariance
    maxlag: integer - number of lags
    """
    os.chdir(dirHome[recon])

    tgList = os.listdir()

    # create empty dataframe
    df = pd.DataFrame(columns = ['tg', 'lon', 'lat', 'normality', 'trend(mm/year)', 'pval', 'dw', 'stderr'])

    for tg in tgList:
        print(tg)

        # load data
        dat = pd.read_csv(tg)

        lon = dat['lon'].unique()[0]
        lat = dat['lat'].unique()[0]

        shapiro, dagosto = checkNormality(dat['value'])

        # if (shapiro <= 0.05) or (dagosto <= 0.05): # original statement
        # if (shapiro > 100) or (dagosto > 100): # to include non-normal data
        if (shapiro > 100) or (dagosto > 100):
            # failed either one of normality tests
            newDf = pd.DataFrame([tg, lon, lat, False, np.nan, np.nan]).T
            newDf.columns = ['tg', 'lon', 'lat', 'normality', 'trend(mm/year)', 'pval', 'dw', 'stderr']
            df = pd.concat([df, newDf])
        else:
            if args:
                for ar in args:
                    annualTrend, pval, durbinStat, stderr = simpleReg(dat, ar)
            else:
                ar = ""
                annualTrend, pval, durbinStat, stderr = simpleReg(dat, ar)
            # print(tg, " - ", dubrinWatson)
            newDf = pd.DataFrame([tg, lon, lat, True, annualTrend, pval, durbinStat, stderr]).T
            newDf.columns = ['tg', 'lon', 'lat', 'normality', 'trend(mm/year)', 'pval', 'dw', 'stderr']
            df = pd.concat([df, newDf])
    
    print(df)

    # check significance at 95% confidence level
    df['significance'] = (~df['pval'].isnull()) & (df['pval'] <= 0.05)

    print(df)

    # save file
    os.chdir(dirOut[recon])
    df.to_csv("{}50thPercTrends_hac{}.csv".format(recon, ar)) # adding heteroscedasticity-consistent standard errors
    
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
    y = dat['value']

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
    
    print(est2.summary())

    # get fitted values
    predVal = est2.fittedvalues.copy()
    residual = y - predVal
    # plt.scatter(residual, predVal)
    # plt.ylabel("predVal")
    # plt.ylabel("trueVal")
    # plt.show()


    # print("pvalue = {}".format(est2.pvalues[1]))
    # print(est2.summary())
    durbinStat = stools.durbin_watson(residual)
    print(durbinStat)
    return est2.params[1]*1000, est2.pvalues[1], durbinStat, stderr

def plotIt(dat, tg):
    # plot data
    plt.figure(figsize=(10,4))
    plt.plot(dat['year'], dat['value'])
    plt.title(tg)
    plt.show()


# fun function
getTrends("era20c", 'HAC')