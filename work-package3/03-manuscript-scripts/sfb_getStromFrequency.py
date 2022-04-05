"""
Created on Wed Jul 28 11:55:00 2021
modified on mon nov 15 09:26:00 2021


this program gets the annual storm frequency  
for each year for a given threshold value (in percentile)
for obs twcr and era20c

@author: Michael Tadesse

"""

from math import nan
import os
import logging
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy import stats
import statsmodels.api as sm
import statsmodels.stats.stattools as stools
from scipy.stats import normaltest
from datetime import datetime
import datetime as dt

dirHome = {
    "twcr" : "G:\\report\\year-3\\07-Fall-2020\\#3Paper\\data\\"\
            "trend-analysis\\data\\allThreeTrends_storm_freq\\twcr",
    "era20c" : "G:\\report\\year-3\\07-Fall-2020\\#3Paper\\data\\"\
            "trend-analysis\\data\\allThreeTrends_storm_freq\\era20c",
    "obs" : "G:\\report\\year-3\\07-Fall-2020\\#3Paper\\data\\"\
            "trend-analysis\\data\\allThreeTrends_storm_freq\\obs"
}

dirOut = {
    "twcr" : "G:\\report\\year-3\\07-Fall-2020\\#3Paper\\data\\"\
            "trend-analysis\\data\\allThreeTrends_storm_freq\\percentiles\\twcr",
    "era20c" : "G:\\report\\year-3\\07-Fall-2020\\#3Paper\\data\\"\
            "trend-analysis\\data\\allThreeTrends_storm_freq\\percentiles\\era20c",
    "obs" : "G:\\report\\year-3\\07-Fall-2020\\#3Paper\\data\\"\
            "trend-analysis\\data\\allThreeTrends_storm_freq\\percentiles\\obs",
    "log" : "G:\\report\\year-3\\07-Fall-2020\\#3Paper\\data\\"\
            "trend-analysis\\data\\allThreeTrends_storm_freq\\percentiles"
}




def getStormFreq(recon):
    """  
    recon: {twcr, era20c, obs}
    """
    os.chdir(dirHome[recon])
    tgList = os.listdir()

    # setting up a log file
    os.chdir(dirOut['log'])
    logging.basicConfig(filename="log.txt", encoding='utf-8', level=logging.DEBUG)

    for tg in tgList:
        os.chdir(dirHome[recon])

        print(tg)


        dat = pd.read_csv(tg)
        lon = dat['lon'].unique()[0]
        lat = dat['lat'].unique()[0]
        recon = dat['data'].unique()[0]


        # rename columns to match
        if (recon == 'era20c') | (recon == 'twcr'):
            dat['surge'] = dat['surge_reconsturcted']


        # get percentiles
        s95 = dat['surge'].quantile(0.95)
        s99 = dat['surge'].quantile(0.99)
        s999 = dat['surge'].quantile(0.999)

        yrs = dat['year'].unique()


        # create empty dataframe
        df = pd.DataFrame(columns = ['year', 'lon', 'lat', 's95', 's99', \
                        's999', 'num95', 'num99', 'num999', 'recon'])

        for y in yrs:
            yrDat = dat[dat['year'] == y]

            above95 = yrDat[yrDat['surge'] >= s95]
            above99 = yrDat[yrDat['surge'] >= s99]
            above999 = yrDat[yrDat['surge'] >= s999]


            # check if percentile outputs are null
            if len(above95) == 0:
                num95 = 0
            else:
                num95 = decluster(above95)

            if len(above99) == 0:
                num99 = 0
            else:
                num99 = decluster(above99)

            if len(above999) == 0:
                num999 = 0
            else:
                num999 = decluster(above999)


            newDf = pd.DataFrame([y, lon, lat, s95, s99, s999, num95, num99, num999, recon]).T
            newDf.columns = ['year', 'lon', 'lat', 's95', 's99', 's999',\
                     'num95', 'num99', 'num999', 'recon']
            df = pd.concat([df, newDf]) 
        
        print(df)


        # writing a log file
        os.chdir(dirOut['log'])

        logging.info("\n\n")
        logging.info(recon)
        logging.info("\n\n")

        logging.info(tg)
        logging.info(df)

        # save file
        os.chdir(dirOut[recon])
        df.to_csv(tg)

# function to decluster 
def decluster(dat):
    dat.reset_index(inplace=True)
    start_date = dat['date'][0]
    # print("start date =", start_date)

    count = 0
    while len(dat) > 0:

        # print(dat)
        dat.reset_index(inplace = True)
        dat.drop("index", axis = 1, inplace = True)

        # assign the first date as start date
        start_date = dat['date'][0]

        # considering 3 days for declustering
        end_date = pd.to_datetime(start_date) + dt.timedelta(days= 2)

        # print(start_date, end_date)

        newDat = dat[dat['date'] <= str(end_date)]

        # register one surge event to the count
        count += 1
        
        # drop the first n rows from the dataframe
        dat.drop(dat.index[0:len(newDat)],0, inplace = True)
    
    return count



# call function
getStormFreq("obs")