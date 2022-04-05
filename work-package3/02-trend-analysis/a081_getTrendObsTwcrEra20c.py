"""  
Created on Fri Aug 20 09:44:00 2021

this script computes three trends for common period
obs - twcr - era20c

@author: Michael Tadesse

"""

from math import nan
import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy import stats
import pymannkendall as mk
import statsmodels.api as sm
import statsmodels.stats.stattools as stools
from scipy.stats import normaltest
from datetime import datetime

dirHome = "G:\\report\\year-3\\07-Fall-2020\\#3Paper\\data\\"\
    "trend-analysis\\data\\allThreeTrends\\99_30yrs_75perc"

os.chdir(dirHome)

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

# Mann-Kendall Trend Test
def mannKendal(dat):
    return mk.original_test(dat['value']).slope*1000, mk.original_test(dat['value']).p


print(os.listdir())

tgList = os.listdir()

# create empty dataframe
df = pd.DataFrame(columns = ['tg', 'lon', 'lat', 'obsTrendReg', 'obsPvalReg', \
        'obsTrendMK', 'obsPvalMK', 'twcrTrendReg', 'twcrPvalReg', 
            'twcrTrendMK', 'twcrPvalMK', 'era20cTrendReg', 'era20cPvalReg',
                'era20cTrendMK', 'era20cPvalMK'])


for tg in tgList:
    print(tg)

    dat = pd.read_csv(tg)
    print(dat)

    lon = dat['lon'].unique()[0]
    lat = dat['lat'].unique()[0]

    obs = dat[dat['data'] == 'obs']
    twcr = dat[dat['data'] == 'twcr']
    era20c = dat[dat['data'] == 'era20c']

    obsTrend, obsPval = simpleReg(obs, "HAC")
    obsTrendMK, obsPvalMK = mannKendal(obs)

    twcrTrend, twcrPval = simpleReg(twcr, "HAC")
    twcrTrendMK, twcrPvalMK = mannKendal(twcr)

    era20cTrend, era20cPval = simpleReg(era20c, "HAC")
    era20cTrendMK, era20cPvalMK = mannKendal(era20c)

    newDf = pd.DataFrame([tg, lon, lat, obsTrend, obsPval, obsTrendMK, obsPvalMK,
        twcrTrend, twcrPval, twcrTrendMK, twcrPvalMK, 
            era20cTrend, era20cPval, era20cTrendMK, era20cPvalMK]).T

    newDf.columns = ['tg', 'lon', 'lat', 'obsTrendReg', 'obsPvalReg', \
        'obsTrendMK', 'obsPvalMK', 'twcrTrendReg', 'twcrPvalReg', 
            'twcrTrendMK', 'twcrPvalMK', 'era20cTrendReg', 'era20cPvalReg',
                'era20cTrendMK', 'era20cPvalMK']
    df = pd.concat([df, newDf])

print(df)

# get significance of trends

df['oRegSig'] = df['obsPvalReg'] <= 0.05
df['oMKSig'] = df['obsPvalMK'] <= 0.05

df['tRegSig'] = df['twcrPvalReg'] <= 0.05
df['tMKSig'] = df['twcrPvalMK'] <= 0.05

df['eRegSig'] = df['era20cPvalReg'] <= 0.05
df['eMKSig'] = df['era20cPvalMK'] <= 0.05



os.chdir("G:\\report\\year-3\\07-Fall-2020\\#3Paper\\data\\"\
    "trend-analysis\\data\\allThreeTrends")

df.to_csv("99thTrendObsTwcrEra20c_30yrs_75perc.csv")