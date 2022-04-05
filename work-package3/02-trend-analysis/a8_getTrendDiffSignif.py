"""
Created on Mon Jul 26 08:32:00 2021

chcek if the difference in trends b/n obs 
and recons is significant

concept based on https://statisticsbyjim.com/regression/comparing-regression-lines/

https://stattrek.com/multiple-regression/interaction.aspx

https://www.theanalysisfactor.com/compare-regression-coefficients/

@author: Michael Getachew Tadesse

"""


import os
import os.path
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from a7_interactionRegression import getDummy, simpleReg
from scipy import stats
import statsmodels.stats.stattools as stools
import statsmodels.api as sm
from datetime import datetime


dirHome = "G:\\report\\year-3\\07-Fall-2020\\#3Paper\\data\\"\
        "trend-analysis\\data\\allThreeTrends\\95_30yrs_75perc"
dirOut = "G:\\report\\year-3\\07-Fall-2020\\#3Paper\\data\\"\
        "trend-analysis\\data\\allThreeTrends\\95TrendDiffSignificance"

os.chdir(dirHome)

#################################################################################
# create empty dataframe - for trend computation 
dfTrend = pd.DataFrame(columns = ['tg', 'lon', 'lat', 'obsTwcrPvalReg', 
        'obsTwcrPvalMK', 'obsEra20cPvalReg', 'obsEra20cPvalMK'])
#################################################################################

tgList = os.listdir()

for tg in tgList:
    print(tg)

    dat = pd.read_csv(tg)
    lon = dat['lon'].unique()[0]
    lat = dat['lat'].unique()[0]

    #####################################################
    # obs vs twcr
    obsTwcr = dat[~(dat['data'] == 'era20c')]
    interactions = getDummy(obsTwcr)
    
    obsTwcr['dummy1'] = interactions['obs']
    obsTwcr['dummy2'] = interactions['twcr']
    
    obsTwcr['int1'] = obsTwcr['dummy1']*obsTwcr['year']
    obsTwcr['int2'] = obsTwcr['dummy2']*obsTwcr['year']

    obsTwcr.drop(['Unnamed: 0', 'Unnamed: 0.1'], axis = 1, inplace = True)

    obs = obsTwcr[['year', 'value', 'dummy1', 'int1']]
    obs.columns = ['year', 'value', 'dummy', 'interaction']

    obsTwcrPval = simpleReg(obs, "HAC")
    #####################################################
    # obs vs era20c
    obsEra20c = dat[~(dat['data'] == 'twcr')]
    interactions = getDummy(obsEra20c)
    
    obsEra20c['dummy1'] = interactions['obs']
    obsEra20c['dummy2'] = interactions['era20c']
    
    obsEra20c['int1'] = obsEra20c['dummy1']*obsEra20c['year']
    obsEra20c['int2'] = obsEra20c['dummy2']*obsEra20c['year']

    obsEra20c.drop(['Unnamed: 0', 'Unnamed: 0.1'], axis = 1, inplace = True)

    obs = obsEra20c[['year', 'value', 'dummy1', 'int1']]
    obs.columns = ['year', 'value', 'dummy', 'interaction']

    obsEra20cPval = simpleReg(obs, "HAC")

    ######################################################

    newDf = pd.DataFrame([tg, lon, lat, obsTwcrPval, obsEra20cPval]).T
    newDf.columns = ['tg', 'lon', 'lat', 'obsTwcrPval', 'obsEra20cPval']
    dfTrend = pd.concat([dfTrend, newDf])

print(dfTrend)

# save as csv
os.chdir(dirOut)
dfTrend.to_csv("95thPercObsTwcrEra20cTrendDiffSignif_30yr_75perc.csv")
