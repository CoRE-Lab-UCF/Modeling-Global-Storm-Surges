"""
Created on Fri Aug 20 08:00:00 2021

this program plots significant differences between 
trends in observations and reconstructions

@author: Michael Tadesse

"""

import os
import numpy as np
import pandas as pd
from scipy.ndimage.measurements import label
import seaborn as sns
import matplotlib
import matplotlib.pyplot as plt
#locate the file that basemap needs
os.environ["PROJ_LIB"] = "C:\\Users\\WahlInstall\\"\
    "Anaconda3\\Library\\share\\basemap"
from mpl_toolkits.basemap import Basemap
from mpl_toolkits.axes_grid.inset_locator import inset_axes



os.chdir("G:\\report\\year-3\\07-Fall-2020\\#3Paper\\data\\"\
    "trend-analysis\\data\\allThreeTrends\\95TrendDiffSignificance")

dat = pd.read_csv("95thPercObsTwcrEra20cTrendDiffSignif_30yr_75perc.csv")


dat['dummy'] = 1
dat['sigTwcr'] = dat[dat['obsTwcrPval'] <= 0.05]['dummy']
dat['sigEra20c'] = dat[dat['obsEra20cPval'] <= 0.05]['dummy']


print(dat)

geoRef = {
    "usw" : [-155, -120, 35, 62],
    "use" : [-96, -69, 25, 45],
    "japan" : [129, 147, 31, 46],
    "australia" : [113, 155, -44, -10],
    "europe" : [-11, 16, 34, 67]
}

###############################
# change region here
region = "usw"
###############################


# plot 
sns.set_context('paper', font_scale = 1.5)

plt.figure(figsize=(20, 10))
m=Basemap(projection='cyl', lat_ts=20, 
            llcrnrlon= geoRef[region][0], urcrnrlon=geoRef[region][1],
                llcrnrlat=geoRef[region][2],urcrnrlat=geoRef[region][3], \
                resolution='c')
x,y = m(dat['lon'].tolist(), dat['lat'].tolist())
m.drawcoastlines()

#draw parallels and meridians 
parallels = np.arange(-80,81,20.)
m.drawparallels(parallels,labels=[True,False,False,False], \
                linewidth = 0)
m.drawmeridians(np.arange(0.,420.,30.),labels=[0,0,0,1], linewidth = 0) # draw meridians

m.bluemarble(alpha = 0.85)

cmap1 = plt.get_cmap("autumn")
sns.scatterplot(x = x, y = y, s = 1000, c = cmap1(dat["sigTwcr"]), \
    palette = "autumn",data = dat, edgecolors='white', linewidth=1.2, label = "20-CR")

cmap2 = plt.get_cmap("autumn_r")
sns.scatterplot(x = x, y = y, s = 700, c = cmap2(dat["sigEra20c"]), \
    palette = "autumn_r",data = dat, edgecolors='white', linewidth=1.2, marker = "v", label = "ERA-20C")


plt.title("Obs vs 20-CR/ERA-20C - significance in differences in trends - 99th percentile")

plt.legend()


# plt.savefig("{}_99thPercObsTwcrEra20cTrendDiffSignif.svg".format(region), dpi = 400)


plt.show()