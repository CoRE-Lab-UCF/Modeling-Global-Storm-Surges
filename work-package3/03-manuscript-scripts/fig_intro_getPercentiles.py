"""

Created on Thu Mar 02 09:02:00 2022

get annual percentiles of reconstructions

@author: Michael Getachew Tadesse

"""


import os
import numpy as np
import pandas as pd
from datetime import datetime


dirHome = {
    "twcr" : "G:\\data\\allReconstructions\\01_20cr",
    "era20c" : "G:\\data\\allReconstructions\\02_era20c"
}


dirOut = {
    "twcr" : "G:\\report\\year-3\\07-Fall-2020\\#3Paper\\"\
            "p28ThirdManuscript\\manuscript\\data\\percentiles\\g20cr",
    "era20c" : "G:\\report\\year-3\\07-Fall-2020\\#3Paper\\"\
            "p28ThirdManuscript\\manuscript\\data\\percentiles\\ge20c"
        }

def getPercentile(recon, x):
    """  
    this function gets the xth percentile value for each year
    recon = {twcr, era20c}
    x = 99.5 - for instance 
    dat - original data (daily time step)
    """
    # get to the recon folder
    os.chdir(dirHome[recon])

    tgList = os.listdir()

    # loop through tide gauges
    for tg in tgList:

        os.chdir(dirHome[recon])

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
            xValue = currentYr['surge_reconsturcted'].quantile(x*0.01)
            newDf = pd.DataFrame([yr, xValue, currentYr['lon'].unique()[0], \
                    currentYr['lat'].unique()[0]]).T 
            newDf.columns = ['year', 'value', 'lon', 'lat']
            df = pd.concat([df, newDf])

        # create saving directory
        os.chdir(dirOut[recon])

        try:
            os.makedirs(str(x))
            os.chdir(str(x)) #cd to it after creating it
        except FileExistsError:
            #directory already exists
            os.chdir(str(x))

        # save as csv
        df.to_csv(tg)



# run code
# recon = ["twcr", "era20c"]
# percentiles = [1, 5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, \
#         65, 70, 75, 80, 85, 90, 95, 99, 99.9]

recon = ["era20c"]
percentiles = [99]

for r in recon:
    for p in percentiles:
        print("{} - {}".format(r, p))
        getPercentile(r, p)
