"""  
this script plots the spatial view of twcr/era20c 
with their length of record after cpt 
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
dirHome = "G:\\report\\year-3\\07-Fall-2020\\#3Paper\\data\\"\
    "changePointTimeSeries\\mamun-cpt-approach\\era20c\\0001-predCPT\\cptSA"
dirOut = "G:\\report\\year-3\\07-Fall-2020\\#3Paper\\p28ThirdManuscript\\manuscript\\figures"

os.chdir(dirHome)

dat = pd.read_csv("era20cVisual_Inspection_GSSRDB_georef.csv")

dat['recordLength'] = 'nan'
dat['recordSign'] = 'nan' 


for ii in range(len(dat)):
    print(dat['tg'][ii])

    # check if tg is dicarded
    if dat['visual_inspection'][ii] == 'discard':
        continue

    # change 2015 to 2010 for era20c
    dat['recordLength'][ii] = 2010 - int(dat['visual_inspection'][ii])

    if dat['recordLength'][ii] <= 50:
        dat['recordSign'][ii] = "0-50"
    elif (dat['recordLength'][ii] > 50) & (dat['recordLength'][ii] <= 75):
        dat['recordSign'][ii] = "50-75"
    elif (dat['recordLength'][ii] > 75) & (dat['recordLength'][ii] <= 100):
        dat['recordSign'][ii] = "75-100"
    elif (dat['recordLength'][ii] > 100) & (dat['recordLength'][ii] <= 125):
        dat['recordSign'][ii] = "100-125"
    elif (dat['recordLength'][ii] > 125) & (dat['recordLength'][ii] <= 150):
        dat['recordSign'][ii] = "125-150"
    elif (dat['recordLength'][ii] > 150) & (dat['recordLength'][ii] <= 180):
        dat['recordSign'][ii] = "150-180"

    # dat['era20cLength'][ii] = 2010 - dat['viEra20c'][ii]

print(dat)
dat.to_csv("era20cSurgeLength.csv")

dat['recordSign'].replace('nan', 'Discarded', inplace = True)

datDiscarded = dat[dat['recordSign'] == "Discarded"]
dat = dat[dat['recordSign'] != "Discarded"]
dat.sort_values("recordLength", ascending=False, inplace = True)

# plot 
sns.set_context('notebook', font_scale = 1.5)

plt.figure(figsize=(20, 10))
m=Basemap(projection='cyl', lat_ts=20, llcrnrlon=-180, 
            urcrnrlon=180,llcrnrlat=-83,urcrnrlat=85, \
                resolution='c')
x,y = m(dat['lon'].tolist(), dat['lat'].tolist())
m.drawcoastlines()

#draw parallels and meridians 
parallels = np.arange(-80,81,20.)
m.drawparallels(parallels,labels=[True,False,False,False], \
                linewidth = 0)
m.drawmeridians(np.arange(0.,420.,30.),labels=[0,0,0,1], linewidth = 0) # draw meridians

# m.bluemarble(alpha = 0.85)

sns.scatterplot(x = x, y = y, s = 70, color = 'red', hue = 'recordSign',  
        data = dat, edgecolor='black', linewidth=0.4, 
        palette = {"0-50":'black', 
                   "50-75":'cyan', 
                   "75-100":'yellow', 
                   "100-125":'lime', 
                   "125-150":'magenta',
                   "150-180":'darkorange'})

# plotting the discarded tide gauges
x,y = m(datDiscarded['lon'].tolist(), datDiscarded['lat'].tolist())
sns.scatterplot(x = x, y = y, s = 100, color = 'red', hue = 'recordSign',  
        data = datDiscarded, palette = {"Discarded":'red'}, edgecolor='black', 
            linewidth=0.4, marker = '^')

# plt.title("Length of ERA-20C Surge Reconstruction (Years) After Changepoint Analysis")

plt.legend()

os.chdir(dirOut)
plt.savefig("er20cSurgeLength.svg", dpi = 400)

# plt.show()
