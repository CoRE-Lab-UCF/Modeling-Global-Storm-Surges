# -*- coding: utf-8 -*-
"""
Created on Wed Oct 21 09:16:00 2020

To validate extreme surges reconstruction

@author: Michael Tadesse
"""
#import libraries
import os 
import numpy as np
import pandas as pd 
from scipy import stats
from sklearn import metrics


def getFiles(data):
    """
    this function gets the reconstruction time
    series and the observed surge time series

    data = ["twcr", "era20c", "eraint", "merra", "erafive"]
    """
    reconPath = {
        "twcr": "G:\\data\\allReconstructions\\01_20cr",
        "era20c": "G:\\data\\allReconstructions\\02_era20c",
        "eraint": "G:\\data\\allReconstructions\\03_erainterim",
        "merra": "G:\\data\\allReconstructions\\04_merra",
        "erafive": "G:\\data\\allReconstructions\\05_era5"
        }

    surgePath = "G:\\data\\allReconstructions\\06_dmax_surge_georef"
    outPath = "G:\\data\\allReconstructions\\validation\\eXtremes"

    os.chdir(reconPath[data])

    tg_list = os.listdir()    

    #empty dataframe for model validation
    df = pd.DataFrame(columns = ['tg', 'lon', 'lat', 'reanalysis','corrn', 'rmse', 'nnse'])

    for ii in range(0, len(tg_list)): 
        tg = tg_list[ii]
        print(tg, '\n')
        #get reconstruction
        os.chdir(reconPath[data])
        reconSurge = pd.read_csv(tg)
        ##remove duplicated rows
        reconSurge.drop(reconSurge[reconSurge['date'].duplicated()].index, axis = 0, inplace = True)
        reconSurge.reset_index(inplace = True)
        reconSurge.drop('index', axis = 1, inplace = True)

        #get surge time series
        os.chdir(surgePath)
        obsSurge = pd.read_csv(tg)
        longitude = obsSurge['lon'][0]
        latitude = obsSurge['lat'][0]
        
        ##remove duplicated rows
        obsSurge.drop(obsSurge[obsSurge['date'].duplicated()].index, axis = 0, inplace = True)
        obsSurge.reset_index(inplace = True)
        obsSurge.drop('index', axis = 1, inplace = True)

        #implement subsetting
        surgeSubset = subsetFiles(reconSurge, obsSurge)
        if surgeSubset.empty:
            continue
        #get extremes 
        surgeExtremes = getExtremes(surgeSubset)

        #implement validation
        corr, rmse, nnse = getMetrics(surgeExtremes)[0], getMetrics(surgeExtremes)[1], getNNSE(surgeExtremes)

        new_df = pd.DataFrame([tg, longitude, latitude, data, corr, rmse, nnse]).T
        new_df.columns = ['tg', 'lon', 'lat', 'reanalysis','corrn', 'rmse', 'nnse']

        df = pd.concat([df, new_df], axis = 0)
        # print(df)
    
    os.chdir(outPath)
    saveName = data+"ValidationExtremes.csv"
    df.to_csv(saveName)

def subsetFiles(reconSurge, obsSurge):
    """
    this function subsets the reconstructed surge
    and observed surge for the entire period
    """
    #get extra column that is only ymd
    ymdMaker = lambda x: x[0:10]
    reconSurge['ymd'] = pd.DataFrame(list(map(ymdMaker, reconSurge['date'])))
    obsSurge['ymd'] = pd.DataFrame(list(map(ymdMaker, obsSurge['date'])))

    # reconSurge = reconSurge[(reconSurge['ymd'] >= '1980-01-03') & (reconSurge['ymd'] < '2011-01-01')]
    # obsSurge = obsSurge[(obsSurge['ymd'] >= '1980-01-03') & (obsSurge['ymd'] < '2011-01-01')]

    #merge reconSurge and obsSurge on 'ymd'
    surgeMerged = pd.merge(reconSurge, obsSurge, on='ymd', how='left')
    
    ##remove NANs
    row_nan = surgeMerged[surgeMerged.isna().any(axis =1)]
    surgeMerged.drop(row_nan.index, axis = 0, inplace = True)
    surgeMerged.reset_index(inplace = True)
    surgeMerged.drop('index', axis = 1, inplace = True)   

    ##save subsetted timeseries in a new variable
    surgeMerged = surgeMerged[['ymd', 'lon_x', 'lat_x', 'surge_reconsturcted', 'surge']]

    return surgeMerged

def getExtremes(dat):
    """
    this function returns the 95th percentile
    threshold
    """
    ##get unique year values
    #get the year
    getYear = lambda x: x.split('-')[0]
    dat['year'] = pd.DataFrame(list(map(getYear, dat['ymd'])))
    years = dat['year'].unique()
    
    perc95 = pd.DataFrame(columns=['ymd', 'lon_x', 'lat_x', 
                                     'surge_reconsturcted', 'surge', 'year'])
    ##for each year extract values above 95th percentile
    for yr in years:
        currentYear = dat[dat['year'] == yr]
        # print(currentYear)
        perc95 = pd.concat([perc95, currentYear[currentYear['surge'] 
                >= np.percentile(currentYear['surge'], 95)]], axis = 0)
    
    return perc95

def getMetrics(surgeMerged):
    """
    this function calculates the correlation, RMSE
    metrics for reconstructed and observed surge
    """

    if (surgeMerged.empty):
        print("no common period")
        metricCorr = 'nan'
        metricRMSE = 'nan'
    else:
        pval = stats.pearsonr(surgeMerged['surge_reconsturcted'], surgeMerged['surge'])[1]
        print(pval)

        if pval >= 0.05:
            print("pval >= 0.05")
            metricCorr = 'nan'
            metricRMSE = 'nan'
        else:
            metricCorr = stats.pearsonr(surgeMerged['surge_reconsturcted'], surgeMerged['surge'])[0]
            metricRMSE = np.sqrt(metrics.mean_squared_error(surgeMerged['surge_reconsturcted'], surgeMerged['surge']))

    return metricCorr, metricRMSE

#added NSE metric computation
def getNNSE(surgeMerged):
    """
    this function computes the normalized Nash-Sutcliffe
    Efficiency (NNSE)
    """
    if surgeMerged.empty:
        print("no common period")
        metricNSE = 'nan'
    else:
        numerator = sum((surgeMerged['surge_reconsturcted'] - surgeMerged['surge'])**2)
        denominator = sum((surgeMerged['surge'] - surgeMerged['surge'].mean())**2)
        metricNSE = 1 - (numerator/denominator)
        metricNNSE = 1/(2 - metricNSE)

    return metricNNSE


#run function
getFiles("erafive")