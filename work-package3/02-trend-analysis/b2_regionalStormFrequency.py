"""
Created on Wed Jul 29 08:30:00 2021
modified on Thu Sep 30 07:24:00 2021

this program gets annual storm frequency for 
regionally clustered tgs 

all plots for the 1875-2015 period

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

dirOut = "G:\\report\\year-3\\07-Fall-2020\\#3Paper\\data\\"\
    "trend-analysis\\data\\05-regionalStormFreqTrends"


def plotRegFreq(recon, region, threshold):
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
        # print(newDat)


    # load and plot tg data
    os.chdir(dirHome[recon] + "\\05-stormFrequency")

    sns.set_context('paper', font_scale = 1.75)

    plt.figure(figsize=(10,5))
    plt.ylabel('No. Storms above {}'.format(threshold))
    plt.xlim([1870, 2020])
    plt.ylim([0, 50])

    # plt.title("{} - Annual Storm Frequency - {}".format(region, recon))

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
        
        # print(tgDat)

        plt.plot(tgDat[tgDat['year'] >= 1950]['year'], \
                tgDat[tgDat['year'] >= 1950][threshold], 'gray', lw = 0.75)

        #####################################################################
        ## plotting moving average
        # plt.plot(tgDat['year'], tgDat[threshold].rolling(window = 10).mean())
        #####################################################################

    
    os.chdir("G:\\report\\year-3\\07-Fall-2020\\#3Paper\\"\
        "data\\trend-analysis\\data\\04-regionalStormFreq")
    
    df = df.sort_values(by ='year')
    df['avg'] = df.iloc[:,1:].mean(axis = 1)
    print(df)
    # df.to_csv("{}_{}_{}.csv".format(recon,region,threshold))


    # plot averaged storm count
    # change the year here base on plotting preference
    plt.plot(df[df['year'] >= 1950]['year'], df[df['year'] >= 1950]['avg'], \
            label = "average storm count", color = "black", lw = "4")
    

    ##################################################################
    # plot trend lines
    ##################################################################

    # # 1875 trend
    # plt.plot(df[df['year'] >= 1875]['year'], -83.58083692 + \
    #     0.05222991*df[df['year'] >= 1875]['year'], \
    #          'r', label = "1875-2015 trend", lw = 2.5, ls = "--")
    # # 1900 trend
    # plt.plot(df[df['year'] >= 1900]['year'], -94.49407261 + \
    #     0.057346246*df[df['year'] >= 1900]['year'], \
    #          'blue', label = "1900-2015 trend", lw = 2.5, ls = "--")
    # 1950 trend
    plt.plot(df[df['year'] >= 1950]['year'], -67.32428462 + \
        0.043245784*df[df['year'] >= 1950]['year'], \
             'lime', label = "1950-2015 trend", lw = 2.5, ls = "--")




    # plt.text(1970, 42, "Trend Slope = 0.093", bbox=dict(facecolor='red', alpha=0.5))
    plt.grid(b=None, which='major', axis= 'both', linestyle='-')
    plt.minorticks_on()
    plt.grid(b=None, which='minor', linestyle='--', axis="both", alpha=0.4)
    # plt.legend(ncol = 2)

    # print number of tgs
    print(len(newDat))


    # save figure
    os.chdir(dirOut)
    plt.savefig(region+"_"+recon+"_"+ threshold +".svg", dpi = 400)

    plt.show()

    


# run code
plotRegFreq("era20c", "gulf", "num95")
