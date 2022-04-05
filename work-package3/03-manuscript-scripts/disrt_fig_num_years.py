"""

Created on Thu Mar 01 15:53:00 2022

plot available number of years for GESLA-V2

@author: Michael Getachew Tadesse

"""

import os 
import numpy as np
import pandas as pd
from datetime import datetime
import seaborn as sns
import matplotlib.pyplot as plt
#locate the file that basemap needs
os.environ["PROJ_LIB"] = "C:\\Users\\WahlInstall\\"\
    "Anaconda3\\Library\\share\\basemap"
from mpl_toolkits.basemap import Basemap



dirHome = "G:\\report\\year-3\\07-Fall-2020\\#3Paper\\data\\trend-analysis\\data\\03-obsSurge"

os.chdir(dirHome)

dat = pd.read_csv("obsSurgeAvailableDat.csv") 

dat25Plus = dat[dat['50plus']]
datElse = dat[~dat['50plus']]

print(dat25Plus)


# plot 
sns.set_context('paper', font_scale = 1.5)

plt.figure(figsize=(20, 10))
m=Basemap(projection='cyl', lat_ts=20, llcrnrlon=-180, 
            urcrnrlon=180,llcrnrlat=-83,urcrnrlat=85, \
                resolution='l')
x,y = m(dat['lon'].tolist(), dat['lat'].tolist())
m.drawcoastlines(linewidth= 0.5, color = "k")

#draw parallels and meridians 
parallels = np.arange(-80,81,20.)

# plot tgs with <25 years
x,y = m(datElse['lon'].tolist(), datElse['lat'].tolist())
sns.scatterplot(x = x, y = y, s = 50,   
        data = datElse, hue = datElse['50plus'], palette = "YlGn" , edgecolor='k', 
            linewidth=0.4, label = "< 50 Years")


# plot tgs with >= 25 years
x,y = m(dat25Plus['lon'].tolist(), dat25Plus['lat'].tolist())
sns.scatterplot(x = x, y = y, s = 50,   
        data = dat25Plus, hue = dat25Plus['50plus'], palette = "Reds", edgecolor='k', 
            linewidth=0.4, label = ">= 50 Years")



plt.legend(loc = "lower left", ncol = 2)

plt.savefig("obs_surge_availability.svg")

plt.show()

