# -*- coding: utf-8 -*-
"""
Created on Wed Jul 15 11:22:00 2020

To plot reanalysis reconstruction timeseries

@author: Michael Tadesse
"""
#get libraries
import os 
import pandas as pd 
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from datetime import datetime

# #define a plot object that can be manipulated
#update the rows of the subplot here 
fig, ax = plt.subplots(2, 1, figsize=(16, 10))
fig.tight_layout(pad = 0.8)

def timeSeriesPlotter(tideGauge, data, row):
    """
    this function organizes five functions 
    to plot surge reconstruction
    
    tideGauge: name of the tide gauge with out .csv extension
    data = ["twcr", "era20c", "eraint", "merra", "erafive"]
    row: where to place the time series on the subplot
    
    the subplot object is defined above - manually add
    plots to it by changing the row argument and the name
    of the tide gauge
    """
    getFiles(tideGauge, data, row)


def getFiles(tideGauge, data, row):
    """
    this function gets the reconstruction time
    series and the observed surge time series

    tideGauge: name of the tide gauge with out .csv extension
    data = ["twcr", "era20c", "eraint", "merra"]
    """
    reconPath = {
        "twcr": "G:\\data\\allReconstructions\\01_20cr",
        "era20c": "G:\\data\\allReconstructions\\02_era20c",
        "eraint": "G:\\data\\allReconstructions\\03_erainterim",
        "merra": "G:\\data\\allReconstructions\\04_merra",
        "erafive": "G:\\data\\allReconstructions\\05_era5"
        }

    surgePath = "G:\\data\\allReconstructions\\06_dmax_surge_georef"

    tg = tideGauge+".csv"
    print(tg, '\n')

    surgeTwcr, surgeEra20c, surgeEraint, surgeMerra, surgeEra5 = [],[],[],[],[]
    #get reconstructed surge
    for ii in data:
        if ii == 'twcr':
            os.chdir(reconPath[ii])
            surgeTwcr = getReconSurge(tg)
        elif ii == 'era20c':
            os.chdir(reconPath[ii])
            surgeEra20c = getReconSurge(tg)
        elif ii == 'eraint':
            os.chdir(reconPath[ii])
            surgeEraint = getReconSurge(tg)
        elif ii == 'merra':
            os.chdir(reconPath[ii])
            surgeMerra = getReconSurge(tg)
        elif ii == 'erafive':
            os.chdir(reconPath[ii])
            surgeEra5 = getReconSurge(tg)
        else:
            "there is a problem!"

    #get observed surge
    os.chdir(surgePath)
    obsSurge = getObsSurge(tg)

    #print(obsSurge)
    getTimeStamp(surgeTwcr, surgeEra20c, surgeEraint, surgeMerra, surgeEra5, obsSurge, 
                 row, tideGauge)

def getReconSurge(tg):
    """
    to get the reconstruction surge 
    """
    #get reconstruction
    reconSurge = pd.read_csv(tg)
    ##remove duplicated rows
    reconSurge.drop(reconSurge[reconSurge['date'].duplicated()].index, 
                    axis = 0, inplace = True)
    reconSurge.reset_index(inplace = True)
    reconSurge.drop('index', axis = 1, inplace = True)

    return reconSurge

def getObsSurge(tg):
    """
    to get the observed surge
    """
    #get surge time series
    obsSurge = pd.read_csv(tg)
    ##remove duplicated rows
    obsSurge.drop(obsSurge[obsSurge['date'].duplicated()].index, axis = 0, 
                  inplace = True)
    obsSurge.reset_index(inplace = True)
    obsSurge.drop('index', axis = 1, inplace = True)

    return obsSurge

def getTimeStamp(surgeTwcr, surgeEra20c, surgeEraint, surgeMerra, surgeEra5, obsSurge, row, 
                 tideGauge):
    """
    this function prepares the time column of the time series
    to make it easy to plot
    """

    #define lambda functions 
    time_stamp = lambda x: (datetime.strptime(x, '%Y-%m-%d %H:%M:%S'))
    time_stamp_surge = lambda x: (datetime.strptime(x, '%Y-%m-%d'))

    if len(surgeTwcr) != 0:
        surgeTwcr['date'] = pd.DataFrame(list(map(time_stamp, surgeTwcr['date'])), 
                                         columns = ['date'])
    if len(surgeEra20c) != 0:
        surgeEra20c['date'] = pd.DataFrame(list(map(time_stamp, surgeEra20c['date'])), 
                                           columns = ['date'])
    if len(surgeEraint) != 0:
        surgeEraint['date'] = pd.DataFrame(list(map(time_stamp, surgeEraint['date'])), 
                                           columns = ['date'])
    if len(surgeMerra) != 0 :
        surgeMerra['date'] = pd.DataFrame(list(map(time_stamp, surgeMerra['date'])), 
                                          columns = ['date'])
    if len(surgeEra5) != 0 :
        surgeEra5['date'] = pd.DataFrame(list(map(time_stamp, surgeEra5['date'])), 
                                          columns = ['date'])
    if len(obsSurge) != 0:
        obsSurge['date'] = pd.DataFrame(list(map(time_stamp_surge, obsSurge['ymd'])), 
                                        columns = ['date'])

    
    #calling the plotter function
    plotTimeSeries(surgeTwcr, surgeEra20c, surgeEraint, surgeMerra, surgeEra5,
                   obsSurge, row, tideGauge)
    

def plotTimeSeries(surgeTwcr, surgeEra20c, surgeEraint, surgeMerra, surgeEra5,
                   obsSurge, row, tideGauge):
    """
    this function plots a time series making use of 
    all reconstructed surge data from reanalyses
    """
    if len(obsSurge) != 0:
        ax[row].plot(obsSurge['date'], obsSurge['surge'], 'o', color = "blue", 
                   label = "observation", lw = 4)
    if len(surgeTwcr) != 0:
        ax[row].plot(surgeTwcr['date'], surgeTwcr['surge_reconsturcted'], 
                   color = "green", label = "twcr", lw = 3)
        ax[row].fill_between(surgeTwcr['date'], surgeTwcr['pred_int_lower'], 
                           surgeTwcr['pred_int_upper'], color = 'lightgreen', 
                           alpha = 0.4)
    if len(surgeEra20c) != 0:
        ax[row].plot(surgeEra20c['date'], surgeEra20c['surge_reconsturcted'], 
                   color = "magenta", label = "era20c")
        ax[row].fill_between(surgeEra20c['date'], surgeEra20c['pred_int_lower'], 
                           surgeEra20c['pred_int_upper'], color = 'violet', 
                           alpha = 0.4)
        # plt.plot(surgeEra20c['date'], surgeEra20c['pred_int_lower'], 
        #color = "gray", lw = 0.5)
        # plt.plot(surgeEra20c['date'], surgeEra20c['pred_int_upper'], 
    # color = "gray", lw = 0.5)
    if len(surgeEraint) != 0:
        ax[row].plot(surgeEraint['date'], surgeEraint['surge_reconsturcted'], 
                   color = "black", label = "eraint")
        ax[row].fill_between(surgeEraint['date'], surgeEraint['pred_int_lower'],
                           surgeEraint['pred_int_upper'], color = 'gray', 
                           alpha = 0.4)
        # plt.plot(surgeEraint['date'], surgeEraint['pred_int_lower'], 
        # color = "gray", lw = 0.5)
        # plt.plot(surgeEraint['date'], surgeEraint['pred_int_upper'], 
    # color = "gray", lw = 0.5)
    if len(surgeMerra) != 0:
        ax[row].plot(surgeMerra['date'], surgeMerra['surge_reconsturcted'], 
                   color = "red", label = "merra")
        ax[row].fill_between(surgeMerra['date'], surgeMerra['pred_int_lower'], 
                           surgeMerra['pred_int_upper'], color = 'lightsalmon', 
                           alpha = 0.4)
    if len(surgeEra5) != 0:
        ax[row].plot(surgeEra5['date'], surgeEra5['surge_reconsturcted'], 
                   color = "cyan", label = "erafive")
        ax[row].fill_between(surgeEra5['date'], surgeEra5['pred_int_lower'], 
                           surgeEra5['pred_int_upper'], color = 'paleturquoise', 
                           alpha = 0.4)
        # plt.plot(surgeMerra['date'], surgeMerra['pred_int_lower'], 
        
        #color = "gray", lw = 0.5)
        # plt.plot(surgeMerra['date'], surgeMerra['pred_int_upper'], 
    #color = "gray", lw = 0.5)
    
    #define title location
    ax[row].set_title(tideGauge, loc ='left')
    
    
    #set legend
    if row == 0:
        handles, labels = ax[row].get_legend_handles_labels()
        pi_patch = mpatches.Patch(color='darkseagreen', 
                                  label='95% Prediction Interval')
        handles.append(pi_patch)
        plt.legend(handles = handles, ncol = 6)
    