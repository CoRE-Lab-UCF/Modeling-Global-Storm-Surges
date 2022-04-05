"""
Created on Wed Jul 29 08:30:00 2021
modified on Thu Sep 30 07:24:00 2021
modified on Wed Jan 26 12:09:00 2022

this program gets annual storm frequency for 
regionally clustered tgs 

all plots for the 1875-2015 period

it also averages the storm counts per region 

@author: Michael Getachew Tadesse

"""

from math import nan
import os
import math
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from scipy import stats
import statsmodels.api as sm
import statsmodels.stats.stattools as stools
from scipy.stats import normaltest
from datetime import datetime


geoRef = {
    "usw" : [-150, -120, 30, 60],
    "use" : [-80, -65, 25, 40],
    "gulf" : [-97, -82, 25, 30],
    "estAsia" : [110, 146, 20, 43],
    "aus_Nz" : [113, 180, -46, -11],
    "mediter" : [1.5, 15, 38, 45],
    "westEurope" : [-11, 9, 48, 59]
}


dirHome = {
    "twcr" : "G:\\report\\year-3\\07-Fall-2020\\#3Paper\\data\\"\
        "trend-analysis\\data\\01-twcr",
    "era20c" : "G:\\report\\year-3\\07-Fall-2020\\#3Paper\\data\\"\
        "trend-analysis\\data\\02-era20c"
}

dir_avg = "G:\\report\\year-3\\07-Fall-2020\\#3Paper\\data\\"\
        "trend-analysis\\data\\04-regionalStormFreq_v3"

# this directory also contains the intercepts + coefficients
dirOut = "G:\\report\\year-3\\07-Fall-2020\\#3Paper\\data\\"\
    "trend-analysis\\data\\05-regionalStormFreqTrends_v3"


# plotting regions
plt_regions = [ "era20c_gulf_num95.csv", "twcr_estAsia_num95.csv",
                "era20c_aus_Nz_num95.csv", "twcr_aus_Nz_num95.csv", 
                'era20c_kattegat_num95.csv', 'twcr_kattegat_num95.csv', 
                "era20c_westEurope_num95.csv", "twcr_westEurope_num95.csv",                  
                "era20c_use_num95.csv" ]

threshold = "num95"


# prepare plotting canvas
sns.set_context('paper', font_scale = 1.75)


fig, axes = plt.subplots(math.ceil(len(plt_regions)/2.0), 2, figsize = (12,12),
        gridspec_kw={'width_ratios': [1,1]})
fig.tight_layout(pad = 0.5)

# plotting panel counter
i = 0
j = 0


for region in plt_regions:

    print(region)

    # get recon+reg name
    recon = region.split('_')[0]

    reg = region.split('_num95.csv')[0].split(recon + "_")[1]
    
    print(reg)

    os.chdir(dirHome[recon])

    dat = pd.read_csv(recon+"TrendTgs.csv")

    # filter tgs
    if reg == "kattegat":
        getCountry = lambda x: ("norway" in x) | ("sweden" in x)
        dat['country'] = pd.DataFrame(list(map(getCountry, dat['tg'])))
        # print(dat)
        newDat = dat[dat['country']]
        # print(newDat)
    elif reg == "south_africa":
        getCountry = lambda x: (reg in x)
        dat['country'] = pd.DataFrame(list(map(getCountry, dat['tg'])))
        # print(dat)
        newDat = dat[dat['country']]
        # print(newDat)
    else:
        lonRange = geoRef[reg][:2]
        latRange = geoRef[reg][2:4]

        newDat = dat[((dat['lon'] >= lonRange[0]) & (dat['lon'] <= lonRange[1])) & \
                ((dat['lat'] >= latRange[0]) & (dat['lat'] <= latRange[1]))]
        # print(newDat)


    # load and plot tg data
    os.chdir(dirHome[recon] + "\\05-stormFrequency_v3")





#     plt.figure(figsize=(10,5))
    axes[i,j].set_ylabel('Annual exceedances above 95th Percentile')
    if recon == "twcr":
        t1930_label = "Trend [1930-2015]"
        t1950_label = "Trend [1950-2015]"
        axes[i,j].set_xlim([1925, 2020])
    else:
        t1930_label = "Trend [1930-2010]"
        t1950_label = "Trend [1950-2010]"
        axes[i,j].set_xlim([1925, 2015])

    axes[i,j].set_ylim([0, 40])

    # axes[i,j].set_title("{}".format(region))
    axes[i,j].text(1995, 3, reg, color = "k", fontsize = 12)

    # concatenate regional counts
    df = pd.DataFrame()
    first = True

    for tg in newDat['tg']:
        # print(tg)
        tgDat = pd.read_csv(tg)
        
        if first:
            df = tgDat[['year', threshold]] 
            first = False
        else:
            df = pd.merge(df, tgDat[['year', threshold]], on = "year", how="outer")
        
        # print(tgDat)

        axes[i,j].plot(tgDat[tgDat['year'] >= 1930]['year'], \
                tgDat[tgDat['year'] >= 1930][threshold], 'gray', lw = 0.75)

#         #####################################################################
#         ## plotting moving average
#         # plt.plot(tgDat['year'], tgDat[threshold].rolling(window = 10).mean())
#         #####################################################################

    
    os.chdir(dir_avg)
    
    df = pd.read_csv(region)
    # plot averaged storm count
    # change the year here base on plotting preference
    axes[i,j].plot(df[df['year'] >= 1930]['year'], df[df['year'] >= 1930]['avg'], \
            label = "Average Exceedance", color = "black", lw = "4")
    

    ##################################################################
    # plot trend lines
    ##################################################################

    os.chdir(dirOut)

    dat_avg_1930 = pd.read_csv("regionalTrends_1930_HAC.csv")
    # get only significant trends
    dat_avg_1930 = dat_avg_1930[dat_avg_1930['significance']]
    dat_avg_1950 = pd.read_csv("regionalTrends_1950_HAC.csv")
    # get only significant trends
    dat_avg_1950 = dat_avg_1950[dat_avg_1950['significance']]

    int_1930 = dat_avg_1930[dat_avg_1930['tg'] == region]['intercept'].values
    int_1950 = dat_avg_1950[dat_avg_1950['tg'] == region]['intercept'].values
    
    if len(int_1930) == 0:
        # set intercept high enough to exclude from plot
        int_1930 = 200
        trend_1930 = 0
        int_1950 = int_1950[0]
        trend_1950 = dat_avg_1950[dat_avg_1950['tg'] == region]['trend(storms/year)'].values[0]

    else:
        int_1930 = int_1930[0]
        trend_1930 = dat_avg_1930[dat_avg_1930['tg'] == region]['trend(storms/year)'].values[0]
        
        # check 1950 trends if they exist
        if len(int_1950) == 0:
            # set intercept high enough to exclude from plot
            int_1950 = 200
            trend_1950 = 0 
        else:
            int_1950 = int_1950[0]
            trend_1950 = dat_avg_1950[dat_avg_1950['tg'] == region]['trend(storms/year)'].values[0]


    # 1930 trend
    axes[i,j].plot(df[df['year'] >= 1930]['year'], int_1930 + \
        trend_1930*df[df['year'] >= 1930]['year'], \
             'r', label = t1930_label, lw = 2.5, ls = "--")
    axes[i,j].text(1995, 34, math.ceil(trend_1930*1000)/1000.0, color = "red", fontsize = 12)

    # 1950 trend
    axes[i,j].plot(df[df['year'] >= 1950]['year'], int_1950 + \
        trend_1950*df[df['year'] >= 1950]['year'], \
             'blue', label = t1950_label, lw = 2.5, ls = "--")
    axes[i,j].text(2005, 34, math.ceil(trend_1950*1000)/1000.0, color = "blue", fontsize = 12)


    axes[i,j].grid(b=None, which='major', axis= 'both', linestyle='-')
    axes[i,j].minorticks_on()
    axes[i,j].grid(b=None, which='minor', linestyle='--', axis="both", alpha=0.4)
    
    if i == 0:
        axes[i,j].legend(ncol = 1, fontsize = 12)

    # adjust panel counters
    if j == 1:
        j = 0
        i += 1
    else:
        j += 1
   
# save figure
os.chdir(dirOut)
plt.savefig("stormFreqTrends.svg", dpi = 400)


plt.show()

    



