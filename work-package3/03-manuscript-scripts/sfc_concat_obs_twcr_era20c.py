"""
Created on tue nov 12 12:16:00 2021
Modified on Thu Feb 03 12:45:00 2021

concatenating obs twcr and era20c in the same dataframe 
to prepare it for comparing trend differences

truncating data for post 1930 

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


dirTwcr = "G:\\report\\year-3\\07-Fall-2020\\#3Paper\\data\\"\
            "trend-analysis\\data\\allThreeTrends_storm_freq\\percentiles\\twcr"
dirEra20c = "G:\\report\\year-3\\07-Fall-2020\\#3Paper\\data\\"\
            "trend-analysis\\data\\allThreeTrends_storm_freq\\percentiles\\era20c"
dirObs = "G:\\report\\year-3\\07-Fall-2020\\#3Paper\\data\\"\
            "trend-analysis\\data\\allThreeTrends_storm_freq\\percentiles\\obs"
dirOut = "G:\\report\\year-3\\07-Fall-2020\\#3Paper\\data\\trend-analysis\\"\
            "data\\allThreeTrends_storm_freq_post1930\\allThree"


os.chdir(dirObs)
tgList = os.listdir()


for tg in tgList:
    print(tg)

    # get obs data
    os.chdir(dirObs)
    obs = pd.read_csv(tg)

    # take only post 1930 data
    obs = obs[obs['year'] >= 1930]

    obs.drop('Unnamed: 0', axis = 1, inplace = True)
    # print(obs)

    # get twcr
    os.chdir(dirTwcr)
    twcr = pd.read_csv(tg)

    # take only post 1930 data
    twcr = twcr[twcr['year'] >= 1930]

    twcr.drop('Unnamed: 0', axis = 1, inplace = True)
    # print(twcr)

    # get era20c
    os.chdir(dirEra20c)
    era20c = pd.read_csv(tg)

    # take only post 1930 data
    era20c = era20c[era20c['year'] >= 1930]

    era20c.drop('Unnamed: 0', axis = 1, inplace = True)
    # print(era20c)


    # concatenate the three
    newDat = pd.concat([obs, twcr, era20c], axis = 0)

    os.chdir(dirOut)
    newDat.to_csv(tg)

