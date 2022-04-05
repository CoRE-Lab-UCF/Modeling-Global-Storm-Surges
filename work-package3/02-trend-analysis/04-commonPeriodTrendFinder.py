import os
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib
from scipy import stats
import statsmodels.api as sm
import matplotlib.pyplot as plt
#locate the file that basemap needs
os.environ["PROJ_LIB"] = "C:\\Users\\WahlInstall\\"\
    "Anaconda3\\Library\\share\\basemap"
from mpl_toolkits.basemap import Basemap
from mpl_toolkits.axes_grid.inset_locator import inset_axes


dirHome = {
    "twcr" : "G:\\report\\year-3\\07-Fall-2020\\#3Paper\\data\\"\
        "trend-analysis\\data\\01-twcr",
    "era20c" : "G:\\report\\year-3\\07-Fall-2020\\#3Paper\\data\\"\
        "trend-analysis\\data\\02-era20c"
}


dirOut = {
    "twcr" : "G:\\report\\year-3\\07-Fall-2020\\#3Paper\\data\\"\
        "trend-analysis\\data\\01-twcr\\03-commonPeriodTrend",
    "era20c" : "G:\\report\\year-3\\07-Fall-2020\\#3Paper\\data\\"\
        "trend-analysis\\data\\02-era20c\\03-commonPeriodTrend"
}



def getPercentile(recon, tg, perc):
    """  
    get the specified percentile surge for the given
    tg and recon 
    """
    os.chdir(os.path.join(dirHome[recon], "02-percentiles", str(perc)))
    percDat = pd.read_csv(tg)
    
    return percDat

def getTgList(recon, year):
    """  
    this function gets the tgs from the specified
    reconstruction and year
    recon = {twcr, era20c}
    """
    os.chdir(dirHome[recon])
    dat = pd.read_csv("{}VI.csv".format(recon))
    # print(dat)

    # filter based on year
    tgList = dat[dat['visual_inspection'] <= str(year)][['tg', 'visual_inspection']] 
    
    return tgList

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

def getTrends(recon, perc, yr):
    """  
    get trends for all tgs under the given recon
    with the specified perc and starting year, yr
    """
    # get tg with cpt <= yr
    tgList = getTgList(recon, yr)
    
    # create empty dataframe
    df = pd.DataFrame(columns = ['tg', 'lon', 'lat', 'normality', 'trend(mm/year)', 'pval'])

    for tg in tgList['tg']:
        print(tg)

        # get percentile data for each tg
        percDat = getPercentile(recon, tg, perc)
    
        # filter only data >= yr
        dat = percDat[percDat['year'] >= yr]
        # print(dat)

        lon = dat['lon'].unique()[0]
        lat = dat['lat'].unique()[0]

        # apply simple linear regression trend calculation
        annualTrend, pval = simpleReg(dat)
        newDf = pd.DataFrame([tg, lon, lat, "nan", annualTrend, pval]).T
        newDf.columns = ['tg', 'lon', 'lat', 'normality', 'trend(mm/year)', 'pval']
        df = pd.concat([df, newDf])


    # check significance at 95% confidence level
    df['significance'] = (~df['pval'].isnull()) & (df['pval'] <= 0.05)

    # save as csv
    os.chdir(dirOut[recon])
    df.to_csv("{}{}_{}PercTrends.csv".format(recon,yr,perc))



    
# run function
getTrends("twcr", 99, 1875)