# -*- coding: utf-8 -*-
"""
Created on Wed Jul 16 15:00:00 2020

where does each Reanalysis perform best
spatially for extremes?

@author: Michael Tadesse
"""
import os 
import numpy as np
import pandas as pd 
import seaborn as sns
import matplotlib.pyplot as plt
#locate the file that basemap needs
os.environ["PROJ_LIB"] = "C:\\Users\\WahlInstall\\Anaconda3\\Library\\share\\basemap"
from mpl_toolkits.basemap import Basemap

def starter():
    #load the files
    twcrDat, era20cDat, eraintDat, merraDat, erafiveDat = loadData()
    #get metrics for all reanalysis concatented by column
    allCorr = processData(twcrDat, era20cDat, eraintDat, merraDat, erafiveDat)[0]
    allRMSE = processData(twcrDat, era20cDat, eraintDat, merraDat, erafiveDat)[1]
    allNSE = processData(twcrDat, era20cDat, eraintDat, merraDat, erafiveDat)[2]
    # allNSE = allNSE[~(allNSE['NSE(%)'] < 0)]

    return allCorr, allRMSE, allNSE

def plotExtremeGlobal(metric):
    """
    this function plots the chosen metric 
    globallly using the basemap library

    metric = {'corr', 'rmse', 'nse'}

    """
    #call processData here
    if metric == 'corr':
        dat = starter()[0]
        #remove tg that have negative correlation
        dat = dat[~(dat['Correlation'] < 0)] 
        varToPlot = 'Correlation'
        title = 'Pearson\'s Correlation - 1980-2010 - above 95%ile'
        bubbleSizeMultiplier = 250
    elif metric == 'nse':
        dat = starter()[2]
        varToPlot = 'NSE(%)'
        title = 'NSE - 1980-2010'  
        bubbleSizeMultiplier = 900
    else:
        dat = starter()[1]
        varToPlot = 'RMSE(cm)'
        title = 'RMSE(cm) - 1980-2010 - above 95%ile'
        bubbleSizeMultiplier = 4

    #increase plot font size
    sns.set_context('notebook', font_scale = 1.5)
    
    plt.figure(figsize=(20, 10))
    m=Basemap(projection='cyl', lat_ts=20, llcrnrlon=-180, 
              urcrnrlon=180,llcrnrlat=-90,urcrnrlat=90, resolution='c')
    x,y = m(dat['lon'].tolist(), dat['lat'].tolist())
    m.drawcoastlines()

    #draw parallels and meridians 
    parallels = np.arange(-80,81,20.)
    meridians = np.arange(-180.,180.,40.)
    m.drawparallels(parallels,labels=[True,False,False,False], linewidth = 0)
    m.drawparallels(parallels,labels=[True,True,False,False], linewidth = 0.5)
    m.drawmeridians(meridians,labels=[False,False,False,True], linewidth = 0.5)
    m.bluemarble(alpha = 0.8) 
    
    #define markers
    markers = {"20CR": "o", "ERA-20C": "o", "ERA-Interim":'o', "MERRA":'o', "ERA-FIVE":'o'}
    #define palette
    color_dict = dict({'20CR':'green',
                  'ERA-20C':'magenta',
                  'ERA-Interim': 'black',
                  'MERRA': 'red',
                  'ERA-FIVE':'aqua'
                  })
    #define bubble sizes
    minSize = min(dat[varToPlot])*bubbleSizeMultiplier
    if minSize < 0:
        minSize = 0
    maxSize = max(dat[varToPlot])*bubbleSizeMultiplier
    
    sns.scatterplot(x = x, y = y, markers = markers, style = 'Reanalysis',\
                    size = varToPlot, sizes=(minSize, maxSize),\
                        hue = 'Reanalysis',  palette = color_dict, data = dat)
    plt.legend(loc = 'lower left', ncol = 12)
    plt.title(title)
    os.chdir("G:\\data\\allReconstructions\\validation\\commonPeriodValidationExtremes\\percentile\\plotFiles")
    saveName = 'allReanalysesExtremes'+metric+'.svg'
    # plt.savefig(saveName, dpi = 400)



def processData(twcrDat, era20cDat, eraintDat, merraDat, erafiveDat):
    """
    this function cleans and prepares
    the data for plotting
    """
    #merge everything
    twcr_era20c = pd.merge(twcrDat, era20cDat, on='tg', how='left')
    twcr_era20c_eraint = pd.merge(twcr_era20c, eraintDat, on='tg', how='left')
    twcr_era20c_eraint_merra = pd.merge(twcr_era20c_eraint, merraDat, on='tg', how='left')
    twcr_era20c_eraint_merra_erafive = pd.merge(twcr_era20c_eraint_merra, erafiveDat, on='tg', how='left')
    
    # #save merged file
    # twcr_era20c_eraint_merra_erafive.to_csv('allMerged.csv')

    allCorr = twcr_era20c_eraint_merra_erafive[['tg', 'lon', 'lat', 'corrTwcr', 'corrEra20c', \
         'corrEraint', 'corrMerra', 'corrErafive']]
    allCorr.columns = ['tg', 'lon', 'lat', '20CR', 'ERA-20C', 'ERA-Interim', 'MERRA', 'ERA-FIVE']
    
    allRMSE = twcr_era20c_eraint_merra_erafive[['tg', 'lon', 'lat',  'rmseTwcr', 'rmseEra20c',\
         'rmseEraint',  'rmseMerra', 'rmseErafive']]
    allRMSE.columns = ['tg', 'lon', 'lat', '20CR', 'ERA-20C', 'ERA-Interim', 'MERRA', 'ERA-FIVE']
    
    allNSE = twcr_era20c_eraint_merra_erafive[['tg', 'lon', 'lat',  'nseTwcr', 
                                       'nseEra20c','nseEraint',  'nseMerra', 'nseErafive']]
    allNSE.columns = ['tg', 'lon', 'lat', '20CR', 'ERA-20C', 'ERA-Interim', 'MERRA', 'ERA-FIVE']
    #get max corr values 
    allCorr['Correlation'] = allCorr.iloc[:,3:8].max(axis = 1)
    allCorr['Reanalysis'] = allCorr.iloc[:, 3:8].idxmax(axis = 1)
    
    #get min rmse values - change to cms for visibility
    allRMSE['RMSE(cm)'] = allRMSE.iloc[:,3:8].min(axis = 1)*100
    allRMSE['Reanalysis'] = allRMSE.iloc[:, 3:8].idxmin(axis = 1)

    #get max nse values 
    allNSE['NSE(%)'] = allNSE.iloc[:,3:8].max(axis = 1)
    allNSE['Reanalysis'] = allNSE.iloc[:, 3:8].idxmax(axis = 1)

    #filter out NAN rows
    ##remove rows where all reanalysis are nan
    allCorr = allCorr[~allCorr['Correlation'].isna()]
    allRMSE = allRMSE[~allRMSE['RMSE(cm)'].isna()]
    allNSE = allNSE[~allNSE['NSE(%)'].isna()]

    allCorr.to_csv("allCorr.csv")
    allRMSE.to_csv("allRMSE.csv")
    allNSE.to_csv("allNSE.csv")
    
    return allCorr, allRMSE, allNSE

def loadData():
    """
    loads the relevant validation files
    """
    #dictionary for datasets
    data = {'twcr': ["twcr19802010ValidationExtremes95ile.csv", "20CR"],
            'era20c': ["era20c19802010ValidationExtremes95ile.csv", "ERA20C"],
            'eraint':["eraint19802010ValidationExtremes95ile.csv", "ERA-Interim"],
            'merra': ["merra19802010ValidationExtremes95ile.csv", "MERAA"],
            'erafive': ["erafive19802010ValidationExtremes95ile.csv", "MERAA"]
            }
    os.chdir("G:\\data\\allReconstructions\\validation\\commonPeriodValidationExtremes\\percentile")

    twcrDat = pd.read_csv(data['twcr'][0])
    twcrDat.columns = ['deleteIt','tg', 'lon', 'lat', 'reanalysis', 
                       'corrTwcr', 'rmseTwcr', 'nseTwcr']
    era20cDat = pd.read_csv(data['era20c'][0])
    era20cDat.columns = ['deleteIt','tg', 'long', 'latt', 'reanalysis', 
                         'corrEra20c', 'rmseEra20c', 'nseEra20c']
    eraintDat = pd.read_csv(data['eraint'][0])
    eraintDat.columns = ['deleteIt','tg', 'long', 'latt', 'reanalysis', 
                         'corrEraint', 'rmseEraint', 'nseEraint']
    merraDat = pd.read_csv(data['merra'][0])
    merraDat.columns = ['deleteIt','tg', 'long', 'latt', 'reanalysis', 
                        'corrMerra', 'rmseMerra', 'nseMerra']
    erafiveDat = pd.read_csv(data['erafive'][0])
    erafiveDat.columns = ['deleteIt','tg', 'long', 'latt', 'reanalysis', 
                        'corrErafive', 'rmseErafive', 'nseErafive']

    # print(twcrDat)
    return twcrDat, era20cDat, eraintDat, merraDat, erafiveDat 
