# -*- coding: utf-8 -*-
"""
Created on Thu Jan 28 14:54:14 2021

plot surge reconstruction changepoints
for all tide gauges - era20c results


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

##########
#load file
########## 
home = "D:\\OneDrive - Knights - University of Central Florida\\UCF\\Projekt.28\\Report\\07-Fall-2020\\#3Paper\\data\\changePointTimeSeries\\20crBCPProb"
os.chdir(home)
dat = pd.read_csv('20crBCPProbv2.csv')


def plotCPT(prob):
    """
    prob : {'p25', 'p50', 'p75'}
    """

    #define probability dictionary
    p = {'p25' : 25, 'p50' : 50, 'p75' : 75}    

    #################################
    #if no changepoint -> year = 1900
    #################################
    for ii in range(len(dat)):
        if np.isnan(dat[prob][ii]):
            print('true');
            dat[prob][ii] = 1900;
    
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
                dat[prob], cmap = 'hot_r')
    m.colorbar(location = 'bottom')
    
    title = "Changepoint years with probability of p >= " + str(p[prob]/100)
    plt.title(title)
    
    # saveName = str(prob) + "era20c.svg";
    # plt.savefig(saveName, dpi=400)