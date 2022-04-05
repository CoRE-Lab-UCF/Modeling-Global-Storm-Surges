"""
Created on Mon Jul 01 08:00:00 2021

this program plots global trends

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
        "trend-analysis\\data\\06-era5"
        }

##############
# parameters
recon = "twcr"
year = 1875
perc = 99
ci = 95
mk = "modifiedMK"
##############


os.chdir(reconDir[recon] + "\\003-{}Trends\\{}".format(year,perc))

fileName = "{}_{}_{}thPercTrends_reg_{}CI_{}_HAC".format(recon,year,perc, ci, mk)


# select the trends column
dat = pd.read_csv(fileName + ".csv")

dat['trends_reg'] = dat[dat['regSig']]['trend_mm_year_reg'] # filter only significant trends
# dat['trends_reg'] = dat['trend_mm_year_reg'] # use all trends for plotting

## Mann-Kendall Trends
# dat['trends_mk'] = dat[dat['mkSig']]['trend_mm_year_mk'] 
# dat['trends_mk'] = dat['trend_mm_year_mk']

print(dat)
# print(dat[~dat['trends'].isnull()])


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

m.bluemarble(alpha = 0.85)

#add colorbar - assign min/max manually
# norm = plt.Normalize(-5, 5)
# normalize = matplotlib.colors.Normalize(vmin=-5, vmax=5)
# sm = plt.cm.ScalarMappable(cmap = "seismic", norm = norm)
# sm.set_array([])

cmap = plt.get_cmap("seismic")

# fix colorbar limits
norm = matplotlib.colors.Normalize(vmin=-6, vmax=6)


ax = sns.scatterplot(x = x, y = y, s = 100, c = cmap(norm(dat['trends_reg'])), \
    palette = "seismic", norm = norm, data = dat, edgecolor='gray', linewidth=0.4)

sm = plt.cm.ScalarMappable(cmap = "seismic", norm = norm)
sm.set_array([])
cbaxes = inset_axes(ax, width="40%", height = "3%", loc = 'lower center')
cbar = ax.figure.colorbar(sm, cax = cbaxes, orientation = 'horizontal')

plt.savefig(fileName + ".svg", dpi = 400)

# # ax.get_legend().remove()
# cbaxes = inset_axes(ax, width="80%", height = "3%", loc = 3)
# ax.figure.colorbar(sm, cax = cbaxes, orientation = 'horizontal')

# ax.set_title(fileName)
ax.set_title("{} {}-2015 - {}th percentile surges - Trends".format(recon,year, perc))

# plt.legend(loc = 3)

plt.show()