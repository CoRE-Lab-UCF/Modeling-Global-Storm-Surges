# -*- coding: utf-8 -*-
"""
Created on Fri Oct 30 09:36:22 2020
F:\OneDrive - Knights - University of Central Florida\UCF\Projekt.28\Report\07-Fall-2020\#3Paper\data\changePointTimeSeries\historicSurge
get daily max surge 

@author: Michael Tadesse
"""
import pandas as pd

#load surge file
tg = 'boston.csv'
dat = pd.read_csv(tg)
dat.drop('Unnamed: 0', axis = 1, inplace = True)

#get unique years
getDays = lambda x: x.split()[0]

dat['days'] = pd.DataFrame(list(map(getDays, dat['date'])))

days = dat['days'].unique()

#get daily max by grouping
datGrouped = dat.groupby("days")
datMax = datGrouped.max()
datMax = datMax.reset_index()

#save as csv
saveName = tg.split('.csv')[0] + 'DailyMax.csv'
datMax.to_csv(saveName)
