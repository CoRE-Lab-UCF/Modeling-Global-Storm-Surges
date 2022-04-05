# -*- coding: utf-8 -*-
"""
Created on Mon Feb  1 09:53:04 2021

global recent changepoint year plotter - era20c

caveat: use the era20cRecentCPTv2.csv file in order 
to compare plots with era20c - it has dummy tide gauges
with recentCPT in 1836 and 2015 to maket the plot start 
from 1836

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


#get file
home = "G:\\report\\07-Fall-2020\\#3Paper\\data\\changePointTimeSeries"\
                                            "\\era20cBcpProb"
os.chdir(home)

################################################
#use era20cRecentCPTv2 file that has test tgs
#in order to compare directly with 20CR
dat = pd.read_csv('era20c1960to2010.csv')
dat.drop('Unnamed: 0', axis = 1, inplace = True)
################################################


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

m.bluemarble(alpha = .82) 

#define markers 
markers = {"p25": "D", "p50": "s", "p75":'^', "p<0.25": "o"}
# markers = {"p50": "s", "p75":'^', "p<0.5": "o"}


ax = sns.scatterplot(x = x, y = y, markers = markers, style = 'pCat',\
                s = 70, hue= 'recentCpt', palette = 'hot_r',  data = dat)
# m.colorbar(location = 'bottom')

#add colorbar for years
norm = plt.Normalize(dat['recentCpt'].min(), dat['recentCpt'].max())
sm = plt.cm.ScalarMappable(cmap = "hot_r", norm = norm)
sm.set_array([])

ax.get_legend().remove()
cbaxes = inset_axes(ax, width="80%", height = "3%", loc = 3)
ax.figure.colorbar(sm, cax = cbaxes, orientation = 'horizontal')


ax.legend(loc = 'lower left', ncol = 3)
# plt.title(title)


# # save as svg
# saveName = 'era20cGlobalNop25.svg'
# plt.savefig(saveName, dpi = 400)
