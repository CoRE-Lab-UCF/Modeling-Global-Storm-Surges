"""  
Created on Fri Aug 30 08:00:00 2021

this script plots the tide gauges with significant trend
differences between obs twcr era20c

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


def countTgsYears():
    """ count number of tgs with starting years """

    os.chdir("G:\\report\\year-3\\07-Fall-2020\\#3Paper\\data\\trend-analysis\\data\\01-twcr\\02-percentiles\\95")

    tgList = os.listdir()

    c1950 = 0
    c1900 = 0
    c1875 = 0
    for tg in tgList:
        print(tg)

        dat = pd.read_csv(tg)
        value = dat['year'][0]

        if value <= 1875:
            c1875 = c1875 + 1
        elif value <= 1900:
            c1900 = c1900 + 1
        elif value <= 1950:
            c1950 = c1950 + 1

    print("c1875 = {}".format(c1875))
    print("c1900 = {}".format(c1900))
    print("c1950 = {}".format(c1950))

os.chdir("G:\\report\\year-3\\07-Fall-2020\\#3Paper\\data\\"\
    "trend-analysis\\data\\allThreeTrends\\95TrendDiffSignificance")

dat = pd.read_csv("95thPercObsTwcrEra20cTrendDiffSignif.csv")


dat['dummy'] = 1
dat['sigTwcr'] = dat[dat['obsTwcrPval'] <= 0.05]['dummy']
dat['sigEra20c'] = dat[dat['obsEra20cPval'] <= 0.05]['dummy']


print(dat)


# plot 
sns.set_context('paper', font_scale = 1.5)

plt.figure(figsize=(20, 10))
m=Basemap(projection='cyl', lat_ts=20, llcrnrlon=-180, 
            urcrnrlon=180,llcrnrlat=-90,urcrnrlat=90, \
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
sns.scatterplot(x = x, y = y, s = 100, c = cmap1(dat["sigTwcr"]), \
    palette = "autumn",data = dat, edgecolors='white', linewidth=0.4, label = "20-CR")

cmap2 = plt.get_cmap("autumn_r")
sns.scatterplot(x = x, y = y, s = 70, c = cmap2(dat["sigEra20c"]), \
    palette = "autumn_r",data = dat, edgecolors='white', linewidth=0.4, marker = "v", label = "ERA-20C")

# plt.savefig(fileName + ".svg", dpi = 400)

plt.title("Obs vs 20-CR/ERA-20C - significance in differences in trends - 95th percentile")

plt.legend()

plt.show()