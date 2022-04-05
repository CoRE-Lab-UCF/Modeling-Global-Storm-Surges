"""
Created on Sun Jan 16 09:50:00 2022

convert hourly surge to daily max surge 

@author: Michael Getachew Tadesse

"""

import os 
import pandas as pd
from functools import reduce
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from datetime import datetime

# directories
home = "G:\\report\\year-3\\07-Fall-2020\\#3Paper\\data"\
            "\\trend-analysis\\data\\allSixTrends\\rawData\\"\
                    "australia_tgs\\selected_v2"
geoData = "G:\\report\\year-3\\07-Fall-2020\\#3Paper\\data"\
            "\\trend-analysis\\data\\03-obsSurge\\data"
dmax = "G:\\report\\year-3\\07-Fall-2020\\#3Paper\\data"\
            "\\trend-analysis\\data\\allSixTrends\\rawData\\"\
                    "australia_tgs\\dmax"

os.chdir(home)

tgList = os.listdir()

for tg in tgList:

    os.chdir(home)

    print(tg)

    dat = pd.read_csv(tg)

    # get date column
    dat['date'] = dat['year'].astype(str) + '-' + \
                        dat['month'].astype(str) + '-' + \
                            dat['day'].astype(str)
    
    # get lon/lat
    os.chdir(geoData)
    geoDat = pd.read_csv(tg.split('txt')[0] + 'csv')
    lon = geoDat['lon'][0]
    lat = geoDat['lat'][0]
    dat['lon'] = lon
    dat['lat'] = lat

    dat = dat[['date', 'lon', 'lat', 'surge']]

    print(lon, lat)

    # create an empty dataframe
    df = pd.DataFrame(columns = ['date', 'lon', 'lat', 'surge'])
    unq_date = dat.date.unique()

    for d in unq_date:
        # print(d)
        newDf = dat[dat['date'] == d]

        newDf = newDf[newDf['surge'] == newDf['surge'].max()].iloc[0,:]
        newDat = pd.DataFrame([newDf['date'], newDf['lon'], newDf['lat'], newDf['surge']]).T
        newDat.columns = ['date', 'lon', 'lat', 'surge']
        # print(newDf)

        df = pd.concat([df, newDat], axis = 0)
    print(df)

    # save dmax
    os.chdir(dmax)
    df.to_csv(tg.split('.txt')[0] + '.csv')

