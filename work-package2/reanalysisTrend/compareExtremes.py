# -*- coding: utf-8 -*-
"""
Created on Tue Aug 11 11:43:56 2020

compare the extremes in observed and reconstructed
surges for a longer period of time

@author: Michael Tadesse
"""
import os 
import pandas as pd


def getExtremes(timeSeries, percentile):
    """
    this function gets the extremes in the 
    observation and their corresponding
    reconstructed values
    """
    years = timeSeries['year'].unique()
    extremes = pd.DataFrame(columns = ['year','meanPercObs', 'stdPercObs', 
                                       'meanPercRecon', 'stdPercRecon'])
    for ii in range(0, len(years)):
        currentYear = timeSeries[timeSeries['year'] == years[ii]]
        currentExtremes = currentYear[currentYear['surge'] >= currentYear['surge'].quantile(0.01*percentile)]
        currentData = pd.DataFrame([years[ii], currentExtremes['surge'].mean(),
                                    currentExtremes['surge'].std(),
                                    currentExtremes['surge_reconsturcted'].mean(),
                                    currentExtremes['surge_reconsturcted'].std()]).T
        currentData.columns = ['year','meanPercObs', 'stdPercObs', 
                                       'meanPercRecon', 'stdPercRecon']
        extremes = pd.concat([extremes, currentData], axis = 0)
    return extremes
        
        
    

def loadTimeSeries(tideGauge, reanalysis):
    """
    this function loads a time series
    for the chosen tide gauge
    
    tideGauge = ['victoria', 'fremantle', 'brest', 'atlanticCity']
    reanalysis = ['Twcr', 'Era20c']
    """
    os.chdir("G:\\data\\reanalysisTrendFiles\\reconSurgeFiles")
    dat = pd.read_csv(tideGauge+reanalysis+"Merged.csv")
    # dat.drop(['Unnamed: 0', 'index', 'Unnamed: 0.1'], axis = 1, inplace = True)
    return dat