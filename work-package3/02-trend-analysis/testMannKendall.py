"""
Created on Fri Aug 30 08:08:00 2021

this program test the mann-kendal method

@author: Michael Tadesse

"""
import os
import pandas as pd
import statsmodels.api as sm
import pymannkendall as mk

os.chdir("G:\\report\\year-3\\07-Fall-2020\\#3Paper\\data\\"\
    "trend-analysis\\data\\01-twcr\\02-percentiles\\99")

dat = pd.read_csv("esbjerg_130121_denmark.csv")

print(dat)
dat = dat[dat['year'] >= 1875]

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

    return est2.params[1]*1000, est2.pvalues[1]

regTrend, regPval = simpleReg(dat, "HAC")

print(regTrend, regPval)

print("\n")

print("original mk")
print(mk.original_test(dat['value']), "\n")

print("modified mk")
print(mk.hamed_rao_modification_test(dat['value']))