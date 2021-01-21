# -*- coding: utf-8 -*-
"""
Created on Fri Sep 11 09:39:37 2020

To compare 20CR and ERA-20C only

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

#load file
os.chdir("G:\\data\\allReconstructions\\validation\\commonPeriodValidation")
dat = pd.read_csv('twcr_era20cRMSEComparison.csv')
dat.drop('Unnamed: 0', axis = 1, inplace = True)

#plot
#increase plot font size
sns.set_context('notebook', font_scale = 1.5)

plt.figure(figsize=(20, 10))
m=Basemap(projection='cyl', lat_ts=20, llcrnrlon=-180, 
          urcrnrlon=180,llcrnrlat=-90,urcrnrlat=90, resolution='c')
x,y = m(dat['lon'].tolist(), dat['lat'].tolist())
m.drawcoastlines()

#get degree signs 
parallels = np.arange(-80,81,20.)
meridians = np.arange(-180.,180.,40.)
#labels = [left,right,top,bottom]
m.drawparallels(parallels,labels=[True,True,False,False], linewidth = 0.5)
m.drawmeridians(meridians,labels=[False,False,False,True], linewidth = 0.5)

m.bluemarble(alpha = 0.8)

#define markers -use same for all for now
markers = {"20CR": "o", "ERA-20c": "o", "ERA-Interim":'o', "MERRA":'o', "ERA-FIVE":'o'}
#define palette
color_dict = dict({'20CR':'green',
              'ERA-20c':'magenta',
              'ERA-Interim': 'black',
              'MERRA': 'red',
              'ERA-FIVE':'aqua'
              })
#define bubble sizes
#use 600 for rmse - X for percentIncrease
minSize = min(dat['percIncrease'])*4
if minSize < 0:
    minSize = 0
maxSize = max(dat['percIncrease'])*4



sns.scatterplot(x = x, y = y, markers = markers, style = 'bestLongTerm',\
                size = 'bestLTMagnitude', sizes=(minSize, maxSize),\
                    hue = 'bestLongTerm',  palette = color_dict, data = dat)
plt.legend(loc = 'lower left')
plt.title('RMSE(m) - Common Perdiod (1980-2010) Validation for 20CR and ERA-20C')



#add histogram of metrics
plt.figure()
plt.style.use('classic')
plt.hist(dat['bestLTvsbest'], bins=50)