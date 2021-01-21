# -*- coding: utf-8 -*-
"""
Created on Fri Jul 24 09:47:48 2020

To plot variance of validation metrics

@author: Michael Tadesse
"""
import os
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
#locate the file that basemap needs
os.environ["PROJ_LIB"] = "C:\\Users\\WahlInstall\\Anaconda3\\Library\\share\\basemap";
from mpl_toolkits.basemap import Basemap


def plotMetricVariance(metric):
    """
    this function plots the variance of 
    the validation metrics for the reconstructed
    surges
    """
    
    #directories for the common period validation
    csvPath = "G:\\data\\allReconstructions\\validation\\commonPeriodValidation"
    os.chdir(csvPath)
    
    #define validation output files
    validationFiles = {'corr' : 'allCorrelationMetricVariance.csv', 'rmse' : 'allRMSEMetricVariance.csv',
                       'nnse' : 'allNSEMetricVariance_v2.csv',
                       'rrmse':'RRMSEOnly.csv'}
    
    chosenMetric = validationFiles[metric]
    
    #read the validation file of choice
    dat = pd.read_csv(chosenMetric)
    #compute standard deviation of metrics for all reanalysis
    # metricColumns = dat[['20CR', 'ERA-20c', 'ERA-Interim', 'MERRA', 'ERA-FIVE']]
    # metricColumns.to_csv('justMetrics.csv')
    #dat['metricStd'] = np.std(metricColumns, axis = 1)
    # dat.to_csv("metricSTDNse.csv")


    #plotting
    if metric == 'corr':
        dat['Metric STD'] = dat['Metric Variance']**0.5
        bubbleSize = 500
        title = 'Pearson\'s Correlation - Variation of Model Accuracy among Reanalyses'
    elif metric == 'rmse':
        #multiply by 100 to get values in cms
        dat['Metric STD'] = 100*dat['Metric Variance']**0.5
        bubbleSize = 60 
        title = 'RMSE - Metric Variation of Model Accuracy among Reanalyses (cm)'
    elif metric == 'rrmse':
        dat['Metric STD'] = dat['metricSTD']
        bubbleSize = 60 
        title = 'RRMSE - Metric Variation of Model Accuracy among Reanalyses (cm)'
    else:
        dat['Metric STD'] = dat['metricSTD']
        bubbleSize = 1500
        title = 'NNSE - Variation of Model Accuracy among Reanalyses'
        
    sns.set_context('notebook', font_scale = 1.5)
    
    plt.figure(figsize=(20, 10))
    m=Basemap(projection='cyl', lat_ts=20, llcrnrlon=-180, 
              urcrnrlon=180,llcrnrlat=-90,urcrnrlat=90, resolution='c')
    x,y = m(dat['lon'].tolist(), dat['lat'].tolist())
    m.drawcoastlines()
    
    #draw parallels and meridians 
    parallels = np.arange(-80,81,20.)
    m.drawparallels(parallels,labels=[True,False,False,False], linewidth = 0)
    
    #define bubble sizes
    minSize = min(dat['Metric STD'])*bubbleSize
    maxSize = max(dat['Metric STD'])*bubbleSize
    
    m.bluemarble(alpha = 0.8)
    sns.scatterplot(x = x, y = y, color = 'red', 
                    size = 'Metric STD', hue = 'Reanalysis',
                    sizes = (minSize, maxSize), palette = {'ERA-Interim':'black', 'ERA-FIVE':'cyan', 'MERRA':'red', 
                               'ERA-20c':'magenta', '20CR':'green'}
                    ,data = dat)
    plt.title(title)
    os.chdir('G:\\data\\allReconstructions\\validation\\commonPeriodValidation\\plotFiles')
    saveName = 'allReanalyses'+metric+'STD.svg'
    plt.savefig(saveName, dpi = 400)