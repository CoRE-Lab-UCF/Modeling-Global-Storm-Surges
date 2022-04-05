"""
Created on Mon Jul 01 08:00:00 2021
Modified on Mon Jan 17 11:28:00 2022

this program plots global trends but divided 
into regions depending on the selected year

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
out = "G:\\report\\year-3\\07-Fall-2020\\#3Paper\\p28ThirdManuscript"\
        "\\manuscript\\figures\\long_term_trends"

#############################
# parameters
recon = "era20c"
year = "1950"
perc = 95
ci = 95
mk = "modifiedMK"
#############################

#########################################################
# defining regions
geoRef = {
    "usw" : [-155, -120, 35, 62],
    "use" : [-96, -69, 25, 45],
    "japan" : [129, 147, 31, 46],
    "australia" : [113, 155, -44, -10],
    "europe" : [-11, 16, 34, 67]
}

if year == "1930":
    region = ["use", "europe", "australia"]
    width_ratio = [1.3,1.3,1.3]
else:
    region = ["use", "usw", "europe", "japan", "australia"]
    width_ratio = [1.3,1.3,1.3,1.3,1.3]

#########################################################


# cd to trend file directory
os.chdir(reconDir[recon] + "\\003-{}Trends\\{}".format(year,perc))

fileName = "{}_{}_{}thPercTrends_reg_{}CI_{}_HAC".format(recon,year,perc, ci, mk)


# get trend file
dat = pd.read_csv(fileName + ".csv")

# get significant/insignificant trends
dat_signf = dat[dat["regSig"]]
dat_insignf = dat[~dat["regSig"]]

#######
# plot 
#######

sns.set_context('paper', font_scale = 1.5)

fig, axes = plt.subplots(1, len(region), figsize=(18, 18),
        gridspec_kw={'width_ratios': width_ratio})
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

    x,y = m(dat_signf['lon'].tolist(), dat_signf['lat'].tolist())
    m.drawcoastlines(color='gray', linewidth=0.5)

    # #draw parallels and meridians 
    # parallels = np.arange(-80,81,20.)
    # m.drawparallels(parallels,labels=[True,False,False,False], \
    #                 linewidth = 0)
    # m.drawmeridians(np.arange(0.,420.,30.),labels=[0,0,0,1], linewidth = 0) # draw meridians

    # m.bluemarble(alpha = 0.85)

    cmap = plt.get_cmap("seismic")

    # fix colorbar limits
    norm = matplotlib.colors.Normalize(vmin=-6, vmax=6)


    # plot significant trends
    # change x and y with new lon and lat 
    sns.scatterplot(x = x, y = y, s = 75, c = cmap(norm(dat_signf['trend_mm_year_reg'])), \
        palette = "seismic", marker = "s", norm = norm, data = dat_signf, edgecolor='k', 
            linewidth=0.6, ax = axes[i])

    x,y = m(dat_insignf['lon'].tolist(), dat_insignf['lat'].tolist())

    # plot insignificant trends
    sns.scatterplot(x = x, y = y, s = 150, c = cmap(norm(dat_insignf['trend_mm_year_reg'])), \
        palette = "seismic", norm = norm, data = dat_insignf, edgecolor='k', linewidth=0.6, ax = axes[i])

    ############################################################################
    # # colorbar stuff
    sm = plt.cm.ScalarMappable(cmap = "seismic", norm = norm)
    sm.set_array([])
    # cbaxes = inset_axes(ax, width="1.5%", height = "60%", loc = 'lower center')
    cbaxes = inset_axes(axes[i], width="40%", height = "3%", loc = 'lower center')
    cbar = axes[i].figure.colorbar(sm, cax = cbaxes, orientation = 'horizontal')
    ############################################################################



    # ax.set_title(fileName)
    start = year
    if recon == "twcr":
        end = "2015"
    else:
        end = "2010"

    # axes[i].set_title("{} {}-{} - {}th percentile surges - {}"
    #     .format(recon, start, end, perc, reg))

    # plt.legend(loc = 3)

    
    i += 1



os.chdir(out)
plt.savefig(fileName + ".svg", dpi = 400)

# plt.show()