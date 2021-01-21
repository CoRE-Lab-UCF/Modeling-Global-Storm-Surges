# -*- coding: utf-8 -*-
"""
Created on Wed Jul 14 10:00:00 2020

To validate reconstruction between 1980-2010

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

    data = ["twcr", "era20c", "eraint", "merra"]
    """
    reconPath = {
        "twcr": "E:\\03_20cr\\08_20cr_surge_reconstruction\\bestReconstruction\\surgeReconstructed",
        "era20c": "F:\\02_era20C\\08_era20C_surge_reconstruction\\bestReconstruction\\surgeReconstructed",
        "eraint": "F:\\01_erainterim\\08_eraint_surge_reconstruction\\bestReconstruction\\surgeReconstructed",
        "merra": "G:\\04_merra\\08_merra_surge_reconstruction\\bestReconstruction\\surgeReconstructed"
        }

    surgePath = "D:\\data\\allReconstructions\\05_dmax_surge_georef"
    outPath = "D:\\data\\allReconstructions\\validation\\commonPeriodValidation"

    os.chdir(reconPath[data])

    tg_list = os.listdir()    

    #empty dataframe for model validation
    df = pd.DataFrame(columns = ['tg', 'lon', 'lat', 'reanalysis','corrn', 'rmse'])

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
        #print(surgeSubset)
        os.chdir("E:\\03_20cr\\07_sonstig")
        #surgeSubset.to_csv("abashiriReconObs.csv")
        #implement validation
        corr, rmse = getMetrics(surgeSubset)[0], getMetrics(surgeSubset)[1]

        new_df = pd.DataFrame([tg, longitude, latitude, data, corr, rmse]).T
        new_df.columns = ['tg', 'lon', 'lat', 'reanalysis','corrn', 'rmse']

        df = pd.concat([df, new_df], axis = 0)
        #print(df)
    
    os.chdir(outPath)
    saveName = data+"19802010Validation.csv"
    df.to_csv(saveName)

def subsetFiles(reconSurge, obsSurge):
    """
    this function subsets the reconstructed surge
    and observed surge for the 1980-2010 period
    """
    #get extra column that is only ymd
    ymdMaker = lambda x: x[0:10]
    reconSurge['ymd'] = pd.DataFrame(list(map(ymdMaker, reconSurge['date'])))
    obsSurge['ymd'] = pd.DataFrame(list(map(ymdMaker, obsSurge['date'])))

    reconSurge = reconSurge[(reconSurge['ymd'] >= '1980-01-03') & (reconSurge['ymd'] < '2011-01-01')]
    obsSurge = obsSurge[(obsSurge['ymd'] >= '1980-01-03') & (obsSurge['ymd'] < '2011-01-01')]
    
    #merge reconSurge and obsSurge on 'ymd'
    surgeMerged = pd.merge(reconSurge, obsSurge, on='ymd', how='left')
    
    ##remove NANs
    row_nan = surgeMerged[surgeMerged.isna().any(axis =1)]
    surgeMerged.drop(row_nan.index, axis = 0, inplace = True)
    surgeMerged.reset_index(inplace = True)
    surgeMerged.drop('index', axis = 1, inplace = True)   

    ##save subsetted timeseries in a new variable
    surgeMerged = surgeMerged[['ymd', 'lon_x', 'lat_x', 'surge_reconsturcted', 'surge']]

    # print(reconSurge.columns)
    # print(obsSurge.columns)
    return surgeMerged

def getMetrics(surgeMerged):
    """
    this function calculates the correlation, RMSE
    metrics for reconstructed and observed surge
    """
    #print(surgeMerged)

    if surgeMerged.empty:
        print("no common period")
        metricCorr = 'nan'
        metricRMSE = 'nan'
    else:
        metricCorr = stats.pearsonr(surgeMerged['surge_reconsturcted'], surgeMerged['surge'])[0]
        metricRMSE = np.sqrt(metrics.mean_squared_error(surgeMerged['surge_reconsturcted'], surgeMerged['surge']))

    return metricCorr, metricRMSE
