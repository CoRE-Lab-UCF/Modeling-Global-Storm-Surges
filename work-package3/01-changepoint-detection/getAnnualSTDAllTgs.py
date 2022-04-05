# -*- coding: utf-8 -*-
"""
Created on Tue Jan 26 09:41:48 2021

get annual recon STD for all tgs

@author: Michael Tadesse
"""

import os 
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt 
from datetime import datetime

home = "G:\\data\\allReconstructions\\01_20cr"
out = "D:\\OneDrive - Knights - University of Central Florida\\UCF\\Projekt.28\\Report\\07-Fall-2020\\#3Paper\\data\\changePointTimeSeries\\20crSTD"

os.chdir(home)
tgList = os.listdir()

for ii in range(0, len(tgList)):
    os.chdir(home)
    print(ii)
    recon = pd.read_csv(tgList[ii])
    
    #get date time series
    getDate = lambda x:x.split(' ')[0]
    time_stamp1 = lambda x: (datetime.strptime(x, '%Y-%m-%d %H:%M:%S'))
    
    recon['date'] = pd.DataFrame(list(map(time_stamp1, recon['date'])))

    #extract year column
    getYear = lambda x: x.year
    recon['year'] = pd.DataFrame(list(map(getYear, recon['date'])))

    #get STD    
    dat = recon.copy()

    sd = pd.DataFrame(columns=['year', 'value'])
    years = dat['year'].unique()
    for jj in years:
        currentYear = dat[dat['year'] == jj]
        df = pd.DataFrame([jj, currentYear['surge_reconsturcted'].std()]).T
        df.columns = ['year', 'value']
        sd = pd.concat([sd, df], axis = 0)
        # print(sd)
    
    os.chdir(out)
    
    sd.to_csv(tgList[ii])