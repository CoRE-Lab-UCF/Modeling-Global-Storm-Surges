"""
Created on Wed Jul 29 08:30:00 2021
modified on Thu Sep 30 07:24:00 2021
modified on Wed Jan 26 12:09:00 2022

this program gets annual storm frequency for 
regionally clustered tgs 

it also averages the storm counts per region 

@author: Michael Tadesse

"""

from math import nan
import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
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

# dirOut = "G:\\report\\year-3\\07-Fall-2020\\#3Paper\\data\\"\
#     "trend-analysis\\data\\05-regionalStormFreqTrends_v3"


def getRegFreq(recon, region, threshold):
    """  
    recon = {twcr, era20c}
    region = {usw, use, europe, japan}
    threshold = {num95, num99, num999}
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
        print(newDat)

    ###################################################
    # change directory to individual surge frequency
    ###################################################

    # load tg data
    os.chdir(dirHome[recon] + "\\05-stormFrequency_v3")

    # concatenate regional counts
    df = pd.DataFrame()
    first = True

    for tg in newDat['tg']:
        print(tg)
        tgDat = pd.read_csv(tg)
        
        if first:
            df = tgDat[['year', threshold]] 
            first = False
        else:
            df = pd.merge(df, tgDat[['year', threshold]], on = "year", how="outer")
        

    #     #####################################################################
    #     ## plotting moving average
    #     # plt.plot(tgDat['year'], tgDat[threshold].rolling(window = 10).mean())
    #     #####################################################################

    
    os.chdir("G:\\report\\year-3\\07-Fall-2020\\#3Paper\\"\
        "data\\trend-analysis\\data\\04-regionalStormFreq_v3")
    
    df = df.sort_values(by ='year')
    df['avg'] = df.iloc[:,1:].mean(axis = 1)
    print(df)
    df.to_csv("{}_{}_{}.csv".format(recon,region,threshold))


# run code

regions = [ "usw", "use", "gulf", "estAsia", "aus_Nz", 
                "mediter", "westEurope", ["sweden", "norway"] ]

recon = ["twcr", "era20c"]


for rec in recon:
    for reg in regions:
        getRegFreq(rec, reg, "num95")
