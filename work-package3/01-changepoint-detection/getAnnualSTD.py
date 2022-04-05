# -*- coding: utf-8 -*-
"""
Created on Tue Nov 10 09:41:05 2020

@author: Michael Tadesse

"""
import os 
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt 
from datetime import datetime

#get obs and recon files 
obs = pd.read_csv("wellingtonDailyMax.csv")
recon = pd.read_csv("wellington_071a_new_zealand.csv")

#get date time series
getDate = lambda x:x.split(' ')[0]
time_stamp2 = lambda x: (datetime.strptime(x, '%Y-%m-%d'))
time_stamp1 = lambda x: (datetime.strptime(x, '%Y-%m-%d %H:%M:%S'))

obs['date'] = pd.DataFrame(list(map(time_stamp2, obs['ymd'])))
recon['date'] = pd.DataFrame(list(map(time_stamp1, recon['date'])))

#plot time series and compare
##plot just obs
plt.figure(figsize = (10, 4))
plt.plot(obs['date'], obs['surge'], color = "blue", label = "observation")
plt.ylabel("Surge Height (m)")
plt.legend()

##plot just recon
plt.figure(figsize = (10, 4))
plt.plot(recon['date'], recon['surge_reconsturcted'], color = "red", label = "ERA-20C Reconstruction")
plt.ylabel("Surge Height (m)")
plt.legend()

##plot both obs and recon
plt.figure(figsize = (10, 4))
plt.plot(obs['date'], obs['surge'], color = "blue", label = "observation")
plt.plot(recon['date'], recon['surge_reconsturcted'], color = "red", label = "20-CR Reconstruction")
plt.ylabel("Surge Height (m)")
plt.legend()



#extract year column
# getYear = lambda x:x.split()[0].split('-')[0]

##or
getYear = lambda x: x.year
##getYear = lambda x:x.split('-')[0]

recon['year'] = pd.DataFrame(list(map(getYear, recon['date'])))


#get STD 
#change dat to obs/recon
#change surge to surge_reconsturcted for recon 
#change csv save name

dat = recon.copy()

sd = pd.DataFrame(columns=['year', 'value'])
years = dat['year'].unique()
for ii in years:
    currentYear = dat[dat['year'] == ii]
    df = pd.DataFrame([ii, currentYear['surge_reconsturcted'].std()]).T
    df.columns = ['year', 'value']
    sd = pd.concat([sd, df], axis = 0)
    print(sd)


sd.to_csv("wellingtonReconSTD.csv")


#combining obs and recon stds
year = pd.DataFrame(np.arange(1836,2016))
year.columns = ['year']

obsSTD = pd.read_csv("wellingtonObsSTD.csv")
reconSTD = pd.read_csv("wellingtonReconSTD.csv")

obsSTD = pd.merge(year, obsSTD, on="year", how="left")
reconSTD = pd.merge(year, reconSTD, on="year", how="left")

#plot std comparison
plt.figure(figsize = (10,4))
plt.plot(obsSTD['year'], obsSTD['value'], label = "observation STD", color = "blue")
plt.plot(reconSTD['year'], reconSTD['value'], label = "ERA-20C Recon STD", color = "red")
plt.ylabel("Surge Height (m)")
