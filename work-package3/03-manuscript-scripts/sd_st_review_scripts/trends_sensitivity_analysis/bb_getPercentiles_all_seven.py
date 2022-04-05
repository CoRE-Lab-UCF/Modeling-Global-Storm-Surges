"""
Created on Fri Dec 17 12:47:00 2021
Modified on Tue Dec 21 13:22:00 2021
Modified on Fri Jan 21 11:51:00 2022

get annual percentiles of G-20CR|G-E20C|G-Int|G-Merra|G-E5|G-EnsMean and Obs  

@author: Michael Tadesse

"""

import os 
import pandas as pd
from datetime import datetime
from functools import reduce


dir_home = "G:\\report\\year-3\\07-Fall-2020\\#3Paper\\data\\"\
            "trend-analysis\\data\\allSevenTrends\\rawData"
dir_out = "G:\\report\\year-3\\07-Fall-2020\\#3Paper\\data\\"\
            "trend-analysis\\data\\allSevenTrends\\percentiles\\99"

def getPercentile(x):
    """  
    this function gets the xth percentile value for each year
    x = 99.5 - for instance 
    """
    # get to the data folder
    os.chdir(dir_home)

    tgList = os.listdir()

    # loop through tide gauges
    for tg in tgList:

        os.chdir(dir_home)

        # print(tg)

        dat = pd.read_csv(tg)[['date', 'lon', 'lat', 'surge', 'twcr_surge',
                                         'era20c_surge', 'eraint_surge', 'merra_surge', 
                                            'era5_surge', 'ensMean']]
        dat.columns = ['date', 'lon', 'lat', 'obs', 'twcr', 'era20c', 
                                'eraint', 'merra', 'era5', 'ensMean']


        # get year for each row
        time_stamp = lambda x: (datetime.strptime(x, '%Y-%m-%d'))
        dat['date'] = pd.DataFrame(list(map(time_stamp, dat['date'])))

        getYear = lambda x: x.year
        dat['year'] = pd.DataFrame(list(map(getYear, dat['date'])))

        years = dat['year'].unique()
        
        # create an empty dataframe for xth percentiles
        df = pd.DataFrame(columns = ['year', 'obs', 'twcr', 'era20c', 
                                        'eraint', 'merra', 'era5', 'ensMean', 'lon', 'lat'])

        # merge percentiles
        data = ['obs', 'twcr', 'era20c', 'eraint', 'merra', 'era5', 'ensMean']
        isFirst = True
        for d in data:
            if isFirst:
                df =  computePercentile(dat, years, d, x)[['year', 'lon', 'lat', d]]
                isFirst = False
            else:
                newDf = computePercentile(dat, years, d, x)[['year', d]]
                df = pd.merge(df, newDf, on='year', how = 'left')

        # create saving directory
        os.chdir(dir_out)

        # save as csv
        df.to_csv(tg)


def computePercentile(dat, years, d, x):
    # create an empty dataframe for xth percentiles
    df = pd.DataFrame(columns = ['year', d, 'lon', 'lat'])
    
    for yr in years:
        currentYr = dat[dat['year'] == yr]
        xValue = currentYr[d].quantile(x*0.01)
        newDf = pd.DataFrame([yr, xValue, currentYr['lon'].unique()[0], \
                currentYr['lat'].unique()[0]]).T 
        newDf.columns = ['year', d, 'lon', 'lat']
        df = pd.concat([df, newDf])

    return df


# run code
getPercentile(99)