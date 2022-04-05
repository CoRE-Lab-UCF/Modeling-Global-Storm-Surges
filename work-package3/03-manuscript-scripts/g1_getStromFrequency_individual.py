"""
* Created on Wed Jul 28 11:55:00 2021                             *
* Modified on Wed Jan 26 10:08:00 2022                            *
* Modified on Tue Mar 22 19:31:00 2022                                     

* this program gets the annual storm frequency                    *
* for each year for a given threshold value (in percentile)       *
*                                                                 *
* *Modified to calculate storm frequency trends from 1930/1950    *
*  this program will truncate the original data at 1930     

  *Modified to declusted surge events (spaced out by 3 days)
*                                                                 *
*@author: Michael Getachew Tadesse                                *

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
import datetime as dt

dirHome = {
    "twcr" : "G:\\report\\year-3\\07-Fall-2020\\#3Paper\\data\\"\
        "trend-analysis\\data\\01-twcr\\01-postCPT",
    "era20c" : "G:\\report\\year-3\\07-Fall-2020\\#3Paper\\data\\"\
        "trend-analysis\\data\\02-era20c\\01-postCPT"
}

dirOut = {
    "twcr" : "G:\\report\\year-3\\07-Fall-2020\\#3Paper\\data\\"\
        "trend-analysis\\data\\01-twcr\\05-stormFrequency_v3",
    "era20c" : "G:\\report\\year-3\\07-Fall-2020\\#3Paper\\data\\"\
        "trend-analysis\\data\\02-era20c\\05-stormFrequency_v3"
}




def getStormFreq(recon):
    """  
    recon: {twcr, era20c}
    param: {95, 99, 99.9}
    """
    os.chdir(dirHome[recon])
    tgList = os.listdir()

    for tg in tgList:
        os.chdir(dirHome[recon])

        print(tg)

        dat = pd.read_csv(tg)
        lon = dat['lon'].unique()[0]
        lat = dat['lat'].unique()[0]

        # get years
        getYears = lambda x: x.split('-')[0]
        dat['year'] = pd.DataFrame(list(map(getYears, dat['date'])))

        # limit data to start on/after 1930
        dat = dat[dat['year'] >= "1930"]
        # print(dat)

        s95 = dat['surge_reconsturcted'].quantile(0.95)
        s99 = dat['surge_reconsturcted'].quantile(0.99)
        s999 = dat['surge_reconsturcted'].quantile(0.999)

        yrs = dat['year'].unique()


        # create empty dataframe
        df = pd.DataFrame(columns = ['year', 'lon', 'lat', 's95', 's99', 
                                        's999', 'num95', 'num99', 'num999'])

        for y in yrs:
            yrDat = dat[dat['year'] == y]

            above95 = yrDat[yrDat['surge_reconsturcted'] >= s95]
            above99 = yrDat[yrDat['surge_reconsturcted'] >= s99]
            above999 = yrDat[yrDat['surge_reconsturcted'] >= s999]
            # print(above99)
            
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


            newDf = pd.DataFrame([y, lon, lat, s95, s99, s999, num95, num99, num999]).T
            newDf.columns = ['year', 'lon', 'lat', 's95', 's99', 's999', 
                                            'num95', 'num99', 'num999']
            df = pd.concat([df, newDf]) 
        
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
getStormFreq("era20c")