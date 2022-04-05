"""
Created on Fri Dec 10 13:38:00 2021

testing 1900-1950 trends 

@author: Michael Tadesse

"""

import os
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib
import matplotlib.pyplot as plt
#locate the file that basemap needs
os.environ["PROJ_LIB"] = "C:\\Users\\WahlInstall\\"\
    "Anaconda3\\Library\\share\\basemap"
from mpl_toolkits.basemap import Basemap
from mpl_toolkits.axes_grid.inset_locator import inset_axes


# get data 
dirHome = "G:\\report\\year-3\\07-Fall-2020\\#3Paper\\data\\"\
        "trend-analysis\\data\\03-obsSurge\\trends\\99"
# \\003-1875Trends\\99
reconDir = {
        "twcr" : "G:\\report\\year-3\\07-Fall-2020\\#3Paper\\data\\"\
        "trend-analysis\\data\\01-twcr",
        "era20c" : "G:\\report\\year-3\\07-Fall-2020\\#3Paper\\data\\"\
        "trend-analysis\\data\\02-era20c",
        "era5" : "G:\\report\\year-3\\07-Fall-2020\\#3Paper\\data\\"\
        "trend-analysis\\data\\06-era5",
        "obs" : "G:\\report\\year-3\\07-Fall-2020\\#3Paper\\data\\"\
                "trend-analysis\\data\\03-obsSurge"
        }

#############################
# parameters
recon = "obs"
year = 1950
perc = 99
ci = 95
mk = "modifiedMK"
onlySignificantTrends = True
#############################


os.chdir(reconDir[recon] + "\\003-{}Trends\\{}".format(year,perc))

fileName = "{}_{}_{}thPercTrends_reg_{}CI_{}_HAC".format(recon,year,perc, ci, mk)


# select the trends column
dat = pd.read_csv(fileName + ".csv")


# filter only significant trends
dat['trends_reg'] = dat[dat['regSig']]['trend_mm_year_reg'] 


# plot 
sns.set_context('paper', font_scale = 1.5)

plt.figure(figsize=(20, 10))

# adjust latitudes for plotting small

m=Basemap(projection='cyl', lat_ts=20, llcrnrlon=-180, 
            urcrnrlon=180,llcrnrlat=-58,urcrnrlat=85, \
                resolution='c')
x,y = m(dat['lon'].tolist(), dat['lat'].tolist())
m.drawcoastlines(color='k', linewidth=0.5)

#draw parallels and meridians 
parallels = np.arange(-80,81,20.)
m.drawparallels(parallels,labels=[True,False,False,False], \
                linewidth = 0)
m.drawmeridians(np.arange(0.,420.,30.),labels=[0,0,0,1], linewidth = 0) # draw meridians

# m.bluemarble(alpha = 0.85)

cmap = plt.get_cmap("seismic")

# fix colorbar limits
norm = matplotlib.colors.Normalize(vmin=-6, vmax=6)


# plot significant trends only
if onlySignificantTrends:
    ax = sns.scatterplot(x = x, y = y, s = 100, c = cmap(norm(dat['trends_reg'])), \
        palette = "seismic", norm = norm, data = dat, edgecolor='gray', linewidth=0.4)
else:
    ax = sns.scatterplot(x = x, y = y, s = 100, c = cmap(norm(dat['trend_mm_year_reg'])), \
    palette = "seismic", norm = norm, data = dat, edgecolor='gray', linewidth=0.4)




############################################################################
# colorbar stuff
sm = plt.cm.ScalarMappable(cmap = "seismic", norm = norm)
sm.set_array([])
# cbaxes = inset_axes(ax, width="1.5%", height = "60%", loc = 'lower center')
cbaxes = inset_axes(ax, width="40%", height = "3%", loc = 'lower center')
cbar = ax.figure.colorbar(sm, cax = cbaxes, orientation = 'horizontal')
############################################################################


# plt.savefig(fileName + ".svg", dpi = 400)

# ax.set_title(fileName)
ax.set_title("{} {}-2015 - {}th percentile surges - Only Significant Trends = {}"
    .format(recon,year, perc, onlySignificantTrends))

# plt.legend(loc = 3)

plt.show()