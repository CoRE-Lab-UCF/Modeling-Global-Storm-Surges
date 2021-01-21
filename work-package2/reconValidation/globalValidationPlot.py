# -*- coding: utf-8 -*-
"""
Created on Wed Jul 9 11:00:00 2020

To plot validations for reanalysis datasets

@author: Michael Tadesse
"""

#add libraries
import os
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
#locate the file that basemap needs
os.environ["PROJ_LIB"] = "C:\\Users\\WahlInstall\\Anaconda3\\Library\\share\\basemap"
from mpl_toolkits.basemap import Basemap

def plotIt(reanalysis, metric):
    """
    this function organizes validation files
    and plots them

    reanalysis: {twcr, era20c, eraint, merra}
    metric: {corr, rmse}
    
    returns a plot of the validation and the 
    aggregated dataframe based on latitude
    
    """
    
    #increase plot font size
    sns.set_context('notebook', font_scale = 1.5)
    
    #dictionary for datasets
    data = {'twcr': ["twcr19802010Validation.csv", "20CR"],
            'era20c': ["era20c19802010Validation.csv", "ERA20C"],
            'eraint':["eraint19802010Validation.csv", "ERA-Interim"],
            'merra': ["merra19802010Validation.csv", "MERAA"]
            }
    
    metrics = {'corr': ["corrn", "Pearson's Correlation"],
               'rmse': ["rmse", "RMSE(m)"]
               }
    
    #cd to the validation directory
    os.chdir("D:\\data\\allReconstructions\\validation\\commonPeriodValidation")
    
    #load validation files
    dat = pd.read_csv(data[reanalysis][0])
    
    #plotting
    plt.figure(figsize=(20, 10))
    m=Basemap(projection='cyl', lat_ts=20, llcrnrlon=-180, 
              urcrnrlon=180,llcrnrlat=-90,urcrnrlat=90, resolution='c')
    x,y = m(dat['lon'].tolist(), dat['lat'].tolist())
    m.drawcoastlines()
    
    #draw parallels and meridians 
    parallels = np.arange(-80,81,20.)
    m.drawparallels(parallels,labels=[True,False,False,False], linewidth = 0)
    
    m.bluemarble(alpha = 0.8) #basemap , alpha = transparency
    plt.scatter(x, y, 70, marker = 'o', edgecolors = 'black', c = 
                dat[metrics[metric][0]], cmap = 'hot_r')
    m.colorbar(location = 'bottom')

    if metric == "corr":
        plt.clim(0, 1)
    else:
        plt.clim(0,0.4)
        
    title = data[reanalysis][1] + " - " + metrics[metric][1]
    plt.title(title)
        
    datAggregated = scoreAggregate(dat)
    
    #plot corresponding latitudinally aggregated figure
    barPlotIt(datAggregated, metric, title)
    
    return datAggregated
    

def scoreAggregate(dat):
    """
    aggregates correlation and rmse
    scores of the reanalysis spatially
    """
    #set band column as nan to start
    dat['band'] = 'nan'
    
    for ii in range(0, len(dat)):
        if dat['lat'][ii] >= -90 and  dat['lat'][ii] <= -85:
            dat['band'][ii] = -90
        elif dat['lat'][ii] > -85 and  dat['lat'][ii] <= -75:
            dat['band'][ii] = -80   
        elif dat['lat'][ii] > -75 and  dat['lat'][ii] <= -65:
            dat['band'][ii] = -70        
        elif dat['lat'][ii] > -65 and  dat['lat'][ii] <= -55:
            dat['band'][ii] = -60    
        elif dat['lat'][ii] > -55 and  dat['lat'][ii] <= -45:
            dat['band'][ii] = -50
        elif dat['lat'][ii] > -45 and  dat['lat'][ii] <= -35:
            dat['band'][ii] = -40
        elif dat['lat'][ii] > -35 and  dat['lat'][ii] <= -25:
            dat['band'][ii] = -30
        elif dat['lat'][ii] > -25 and  dat['lat'][ii] <= -15:
            dat['band'][ii] = -20
        elif dat['lat'][ii] > -15 and  dat['lat'][ii] <= -5:
           dat['band'][ii] = -10
        elif dat['lat'][ii] > -5 and  dat['lat'][ii] <= 5:
            dat['band'][ii] = 0
        elif dat['lat'][ii] > 5 and  dat['lat'][ii] <= 15:
            dat['band'][ii] = 10
        elif dat['lat'][ii] > 15 and  dat['lat'][ii] <= 25:
            dat['band'][ii] = 20
        elif dat['lat'][ii] > 25 and  dat['lat'][ii] <= 35:
            dat['band'][ii] = 30
        elif dat['lat'][ii] > 35 and  dat['lat'][ii] <= 45:
            dat['band'][ii] = 40
        elif dat['lat'][ii] > 45 and  dat['lat'][ii] <= 55:
            dat['band'][ii] = 50
        elif dat['lat'][ii] > 55 and  dat['lat'][ii] <= 65:
            dat['band'][ii] = 60
        elif dat['lat'][ii] > 65 and  dat['lat'][ii] <= 75:
            dat['band'][ii] = 70
        elif dat['lat'][ii] > 75 and  dat['lat'][ii] <= 85:
            dat['band'][ii] = 80
        elif dat['lat'][ii] > 85 and  dat['lat'][ii] <= 90:
            dat['band'][ii] = 90
        
    return dat

    
def barPlotIt(dat, metric, title):
    """
    to plot the horizontal barplots for 
    reanalysis datasets
    
    metric: corr, rmse
    
    """
    #increase plot font size
    sns.set_context('notebook', font_scale = 1.5)
    
    bandGrouped = dat.groupby('band')
    if metric == 'corr':
        requestedMetric = bandGrouped.corrn.mean()
        xLabel = "Pearson's Correlation"

    else:
        requestedMetric = bandGrouped.rmse.mean()
        xLabel = "RMSE (m)"
    
    labels, counts  = np.unique(dat['band'], return_counts = True)
    plt.figure(figsize=(10, 10))
    sns.barplot(x = requestedMetric, y = labels, orient = 'h')
    plt.xlim(reversed(plt.xlim()))
    plt.gca().invert_xaxis()
    plt.xlabel(xLabel)
    #invert y axis
    plt.gca().invert_yaxis() 
    if metric == 'corr':
        plt.xlim([0,1])
    else:
        plt.xlim([0,0.18])
    plt.title(title)
    
    


