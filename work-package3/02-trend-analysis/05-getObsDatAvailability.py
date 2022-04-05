"""  
check how much data is available in observed surges 
get the percentage of missing data

"""

from math import nan
import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy import stats
import statsmodels.api as sm
from scipy.stats import normaltest
from datetime import datetime


dirHome = "G:\\report\\year-3\\07-Fall-2020\\#3Paper\\data\\"\
        "trend-analysis\\data\\03-obsSurge\\percentiles\\99"

dirOut = "G:\\report\\year-3\\07-Fall-2020\\#3Paper\\data\\"\
        "trend-analysis\\data\\03-obsSurge"


os.chdir(dirHome)

tgList = os.listdir()

# create empty dataframe
df = pd.DataFrame(columns = ['tg', 'lon', 'lat', 'start', 'end', \
    'lengthTheoretical', 'lengthAvailable', 'percAvailable'])

for tg in tgList:
    print(tg)

    dat = pd.read_csv(tg)

    lon = dat['lon'].unique()[0]
    lat = dat['lat'].unique()[0]
    start = dat['year'][0]
    end = dat['year'][len(dat)-1]
    lengthTheoretical = end - start + 1
    lengthAvailable = len(dat)
    percAvailable = lengthAvailable*100/lengthTheoretical
    
    newDf = pd.DataFrame([tg, lon, lat, start, end, lengthTheoretical, lengthAvailable, percAvailable]).T
    newDf.columns = ['tg', 'lon', 'lat', 'start', 'end', 'lengthTheoretical', 'lengthAvailable', 'percAvailable']

    df = pd.concat([df, newDf])

print(df)

# save csv
os.chdir(dirOut)
df.to_csv("obsSurgeAvailableDat.csv")





