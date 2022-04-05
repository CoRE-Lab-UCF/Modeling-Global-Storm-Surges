"""
Created on Fri Sep 01 11:24:00 2021

this program plots overlapping tgs with significant trends
when using linear regression and mann-kendal

@author: Michael Getachew Tadesse

"""

import os
import numpy as np
import pandas as pd
from scipy.ndimage.measurements import label
import seaborn as sns
import matplotlib
import matplotlib.pyplot as plt
#locate the file that basemap needs
# os.environ["PROJ_LIB"] = "C:\\Users\\WahlInstall\\"\
#     "Anaconda3\\Library\\share\\basemap"
from mpl_toolkits.basemap import Basemap
from mpl_toolkits.axes_grid.inset_locator import inset_axes

##################################################################################

####################
# parameters
recon = "02-era20c"
threshold = 99
year = 1900
ci = 90
mk = "modifiedMK"

####################


os.chdir("G:\\report\\year-3\\07-Fall-2020\\#3Paper\\data\\"\
    "trend-analysis\\data\\{}\\003-{}Trends\\{}".format(recon, year, threshold))

dat = pd.read_csv("{}_{}_{}thPercTrends_reg_{}CI_{}_HAC.csv".format(recon.split('-')[1],year, threshold, ci, mk))

dat['dummy'] = 1
dat['sigReg'] =  dat[(dat['regSig'] == True) & (dat['mkSig'] == False)]['dummy']
dat['sigMK'] = dat[(dat['regSig'] == False) & (dat['mkSig'] == True)]['dummy']
dat['sigBoth'] = dat[(dat['regSig'] == True) & (dat['mkSig'] == True)]['dummy']
##################################################################################

print(dat)

# plot 
sns.set_context('paper', font_scale = 1.5)

plt.figure(figsize=(20, 10))
m=Basemap(projection='cyl', lat_ts=20, llcrnrlon=-180, 
            urcrnrlon=180,llcrnrlat=-90,urcrnrlat=90, \
                resolution='c')
x,y = m(dat['lon'].tolist(), dat['lat'].tolist())
m.drawcoastlines(linewidth = 0.5)

#draw parallels and meridians 
parallels = np.arange(-80,81,20.)
m.drawparallels(parallels,labels=[True,False,False,False], \
                linewidth = 0)
m.drawmeridians(np.arange(0.,420.,30.),labels=[0,0,0,1], linewidth = 0) # draw meridians

m.bluemarble(alpha = 0.0)

cmap1 = plt.get_cmap("rainbow")
sns.scatterplot(x = x, y = y, s = 200, c = cmap1(dat["sigReg"]), \
    palette = "rainbow",data = dat, edgecolors='white', linewidth=0.0, label = "LR")

cmap2 = plt.get_cmap("winter_r")
sns.scatterplot(x = x, y = y, s = 200, c = cmap2(dat["sigMK"]), \
    palette = "winter_r",data = dat, edgecolors='white', linewidth=0.0, label = "MK")

cmap3 = plt.get_cmap("PiYG")
sns.scatterplot(x = x, y = y, s = 200, c = cmap3(dat["sigBoth"]), \
    palette = "PiYG",data = dat, edgecolors='white', linewidth=0.0,  label = "Both")



plt.title("{} - {}th Percentile Surges ({}-2015) - {}% Significance - Linear Regression (LR) vs {}".\
        format(recon, threshold, year, ci,  mk))

plt.legend()


# plt.savefig("LR_MK_99thPercReconSignif.svg", dpi = 400)


plt.show()

