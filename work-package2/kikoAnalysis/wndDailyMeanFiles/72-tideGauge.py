# -*- coding: utf-8 -*-
"""
Created on Tue Sep 29 09:40:12 2020

@author: Michael Tadesse
"""

import os 
import pandas as pd

dir_in = "/lustre/fs0/home/mtadesse/eraFiveConcat"
dir_out = "/lustre/fs0/home/mtadesse/dailyPred"

os.chdir(dir_in)
tgList = os.listdir()

x = 72
y = 73

#looping through individual tide gauges
for ii in range(x, y):
    os.chdir(tgList[ii])
    
    #load file
    wnd = pd.read_csv('wndRest.csv')
    wnd.drop(['Unnamed: 0'], axis = 1, inplace = True)
    
    #get daily time steps
    getDays = lambda x: x.split()[0]
    wnd['days'] = pd.DataFrame(list(map(getDays, wnd['date'])))
    
    #get unique days
    days = wnd['days'].unique()
    
    first = True
    for d in days:
        currentDay = wnd[wnd['days'] == d]
        print(currentDay)
        if first:
            currentMean = pd.DataFrame(currentDay.mean(axis = 0)).T
            currentMean['date'] = d
            first = False
            dailyMean = currentMean
        else:
            currentMean = pd.DataFrame(currentDay.mean(axis = 0)).T
            currentMean['date'] = d        
            dailyMean = pd.concat([dailyMean, currentMean], axis = 0)
            
    dailyMean.to_csv('wndDaily.csv')
