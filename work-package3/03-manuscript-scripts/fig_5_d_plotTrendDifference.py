"""
Created on Fri Aug 20 08:00:00 2021
Modified on Wed Feb 02 08:35:00 2022

this program plots significant differences between 
trends in observations and reconstructions

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
os.environ["PROJ_LIB"] = "C:\\Users\\WahlInstall\\"\
    "Anaconda3\\Library\\share\\basemap"
from mpl_toolkits.basemap import Basemap
from mpl_toolkits.axes_grid.inset_locator import inset_axes


dirOut = "G:\\report\\year-3\\07-Fall-2020\\#3Paper\\"\
    "p28ThirdManuscript\\manuscript\\figures\\tredDiffSignf"

os.chdir("G:\\report\\year-3\\07-Fall-2020\\#3Paper\\data\\"\
    "trend-analysis\\data\\allThreeTrends\\95TrendDiffSign_post1930")


# trend files
t95 = "G:\\report\\year-3\\07-Fall-2020\\#3Paper\\data\\"\
                "trend-analysis\\data\\allThreeTrends\\95TrendDiffSign_post1930\\"\
                        "95thPercObsTwcrEra20cTrendDiffSign_30yr_75perc_post1930.csv"
t99 = "G:\\report\\year-3\\07-Fall-2020\\#3Paper\\data\\trend-analysis\\"\
                "data\\allThreeTrends\\99TrendDiffSign_post1930\\"\
                        "99thPercObsTwcrEra20cTrendDiffSign_30yr_75perc_post1930.csv"


#############################
# parameters
file = t99
region = ["usw", "use",  "europe", "japan", "australia"]
#############################



# defining regions
geoRef = {
    "usw" : [-155, -120, 35, 62],
    "use" : [-96, -69, 25, 45],
    "japan" : [129, 147, 31, 46],
    "australia" : [113, 155, -44, -10],
    "europe" : [-11, 16, 34, 67]
}

# read trend file
dat = pd.read_csv(file)

dat['dummy'] = 1
dat['sigTwcr'] = dat[dat['obsTwcrPval'] <= 0.05]['dummy']
dat['sigEra20c'] = dat[dat['obsEra20cPval'] <= 0.05]['dummy']


print(dat)


#######
# plot 
#######

sns.set_context('paper', font_scale = 1.5)

fig, axes = plt.subplots(1, len(region), figsize=(18, 18),
        gridspec_kw={'width_ratios': [1,1,1,1,1]})
fig.tight_layout(pad = 0.01)


# plotting panel counter
i = 0

for reg in region:

    print(reg)

    print(region)

     # adjust latitudes for plotting small
    m=Basemap(projection='cyl', lat_ts=20, 
                llcrnrlon= geoRef[reg][0], urcrnrlon=geoRef[reg][1],
                    llcrnrlat=geoRef[reg][2],urcrnrlat=geoRef[reg][3], \
                    resolution='i', ax = axes[i])

    x,y = m(dat['lon'].tolist(), dat['lat'].tolist())
    m.drawcoastlines(color='gray', linewidth=0.5)

    cmap1 = plt.get_cmap("autumn")
    
    sns.scatterplot(x = x, y = y, s = 300, c = cmap1(dat["sigTwcr"]), \
        palette = "autumn",data = dat, edgecolor='black', \
                linewidth=1.0, label = "G-20CR", ax = axes[i])

    cmap2 = plt.get_cmap("autumn_r")
    sns.scatterplot(x = x, y = y, s = 150, c = cmap2(dat["sigEra20c"]), \
            palette = "autumn_r",data = dat, edgecolor='black', linewidth=1.0, 
                marker = "v", label = "G-E20C", ax = axes[i])

    i += 1

# # plt.title("Obs vs 20-CR/ERA-20C - significance in differences in trends - 99th percentile")

# plt.legend()

os.chdir(dirOut)
plt.savefig("{}thPercObsTwcrEra20cTrendDiffSignif_post1930.svg".format(file), dpi = 400)


# plt.show()