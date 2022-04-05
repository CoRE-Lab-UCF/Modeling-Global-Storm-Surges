"""
Created on Fri Jul 30 12:17:00 2021

this program gets the annual mean storm intensity  
for each year for a given threshold value (in percentile)
it averages the surge values per year that are greater or
equal to the specified threshold amount of the given year

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

dirHome = {
    "twcr" : "G:\\report\\year-3\\07-Fall-2020\\#3Paper\\data\\"\
        "trend-analysis\\data\\01-twcr\\01-postCPT",
    "era20c" : "G:\\report\\year-3\\07-Fall-2020\\#3Paper\\data\\"\
        "trend-analysis\\data\\02-era20c\\01-postCPT"
}

dirOut = {
    "twcr" : "G:\\report\\year-3\\07-Fall-2020\\#3Paper\\data\\"\
        "trend-analysis\\data\\01-twcr\\06-stormIntensity",
    "era20c" : "G:\\report\\year-3\\07-Fall-2020\\#3Paper\\data\\"\
        "trend-analysis\\data\\02-era20c\\06-stormIntensity"
}




def getStormIntensity(recon):
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

        # print(dat)

        yrs = dat['year'].unique()


        # create empty dataframe
        df = pd.DataFrame(columns = ['year', 'lon', 'lat', 's95', 's99', 's999', 'mean95', 'mean99', 'mean999'])

        for y in yrs:
            yrDat = dat[dat['year'] == y]

            s95 = yrDat['surge_reconsturcted'].quantile(0.95)
            s99 = yrDat['surge_reconsturcted'].quantile(0.99)
            s999 = yrDat['surge_reconsturcted'].quantile(0.999)

            mean95 = np.mean(yrDat[yrDat['surge_reconsturcted'] >= s95]['surge_reconsturcted'])
            mean99 = np.mean(yrDat[yrDat['surge_reconsturcted'] >= s99]['surge_reconsturcted'])
            mean999 = np.mean(yrDat[yrDat['surge_reconsturcted'] >= s999]['surge_reconsturcted'])

            newDf = pd.DataFrame([y, lon, lat, s95, s99, s999, mean95, mean99, mean999]).T
            newDf.columns = ['year', 'lon', 'lat', 's95', 's99', 's999', 'mean95', 'mean99', 'mean999']
            df = pd.concat([df, newDf]) 
        
        # print(df)

        # save file
        os.chdir(dirOut[recon])
        df.to_csv(tg)

# call function
getStormIntensity("era20c")