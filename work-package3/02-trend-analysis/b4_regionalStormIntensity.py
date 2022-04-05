"""
Created on Wed Jul 30 12:10:00 2021

this program gets mean of the surge values above a given 
threshold value for each tg 

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


geoRef = {
    "usw" : [-150, -120, 30, 60],
    "use" : [-80, -65, 25, 40],
    "gulf" : [-97, -82, 25, 30],
    "estAsia" : [110, 146, 20, 43],
    "aus_Nz" : [113, 180, -46, -11],
    "mediter" : [1.5, 15, 38, 45],
    "westEurope" : [-11, 9, 48, 59]
}


dirHome = {
    "twcr" : "G:\\report\\year-3\\07-Fall-2020\\#3Paper\\data\\"\
        "trend-analysis\\data\\01-twcr",
    "era20c" : "G:\\report\\year-3\\07-Fall-2020\\#3Paper\\data\\"\
        "trend-analysis\\data\\02-era20c"
}


def plotRegIntensity(recon, region, threshold):
    """  
    recon = {twcr, era20c}
    region = {usw, use, europe, japan}
    threshold = {s95, s99, s999, mean95, mean99, mean999}
    """

    os.chdir(dirHome[recon])

    dat = pd.read_csv(recon+"TrendTgs.csv")

    # filter tgs
    if region == ["sweden", "norway"]:
        getCountry = lambda x: ("norway" in x) | ("sweden" in x)
        dat['country'] = pd.DataFrame(list(map(getCountry, dat['tg'])))
        print(dat)
        newDat = dat[dat['country']]
        print(newDat)
    elif region == "south_africa":
        getCountry = lambda x: (region in x)
        dat['country'] = pd.DataFrame(list(map(getCountry, dat['tg'])))
        print(dat)
        newDat = dat[dat['country']]
        print(newDat)
    else:
        lonRange = geoRef[region][:2]
        latRange = geoRef[region][2:4]

        newDat = dat[((dat['lon'] >= lonRange[0]) & (dat['lon'] <= lonRange[1])) & \
                ((dat['lat'] >= latRange[0]) & (dat['lat'] <= latRange[1]))]
        # print(newDat)


    # load and plot tg data
    os.chdir(dirHome[recon] + "\\06-stormIntensity")

    plt.figure(figsize=(14,5))
    plt.ylabel('Surge Height (m)')
    plt.xlim([1836, 2015])
    # plt.ylim([0, 55])
    plt.title("{} - Annual Mean Storm Intensity - {}".format(region, recon))

    for tg in newDat['tg']:
        print(tg)
        tgDat = pd.read_csv(tg)
        # print(tgDat)

        # plt.plot(tgDat['year'], tgDat[threshold])

        #####################################################################
        ## plotting moving average
        plt.plot(tgDat['year'], tgDat[threshold].rolling(window = 10).mean(), label = tg)
        #####################################################################
    # plt.legend()
    plt.show()

    


# run code
plotRegIntensity("twcr", "westEurope", "mean999")