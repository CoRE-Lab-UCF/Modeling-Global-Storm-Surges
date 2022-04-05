"""  
Created on Wed Feb 02 07:38:00 2022
Modified on Thu Feb 03 07:32:00 2022

this script finds common period obs and recon percentiles
this is just for 99th/95th percentile - but can be adjusted for 
other percentiles

@author: Michael Getachew Tadesse

"""

import os
import os.path # check if a file exists
import pandas as pd
import matplotlib.pyplot as plt


dirHome = "G:\\report\\year-3\\07-Fall-2020\\#3Paper\\data\\"\
        "trend-analysis\\data\\03-obsSurge"

dirObs = "G:\\report\\year-3\\07-Fall-2020\\#3Paper\\data\\"\
        "trend-analysis\\data\\03-obsSurge\\percentiles\\99"

dirTwcr = "G:\\report\\year-3\\07-Fall-2020\\#3Paper\\data\\"\
        "trend-analysis\\data\\01-twcr\\02-percentiles\\99"

dirEra20c = "G:\\report\\year-3\\07-Fall-2020\\#3Paper\\data\\"\
        "trend-analysis\\data\\02-era20c\\02-percentiles\\99"

dirOut = "G:\\report\\year-3\\07-Fall-2020\\#3Paper\\data\\"\
        "trend-analysis\\data\\03-obsSurge\\plots"


os.chdir(dirHome)
tgList = pd.read_csv("obsSurgeAvailableDat.csv")


# only those with 30 years or plus and 75% availability and starting on or after 1930
df = tgList[(tgList['lengthAvailable'] >= 30) &(tgList['percAvailable'] >= 75)]
# df = df[df['start'] >= 1930]


countTwcr = 0
countEra20c = 0

# def plotExtremes(obs, twcr, era20c):
#     ###############################################
#     # plotting
#     # plot obs | twcr | era20c
#     plt.figure(figsize=(15,4))
#     plt.plot(obs['year'], obs['value'], label = "obs", color = "blue")
#     plt.plot(twcr['year'], twcr['value'], label = "twcr", color = "green")
#     plt.plot(era20c['year'], era20c['value'], label = "era20c", color = "magenta")
#     plt.legend()

#     # save figure
#     os.chdir(dirOut)
#     plt.savefig(tg.split('.csv')[0] + ".jpg")
#     ###############################################

# def compareTrends():
#     # compute trends
#     obsTrend, twcrTrend, era20cTrend = getTrends(obs, twcr, era20c, 100)
#     # print(obs)
#     lon = obs['lon'].unique()
#     lat = obs['lat'].unique()

#     newDf = pd.DataFrame([tg, lon, lat, len(twcr), obsTrend, twcrTrend, era20cTrend]).T
#     newDf.columns = ['tg', 'lon', 'lat', 'length', 'obsTrend', 'twcrTrend', 'era20cTrend']
#     dfTrend = pd.concat([dfTrend, newDf])


shortData = 0

for tg in df['tg']:
    print(tg)

    ################################################
    # select most recent start and earliest end date
    ################################################

    # check obs
    os.chdir(dirObs)
    obs = pd.read_csv(tg)

    ########################
    # set start and end year
    ########################
    start = 1930
    end = 2010

    # print("obs ", len(obs), start, end)

    # check twcr
    os.chdir(dirTwcr)
    if os.path.isfile(tg):
        twcr = pd.read_csv(tg)
        if (twcr['year'][0] > start):
            start = twcr['year'][0]
        if (twcr['year'][len(twcr)-1] < end):
            end = twcr['year'][len(twcr)-1]
    else:
        twcr = pd.DataFrame(columns = ['year', 'value', 'lon', 'lat'])
    # print("twcr ", len(twcr), start, end)


    # check era20c
    os.chdir(dirEra20c)
    if os.path.isfile(tg):
        era20c = pd.read_csv(tg)
        if (era20c['year'][0] > start):
            start = era20c['year'][0]
        if (era20c['year'][len(era20c)-1] < end):
            end = era20c['year'][len(era20c)-1]
    else:
        era20c = pd.DataFrame(columns = ['year', 'value', 'lon', 'lat'])
    # print("era20c ", len(era20c), start, end)

    ################################################

    # get obs data
    os.chdir(dirObs)
    obs = pd.read_csv(tg)
    obs = obs[(obs['year']>= start)&(obs['year']<= end)]
    obs['data'] = "obs"
    # print(obs)


    ##########################################
    # check again if length >= 30
    if len(obs) < 30:
        # print("\n")
        # print(tg, "***", "new start date shortened data")
        # print("\n")
        shortData += 1
        continue
    ##########################################


    # get twcr data
    os.chdir(dirTwcr)
    if os.path.isfile(tg):
        twcr = pd.read_csv(tg)
        twcr = twcr[(twcr['year']>= start)&(twcr['year']<= end)]
        twcr['data'] = "twcr"
        # print(twcr)
    else:
        print("twcr - {} no twcr data".format(tg))
        countTwcr = countTwcr + 1
    
    # get era20c data
    os.chdir(dirEra20c)
    if os.path.isfile(tg):
        era20c = pd.read_csv(tg)
        era20c = era20c[(era20c['year']>= start)&(era20c['year']<= end)]
        era20c['data'] = "era20c"
        # print(era20c)
        print("\n")
    else:
        print("era20c - {} no era20c data".format(tg))
        countEra20c = countEra20c + 1


    ################################################
    # check if either twcr or era20c is missing
    if ((len(twcr) == 0) or (len(era20c) == 0)):
        continue # skip plotting this tg trends

    ################################################
    # plotExtremes(obs, twcr, era20c)
    ################################################
    # concatenate obs, twcr, and era20c
    # this is to study the difference between trends
    newDat = pd.concat([obs, twcr, era20c], axis = 0)

    print(shortData)

    # save as csv
    os.chdir("G:\\report\\year-3\\07-Fall-2020\\#3Paper"\
        "\\data\\trend-analysis\\data\\allThreeTrends\\99_post1930_30yrs_75perc")
    
    newDat.to_csv(tg)