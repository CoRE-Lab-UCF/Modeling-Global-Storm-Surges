import os
import pandas as pd
from datetime import datetime
import matplotlib.pyplot as plt


dirHome = "G:\\report\\year-3\\07-Fall-2020\\#3Paper\\data\\trend-analysis\\data\\test"

os.chdir(dirHome)

dat = pd.read_csv("cuxhaven_germanyEra20c.csv")
time_stamp = lambda x: (datetime.strptime(x, '%Y-%m-%d %H:%M:%S'))
dat['date'] = pd.DataFrame(list(map(time_stamp, dat['date'])))

def plotTimeSeries():
    time_stamp = lambda x: (datetime.strptime(x, '%Y-%m-%d %H:%M:%S'))

    dat['date'] = pd.DataFrame(list(map(time_stamp, dat['date'])), 
                                            columns = ['date'])

    print(dat)

    plt.figure(figsize=(15,4))
    plt.plot(dat['date'], dat['surge_reconsturcted'], label = "twcr surge", color = "green")
    plt.legend()
    plt.ylabel("Surge Height (m)")
    plt.grid(b=None, which='major', axis= 'both', linestyle='-')
    plt.minorticks_on()
    plt.grid(b=None, which='minor', linestyle='--', axis="both", alpha=0.4)
    plt.show()

### get annual xth percentiles
## for each year get the xth percentile

def getPercentile(dat, x):
    """  
    this function gets the xth percentile value for each year
    x = 99.5 - for instance 
    dat - original data (daily time step)
    """
    # get year for each row
    getYear = lambda x: x.year
    dat['year'] = pd.DataFrame(list(map(getYear, dat['date'])))

    # print(dat)

    years = dat['year'].unique()

    # create an empty dataframe for xth percentiles
    df = pd.DataFrame(columns = ['year', 'value'])

    for yr in years:
        currentYr = dat[dat['year'] == yr]
        xValue = currentYr['surge_reconsturcted'].quantile(x*0.01)
        newDf = pd.DataFrame([yr, xValue]).T 
        newDf.columns = ['year', 'value']
        df = pd.concat([df, newDf])
    print(df)

    # save as csv
    df.to_csv("cuxhavenEra20c99Percentile.csv")

getPercentile(dat,99)
