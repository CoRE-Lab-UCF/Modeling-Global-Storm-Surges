"""
Created on Thu Jan 19 07:28:00 2022
Modified on Fri Jan 21 12:09:00 2022

this program plots global trends for all seven datasets
for selected regions as subplots

@author: Michael Getachew Tadesse

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
            "trend-analysis\\data\\allSevenTrends\\trends"
dirOut = "G:\\report\\year-3\\07-Fall-2020\\#3Paper\\p28ThirdManuscript\\"\
            "manuscript\\figures\\seven_trends"


#############################
# parameters
region = ["europe", "use", "usw", "australia"]
recon = ["tobs", "t20cr", "te20c", "teint", "tmer", "te5", 'tens']
pval = {"tobs":"pobs", "t20cr":"p20cr", "te20c":"pe20c", 
                "teint":"peint", "tmer":"pmer", "te5":"pe5", "tens":"pens"}
ci = 95
#############################

# # original use 
# "use" : [-96, -69, 25, 45]

geoRef = {
    "usw" : [-155, -120, 35, 62],
    "use" : [-88, -69, 25, 45],
    "japan" : [129, 147, 31, 46],
    "australia" : [113, 155, -44, -10],
    "europe" : [-12, 17, 34, 67]
}



os.chdir(dirHome)
fileName = "allSevenTrends_99th"

# read trend file
dat = pd.read_csv(fileName + ".csv")

#######
# plot 
#######

sns.set_context('paper', font_scale = 1.5)

fig, axes = plt.subplots(4, len(recon), figsize = (20,20),
        gridspec_kw={'width_ratios': [1,1,1,1,1,1,1]})
fig.tight_layout(pad = 0.01)

# plotting panel counter
i = 0
j = 0

for reg in region:
    for rec in recon:

        print(i,j, rec, reg)

        # find significant trends
        dat_rec = dat[['tg', 'lon', 'lat', rec, pval[rec]]]
        dat_rec['signf'] = dat_rec[pval[rec]] <= 0.05
        
        dat_signf = dat_rec[dat_rec["signf"]]
        dat_insignf = dat_rec[~dat_rec["signf"]]

        # plot 
        sns.set_context('paper', font_scale = 1.5)

        # adjust latitudes for plotting small

        m=Basemap(projection='cyl', lat_ts=20, 
                    llcrnrlon= geoRef[reg][0], urcrnrlon=geoRef[reg][1],
                        llcrnrlat=geoRef[reg][2],urcrnrlat=geoRef[reg][3], \
                        resolution='i', ax = axes[i,j])

        x,y = m(dat_signf['lon'].tolist(), dat_signf['lat'].tolist())
        m.drawcoastlines(color='gray', linewidth=0.5)

        
        # #draw parallels and meridians 
        # parallels = np.arange(-80,81,20.)
        # m.drawparallels(parallels,labels=[True,False,False,False], \
        #                 linewidth = 0)
        # m.drawmeridians(np.arange(0.,420.,30.),labels=[0,0,0,1], linewidth = 0) # draw meridians


        cmap = plt.get_cmap("seismic")

        # fix colorbar limits
        norm = matplotlib.colors.Normalize(vmin=-6, vmax=6)


        # plot significant trends
        # change x and y with new lon and lat 
        sns.scatterplot(x = x, y = y, s = 50, c = cmap(norm(dat_signf[rec])), \
            palette = "seismic", marker = "s", norm = norm, data = dat_signf, edgecolor='k', 
                linewidth=0.4, ax = axes[i,j])

        x,y = m(dat_insignf['lon'].tolist(), dat_insignf['lat'].tolist())

        # plot insignificant trends
        sns.scatterplot(x = x, y = y, s = 100, c = cmap(norm(dat_insignf[rec])), \
        palette = "seismic", norm = norm, data = dat_insignf, edgecolor='k', linewidth=0.4, ax = axes[i,j])


        ############################################################################
        # colorbar stuff
        sm = plt.cm.ScalarMappable(cmap = "seismic", norm = norm)
        sm.set_array([])
        # cbaxes = inset_axes(ax, width="1.5%", height = "60%", loc = 'lower center')
        cbaxes = inset_axes(axes[i,j], width="40%", height = "3%", loc = 'lower center')
        cbar = axes[i,j].figure.colorbar(sm, cax = cbaxes, orientation = 'horizontal')
        ############################################################################

        axes[i,j].set_title(rec)
        # axes[i,j].set_title("1980-2010 - {} - {} 99th percentile surges - Significance level = {}%"
        #     .format(reg, rec, ci))
        
        # adjust panel counters
        if j == 6:
            j = 0
            i += 1
        else:
            j += 1


# save/show plots
os.chdir(dirOut)
# plt.savefig("allSevenTrends_4regions.svg", dpi = 400)

plt.show()
