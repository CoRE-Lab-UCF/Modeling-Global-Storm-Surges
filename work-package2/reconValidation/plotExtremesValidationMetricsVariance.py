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
    csvPath = "G:\\data\\allReconstructions\\validation\\commonPeriodValidationExtremes\\percentile"
    os.chdir(csvPath)
    
    #define validation output files
    validationFiles = {'corr' : 'allCorr.csv', 'rmse' : 'allRMSE.csv',
                       'nnse' : 'allNNSE.csv', 'rrmse':'RRMSEOnly.csv'}
    
    chosenMetric = validationFiles[metric]
    
    #read the validation file of choice
    dat = pd.read_csv(chosenMetric)
    #compute standard deviation of metrics for all reanalysis
    metricColumns = dat[['20CR', 'ERA-20C', 'ERA-Interim', 'MERRA', 'ERA-FIVE']]
    # metricColumns.to_csv('justMetrics.csv')
    #dat['metricStd'] = np.std(metricColumns, axis = 1)
    # dat.to_csv("metricSTDNse.csv")


    #plotting
    if metric == 'corr':
        dat['Metric STD'] = dat['metricSTD']
        bubbleSize = 800
        title = 'Pearson\'s Correlation - Variation of Model Accuracy among Reanalyses'
    elif metric == 'rmse':
        #multiply by 100 to get values in cms
        dat['Metric STD'] = 100*dat['metricSTD']
        bubbleSize = 4000 
        title = 'RMSE - Metric Variation of Model Accuracy among Reanalyses (cm)'
    elif metric == 'rrmse':
        dat['Metric STD'] = dat['metricSTD']
        bubbleSize = 50
        title = 'RRMSE - Variation of Model Accuracy among Reanalyses'
    else:
        dat['Metric STD'] = dat['metricSTD']
        bubbleSize = 50
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
    minSize = min(dat['metricSTD'])*bubbleSize
    maxSize = max(dat['metricSTD'])*bubbleSize
    
    m.bluemarble(alpha = 0.8)
    sns.scatterplot(x = x, y = y, color = 'red', 
                    size = 'metricSTD', hue = 'Reanalysis',
                    sizes = (minSize, maxSize), 
                    palette = {'ERA-Interim':'black', 'ERA-FIVE':'cyan', 'MERRA':'red', 
                               'ERA-20C':'magenta', '20CR':'green'}
                    ,data = dat)
    plt.title(title)
    os.chdir('D:\\OneDrive - Knights - University of Central Florida\\UCF\\Projekt.28\\Report\\05-Spring-2020\\#2Paper\\p28DataDescriptor\\reView\\figures\\r1c25')
    saveName = 'allReanalyses'+metric+'STD.svg'
    plt.savefig(saveName, dpi = 400)