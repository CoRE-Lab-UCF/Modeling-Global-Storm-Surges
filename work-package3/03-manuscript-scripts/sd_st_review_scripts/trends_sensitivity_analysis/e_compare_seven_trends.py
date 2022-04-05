"""
Created on Sat Jan 22 11:03:00 2022

this program compares the differences in trends
of the six trends against observed surge trends 
with box-plots

built off of descriptor's boxplot fig 5 
p28DataDescriptor/reView/code/r1c26/fig5getLatitudinalMetrics.py

@author: Michael Getachew Tadesse

"""

import os
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib
import matplotlib.pyplot as plt



# get data 
dirHome = "G:\\report\\year-3\\07-Fall-2020\\#3Paper\\data\\"\
            "trend-analysis\\data\\allSevenTrends\\trends"
dirOut = "G:\\report\\year-3\\07-Fall-2020\\#3Paper\\p28ThirdManuscript\\"\
            "manuscript\\figures\\seven_trends"


os.chdir(dirHome)

# read trends data
dat = pd.read_csv("allSevenTrends_99th.csv")
dat = dat[['tg', 'lon', 'lat','tobs', 't20cr', 'te20c', 'teint', 'tmer', 'te5', 'tens']]
dat['region'] = 'nan'

print(dat)

# get trend differences
dat['d20cr'] = dat['tobs'] - dat['t20cr']
dat['de20c'] = dat['tobs'] - dat['te20c']
dat['deint'] = dat['tobs'] - dat['teint']
dat['dmer'] = dat['tobs'] - dat['tmer']
dat['de5'] = dat['tobs'] - dat['te5']
dat['dens'] = dat['tobs'] - dat['tens']

print(dat[['d20cr', 'de20c', 'deint', 'dmer', 'de5', 'dens']])


# categorize tgs according to region
for ii in range(len(dat)):
    if (dat['lon'][ii] >= -155) & (dat['lon'][ii] <= -120) & \
                (dat['lat'][ii] >= 35) & (dat['lat'][ii] <= 62):
        dat['region'][ii] = "USW"
    elif (dat['lon'][ii] >= -96) & (dat['lon'][ii] <= -69) & \
                (dat['lat'][ii] >= 25) & (dat['lat'][ii] <= 45):
        dat['region'][ii] = "USE"
    elif (dat['lon'][ii] >= -11) & (dat['lon'][ii] <= 16) & \
                (dat['lat'][ii] >= 34) & (dat['lat'][ii] <= 67):
        dat['region'][ii] = "Europe"
    elif (dat['lon'][ii] >= 129) & (dat['lon'][ii] <= 147) & \
                (dat['lat'][ii] >= 31) & (dat['lat'][ii] <= 46):
        dat['region'][ii] = "Japan"
    elif (dat['lon'][ii] >= 113) & (dat['lon'][ii] <= 155) & \
                (dat['lat'][ii] >= -44) & (dat['lat'][ii] <= -10):
        dat['region'][ii] = "Australia"

# remove nans
row_nan = dat[dat['region'] == 'nan']
dat.drop(row_nan.index, axis = 0, inplace = True)
dat.reset_index(inplace = True)
dat.drop('index', axis = 1, inplace = True)

#get core data only
df = dat[['d20cr', 'de20c', 'deint', 'dmer', 'de5', 'dens', 'region']]

#melt dataframe
dfMelt = df.melt(id_vars='region')

#color coding
pal = {'d20cr': 'green', 
                          'de20c': 'magenta', 'deint' : 'black',
                          'dmer' : 'red', 'de5':'cyan', 'dens': 'goldenrod'}

#plot
sns.set_context("paper", font_scale=1.75)
plt.figure(figsize = (14,8))
bplot = sns.boxplot(x="region", y=dfMelt["value"], width = 0.8, 
                    data=dfMelt,  palette = pal,
                    hue = 'variable')

plt.xlabel('')
plt.ylabel('Difference in Trend (mm/year)')
plt.title('Obs Trend - Reconstruction Trend in mm/year')

plt.ylim([-6,6])

plt.grid()

plt.savefig('comparison_trends.svg', dpi = 400)

plt.show()