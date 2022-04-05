"""
Created on tue nov 09 12:26:00 2021

this program gets the annual storm frequency  
for each year for a given threshold value (in percentile)

also gets this frequency for the obs 20-cr and era-20c for
the common period

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


dirHome = "G:\\report\\year-3\\07-Fall-2020\\#3Paper\\data\\"\
        "trend-analysis\\data\\03-obsSurge"

dirTwcr = "G:\\report\\year-3\\07-Fall-2020\\#3Paper\\data\\"\
        "trend-analysis\\data\\01-twcr\\01-postCPT"
dirEra20c = "G:\\report\\year-3\\07-Fall-2020\\#3Paper\\data\\"\
        "trend-analysis\\data\\02-era20c\\01-postCPT"
dirObs = "G:\\report\\year-3\\07-Fall-2020\\#3Paper\\data\\"\
        "trend-analysis\\data\\03-obsSurge\\data"

dirOut = "G:\\report\\year-3\\07-Fall-2020\\#3Paper\\data\\trend-analysis\\"\
        "data\\allThreeTrends_storm_freq"


os.chdir(dirHome)
tgList = pd.read_csv("obsSurgeAvailableDat.csv")


# only those with 30 years or plus and 75% availability
df = tgList[(tgList['lengthAvailable'] >= 30) &(tgList['percAvailable'] >= 75)]

for tg in df['tg']:
    print (tg)

    ################################################
    # select most recent start and earliest end date
    ################################################

    # check obs
    os.chdir(dirObs)
    obs = pd.read_csv(tg)
    start = obs['ymd'][0].split('-')[0]
    end = obs['ymd'][len(obs)-1].split('-')[0]
    # print("obs ", len(obs), start, end)

    # check twcr
    os.chdir(dirTwcr)
    if os.path.isfile(tg):
        twcr = pd.read_csv(tg)
        if (twcr['date'][0].split('-')[0] > start):
            start = twcr['date'][0].split('-')[0]
        if (twcr['date'][len(twcr)-1].split('-')[0] < end):
            end = twcr['date'][len(twcr)-1].split('-')[0]
    else:
        twcr = pd.DataFrame(columns = ['year', 'value', 'lon', 'lat'])
    # print("twcr ", len(twcr), start, end)

        # check era20c
    os.chdir(dirEra20c)
    if os.path.isfile(tg):
        era20c = pd.read_csv(tg)
        if (era20c['date'][0].split('-')[0] > start):
            start = era20c['date'][0].split('-')[0]
        if (era20c['date'][len(era20c)-1].split('-')[0] < end):
            end = era20c['date'][len(era20c)-1].split('-')[0]
    else:
        era20c = pd.DataFrame(columns = ['year', 'value', 'lon', 'lat'])
    # print("era20c ", len(era20c), start, end)
    print("\n")

    ################################################
    # get obs data
    os.chdir(dirObs)
    obs = pd.read_csv(tg)

    getYear = lambda x: x.split('-')[0]
    obs['year'] = pd.DataFrame(list(map(getYear, obs['ymd'])))

    obs = obs[(obs['year']>= start)&(obs['year']<= end)]
    obs['data'] = "obs"
    # print(obs)

    # get twcr data
    os.chdir(dirTwcr)
    if os.path.isfile(tg):
        twcr = pd.read_csv(tg)

        twcr['year'] = pd.DataFrame(list(map(getYear, twcr['date'])))

        twcr = twcr[(twcr['year']>= start)&(twcr['year']<= end)]
        twcr['data'] = "twcr"
        # print(twcr)
    else:
        print("twcr - {} no twcr data".format(tg))

    # get era20c data
    os.chdir(dirEra20c)
    if os.path.isfile(tg):
        era20c = pd.read_csv(tg)

        era20c['year'] = pd.DataFrame(list(map(getYear, era20c['date'])))

        era20c = era20c[(era20c['year']>= start)&(era20c['year']<= end)]
        era20c['data'] = "era20c"

        # print(era20c)
        print("\n")
    else:
        print("era20c - {} no era20c data".format(tg))

    ################################################
    # check if either twcr or era20c is missing

    #############################
    # merge with the same columns
    #############################

    if ((len(twcr) == 0) or (len(era20c) == 0)):
        continue # skip plotting this tg trends

    ################################################

    # concatenate obs, twcr, and era20c
    # this is to study the difference between trends
    newDat = pd.concat([obs, twcr, era20c], axis = 0)

    os.chdir(dirOut)
    newDat.to_csv(tg)