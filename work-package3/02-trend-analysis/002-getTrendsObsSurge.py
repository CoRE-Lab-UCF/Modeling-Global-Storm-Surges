from math import nan
import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy import stats
import statsmodels.api as sm
from scipy.stats import normaltest
from datetime import datetime

# just for 99th percentile
dirHome = "G:\\report\\year-3\\07-Fall-2020\\#3Paper\\data\\"\
        "trend-analysis\\data\\03-obsSurge\\percentiles\\99"

dirPlot = "G:\\report\\year-3\\07-Fall-2020\\#3Paper\\data\\"\
        "trend-analysis\\data\\03-obsSurge\\plots\\99"

dirOut = "G:\\report\\year-3\\07-Fall-2020\\#3Paper\\data\\"\
        "trend-analysis\\data\\03-obsSurge\\trends\\99"


def getTrends():
    """ 
    this function computes the trends after 
    """
    os.chdir(dirHome)

    tgList = os.listdir()

    # create empty dataframe
    df = pd.DataFrame(columns = ['tg', 'lon', 'lat', 'normality', 'trend(mm/year)', 'pval'])

    for tg in tgList:

        os.chdir(dirHome)

        print(tg)

        # load data
        dat = pd.read_csv(tg)

        # get only 1950 onward data
        if dat['year'][0] > 1950:
            continue 
        else:
            dat = dat[(dat['year'] >= 1950) & (dat['year'] <= 2015)]
            # check completeness of 75% for 1950-2010 there are 61 years - 46 is 75%
            if len(dat) < 46:
                continue

        # # plot time series and save
        # # plotIt(dat, tg)

        # # set restrictions on data availability 
        # # only take tg with more than 25 years - reproduce martha's results
        # if (len(dat) <= 25):
        #     continue 

        lon = dat['lon'].unique()[0]
        lat = dat['lat'].unique()[0]

        shapiro, dagosto = checkNormality(dat['value'])

        # decide to do normality check or not
        # if (shapiro <= 0.05) or (dagosto <= 0.05): # original statement
        # if (shapiro > 100) or (dagosto > 100): # to include non-normal data
        if (shapiro > 1000) or (dagosto > 1000):
            # failed either one of normality tests
            newDf = pd.DataFrame([tg, lon, lat, False, np.nan, np.nan]).T
            newDf.columns = ['tg', 'lon', 'lat', 'normality', 'trend(mm/year)', 'pval']
            df = pd.concat([df, newDf])
        else:
            annualTrend, pval = simpleReg(dat)
            newDf = pd.DataFrame([tg, lon, lat, True, annualTrend, pval]).T
            newDf.columns = ['tg', 'lon', 'lat', 'normality', 'trend(mm/year)', 'pval']
            df = pd.concat([df, newDf])
    
    print(df)

    # check significance at 95% confidence level
    df['significance'] = (~df['pval'].isnull()) & (df['pval'] <= 0.05)

    print(df)

    # save file
    os.chdir(dirOut)
    df.to_csv("ObsSurge99thPercTrends_no_normalityCheck_v2.csv")
    



def checkNormality(x):
    """ checks normality of the time series """
    shapiro_test = stats.shapiro(x) # shapiro test
    stat, p = normaltest(x) # D'Agostino test

    # print("shapiro pvalue = {}".format(shapiro_test.pvalue))
    # print("D'Agostino pvalue = {} \n".format(p))

    return shapiro_test.pvalue, p

def simpleReg(dat):
    """ implements simple linear regression """
    x = dat['year']
    y = dat['value']

    x2 = sm.add_constant(x)
    est = sm.OLS(y, x2)
    est2 = est.fit()

    # print("pvalue = {}".format(est2.pvalues[1]))
    # print(est2.summary())
    return est2.params[1]*1000, est2.pvalues[1] # returns coefficient of year in mm

def plotIt(dat, tg):
    # plot data
    plt.figure(figsize=(10,4))
    plt.plot(dat['year'], dat['value'])
    plt.scatter(dat['year'], dat['value'], color = "blue")
    plt.title(tg)

    os.chdir(dirPlot)
    plt.savefig(tg+".jpg")
    plt.close('all')
    # plt.show()


# fun function
getTrends()