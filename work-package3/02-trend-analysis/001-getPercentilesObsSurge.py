import os
import numpy as np
import pandas as pd
from datetime import datetime


dirHome = "G:\\report\\year-3\\07-Fall-2020\\#3Paper\\data\\"\
    "trend-analysis\\data\\03-obsSurge\\data"


dirOut = "G:\\report\\year-3\\07-Fall-2020\\#3Paper\\data\\"\
    "trend-analysis\\data\\03-obsSurge\\percentiles"

def getPercentile(x):
    """  
    this function gets the xth percentile value for each year
    considering only observed surge
    x = 99.5 - for instance 
    dat - original data (daily time step)
    """
    # get to the obs folder
    os.chdir(dirHome)

    tgList = os.listdir()

    # loop through tide gauges
    for tg in tgList:

        os.chdir(dirHome)

        # print(tg)

        dat = pd.read_csv(tg)

        # get year for each row
        time_stamp = lambda x: (datetime.strptime(x, '%Y-%m-%d %H:%M:%S'))
        dat['date'] = pd.DataFrame(list(map(time_stamp, dat['date'])))

        getYear = lambda x: x.year
        dat['year'] = pd.DataFrame(list(map(getYear, dat['date'])))

        years = dat['year'].unique()
        
        # create an empty dataframe for xth percentiles
        df = pd.DataFrame(columns = ['year', 'value', 'lon', 'lat'])

        for yr in years:
            currentYr = dat[dat['year'] == yr]
            xValue = currentYr['surge'].quantile(x*0.01)
            newDf = pd.DataFrame([yr, xValue, currentYr['lon'].unique()[0], \
                    currentYr['lat'].unique()[0]]).T 
            newDf.columns = ['year', 'value', 'lon', 'lat']
            df = pd.concat([df, newDf])

        # create saving directory
        os.chdir(dirOut)

        try:
            os.makedirs(str(x))
            os.chdir(str(x)) #cd to it after creating it
        except FileExistsError:
            #directory already exists
            os.chdir(str(x))

        # save as csv
        df.to_csv(tg)



# run code
percentiles = [95, 99, 99.9]

for p in percentiles:
    print("{}".format(p))
    getPercentile(p)
