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
dirHome = "G:\\report\\year-3\\07-Fall-2020\\#3Paper"\
    "\\data\\changePointTimeSeries\\reconValidation"

os.chdir(dirHome)

dat = pd.read_csv("twcrCorr0p7plus.csv")

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
sns.scatterplot(x = x, y = y, s = 70, color = 'red',  
        data = dat, edgecolors='gray', linewidth=0.4)

# plt.title("{} - tide gauges with {} or more years of data - total = {} tgs".format(reanalysis, yrLength, len(dat)))

# plt.legend(loc = 3)

plt.show()