# -*- coding: utf-8 -*-
"""
Created on Thu Sep 10 18:05:55 2020

Figure #1 - Sensitivity Analysis Phase 1

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

#load data from "F:\01_erainterim\06_eraint_results\predictor_importance"

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

plt.scatter(x, y, 100, marker = 'o', edgecolors = 'black', c = 
                dat['baseMinusSstRmse'], cmap = 'seismic_r')
m.colorbar(location = 'bottom')

plt.clim(-12.5,12.5)
plt.title('Difference in RMSE (mm) between Base Case and SST Case')

os.chdir('G:\\data\manuscriptFiles\\figures')
saveName = 'figure1b.svg'
plt.savefig(saveName, dpi = 400)
