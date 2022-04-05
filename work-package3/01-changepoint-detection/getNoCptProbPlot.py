# -*- coding: utf-8 -*-
"""
Created on Fri Jan 29 09:00:43 2021

plot tide gauges with no changepoints
for a given probability - p25, 

@author: Michael Tadesse
"""
#add libraries
import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
#locate the file that basemap needs
os.environ["PROJ_LIB"] = "C:\\Users\\WahlInstall\\Anaconda3\\Library\\share\\basemap"
from mpl_toolkits.basemap import Basemap

home = "D:\\OneDrive - Knights - University of Central Florida\\UCF\\Projekt.28\\Report\\07-Fall-2020\\#3Paper\\data\\changePointTimeSeries\\20crBCPProb"
os.chdir(home)


def plotNoCPT(param):
    """
    param : minimum probability that the given year
            is not a changepoint
    
    "75%" : changepoint detected with p <= 0.25
    "50%" : changepoint detected with p <= 0.5
    "25%" : changepoint detected with p <= 0.75 
    
    """
    #define probability dictionary
    p = {'75%' : "noCptP75.csv", 
         '50%' : "noCptP50.csv", 
         '25%' : "noCptP25.csv"}
    
    orgnYear = 1836;
    
    dat = pd.read_csv(p[param]);
    
 

    #################################
    #if no changepoint -> year = 1900
    #################################
    dat[['p25','p50','p75']].fillna(orgnYear, inplace = True);
    
    
    #plotting
    
    sns.set_context('notebook', font_scale = 1.5)
    
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
                'orangered')
    
    title = "Tide Gauges with no changepoint: p >= " + param
    plt.title(title)
    
    # saveName = "noCPT" + param + "20cr.svg";
    # plt.savefig(saveName, dpi=400)
    