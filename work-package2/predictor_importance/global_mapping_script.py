# -*- coding: utf-8 -*-
"""
Created on Tue Apr 14 09:49:38 2020


Global Mapping (correlation/RMSE) script

@author: Michael Tadesse
"""

import os
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
#locate the file that basemap needs
os.environ["PROJ_LIB"] = "C:\\Users\\WahlInstall\\Anaconda3\\Library\\share\\basemap";
from mpl_toolkits.basemap import Basemap


#load file to be plotted
dat = pd.read_csv('eraint_lrreg_validation_pca.csv')
dat_new = dat.drop(dat.loc[dat['tg'] == 'roscoff-france-refmar.csv'].index)
dat_new.reset_index(inplace = True)
dat_new.drop(['index'], axis =1, inplace = True)
dat_new.drop(['Unnamed: 0'], axis =1, inplace = True)


sns.set_context('notebook', font_scale = 2)

#plotting rmse
fig=plt.figure(figsize=(16, 12) )
m=Basemap(projection='mill', lat_ts=10, llcrnrlon=-180, \
  urcrnrlon=180,llcrnrlat=-80,urcrnrlat=80, \
  resolution='c')
x,y = m(dat_new['lon'].tolist(), dat_new['lat'].tolist())
m.drawcoastlines()
plt.scatter(x, y, 70, marker = 'o', edgecolors = 'black', c = dat_new['rmse'], cmap = 'hot_r')
cbar = m.colorbar(location = 'bottom')
plt.clim(0, 0.3)
plt.title('Base_case - RMSE(m)')

#save figure
plt.savefig("base_case_corr.png", dpi = 400)


#plotting correlation
fig=plt.figure(figsize=(16, 12) )
m=Basemap(projection='mill', lat_ts=10, llcrnrlon=-180, \
  urcrnrlon=180,llcrnrlat=-80,urcrnrlat=80, \
  resolution='c')
x,y = m(dat_new['lon'].tolist(), dat_new['lat'].tolist())
m.drawcoastlines()
plt.scatter(x, y, 70, marker = 'o', edgecolors = 'black',\
            c = dat_new['corr_data'], cmap = 'hot_r')
cbar = m.colorbar(location = 'bottom')
plt.clim(0, 1)
plt.title('Base_case  - Correlation')



#extract correlation data from dat_new
get_corr = lambda x: float(x.split('(')[1].split(',')[0])
corr_data = pd.DataFrame(list(map(get_corr, dat_new['corrn'])), columns = ['corrn'])
dat_new['corr_data'] = corr_data