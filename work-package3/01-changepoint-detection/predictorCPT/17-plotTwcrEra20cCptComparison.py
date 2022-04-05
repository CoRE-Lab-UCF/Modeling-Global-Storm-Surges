"""  
this script plots the spatial view of where twcr/era20c 
have earlier changepoint 
"""

import os
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
#locate the file that basemap needs
os.environ["PROJ_LIB"] = "C:\\Users\\WahlInstall\\"\
    "Anaconda3\\Library\\share\\basemap"
from mpl_toolkits.basemap import Basemap


# get data 
dirHome = "G:\\report\\year-3\\07-Fall-2020\\#3Paper\\data\\changePointTimeSeries"\
    "\\mamun-cpt-approach\\twcr_era20c_1900_2010"

os.chdir(dirHome)


# process data
dat = pd.read_csv("twcrEra20c_cptComparison_geoRef.csv")

# print(len(str(dat[var][0])))

# choose changepoint probability
cpt = 50

var = "p"+str(cpt)+"E"

dat[var] = dat[var].replace(float('nan'), 'equal')
dat[var] = dat[var].replace(True, 'ERA-20C')
dat[var] = dat[var].replace(False, '20-CR')

# plot 
sns.set_context('notebook', font_scale = 1.5)

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
sns.scatterplot(x = x, y = y, s = 70, color = 'red', \
   palette = {'ERA-20C':'magenta','20-CR':'green', 'equal': 'None'},  
        data = dat, hue=var, edgecolors='gray', linewidth=0.4)

plt.title("comparison of 20-CR and ERA-20C changepoints for (1900-2010) - {}% changepoint probability".format(cpt))

plt.legend(loc = 3)

plt.show()
