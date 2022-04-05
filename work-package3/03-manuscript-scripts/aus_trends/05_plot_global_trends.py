"""
Created on Thu Dec 30 09:07:00 2021

this program plots global trends for all six datasets

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
dirHome = "G:\\report\\year-3\\07-Fall-2020\\#3Paper\\data"\
            "\\trend-analysis\\data\\allSixTrends\\rawData\\"\
                    "australia_tgs\\trends"
dirOut = "G:\\report\\year-3\\07-Fall-2020\\#3Paper\\p28ThirdManuscript\\"\
            "manuscript\\figures\\six_trends\\high_res"


#############################
# parameters
region = ["australia"]
recon = ["tobs", "t20cr", "te20c", "teint", "tmer", "te5"]
pval = {"tobs":"pobs", "t20cr":"p20cr", "te20c":"pe20c", 
                "teint":"peint", "tmer":"pmer", "te5":"pe5"}
ci = 95
mk = "modifiedMK"
#############################

geoRef = {
    "usw" : [-155, -120, 35, 62],
    "use" : [-96, -69, 25, 45],
    "japan" : [129, 147, 31, 46],
    "australia" : [113, 155, -44, -10],
    "europe" : [-11, 16, 34, 67]
}



os.chdir(dirHome)
fileName = "aus_SixTrends_99th"


# select the trends column
dat = pd.read_csv(fileName + ".csv")


for rec in recon:
    for reg in region:

        # find significant trends
        dat_rec = dat[['tg', 'lon', 'lat', rec, pval[rec]]]
        dat_rec['signf'] = dat_rec[pval[rec]] <= 0.05
        
        dat_signf = dat_rec[dat_rec["signf"]]
        dat_insignf = dat_rec[~dat_rec["signf"]]

        
        # plot 
        sns.set_context('paper', font_scale = 1.5)

        plt.figure(figsize=(20, 10))

        # adjust latitudes for plotting small

        m=Basemap(projection='cyl', lat_ts=20, 
                    llcrnrlon= geoRef[reg][0], urcrnrlon=geoRef[reg][1],
                        llcrnrlat=geoRef[reg][2],urcrnrlat=geoRef[reg][3], \
                        resolution='i')

        x,y = m(dat_signf['lon'].tolist(), dat_signf['lat'].tolist())
        m.drawcoastlines(color='gray', linewidth=0.5)

        #draw parallels and meridians 
        parallels = np.arange(-80,81,20.)
        m.drawparallels(parallels,labels=[True,False,False,False], \
                        linewidth = 0)
        m.drawmeridians(np.arange(0.,420.,30.),labels=[0,0,0,1], linewidth = 0) # draw meridians

        # m.bluemarble(alpha = 0.85)

        cmap = plt.get_cmap("seismic")

        # fix colorbar limits
        norm = matplotlib.colors.Normalize(vmin=-7, vmax=7)


        # plot significant trends
        # change x and y with new lon and lat 
        ax = sns.scatterplot(x = x, y = y, s = 100, c = cmap(norm(dat_signf[rec])), \
            palette = "seismic", marker = "s", norm = norm, data = dat_signf, edgecolor='k', 
                linewidth=0.4)

        x,y = m(dat_insignf['lon'].tolist(), dat_insignf['lat'].tolist())

        # plot insignificant trends
        ax = sns.scatterplot(x = x, y = y, s = 200, c = cmap(norm(dat_insignf[rec])), \
        palette = "seismic", norm = norm, data = dat_insignf, edgecolor='k', linewidth=0.4)




        ############################################################################
        # colorbar stuff
        sm = plt.cm.ScalarMappable(cmap = "seismic", norm = norm)
        sm.set_array([])
        # cbaxes = inset_axes(ax, width="1.5%", height = "60%", loc = 'lower center')
        cbaxes = inset_axes(ax, width="40%", height = "3%", loc = 'lower center')
        cbar = ax.figure.colorbar(sm, cax = cbaxes, orientation = 'horizontal')
        ############################################################################



        # ax.set_title(fileName)
        ax.set_title("1980-2010 - {} - {} 99th percentile surges - Significance level = {}%"
            .format(reg, rec, ci))

        # plt.legend(loc = 3)

        os.chdir(dirOut)
        # plt.savefig(reg+"_"+rec + ".jpeg", dpi = 400)

        plt.show()