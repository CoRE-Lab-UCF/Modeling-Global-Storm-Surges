"""  
Modified on Fri Feb 04 07:31:00 2022

this script computes the annual STD of each predictor

@author: Michael Tadesse

"""

import os 
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt 
from datetime import datetime

# change predictor here - slp - wnd_u - wnd_v -
home = "G:\\report\\year-3\\07-Fall-2020\\#3Paper\\data\\"\
        "changePointTimeSeries\\mamun-cpt-approach\\extended_tgs"
out = "G:\\report\\year-3\\07-Fall-2020\\#3Paper\\data\\"\
        "changePointTimeSeries\\mamun-cpt-approach\\obsSurge\\01-annualSTD"

os.chdir(home)
tgList = os.listdir()

for ii in range(0, len(tgList)):
    os.chdir(home)
    print(tgList[ii])
    obs = pd.read_csv(tgList[ii])
    
    #get date time series
    getDate = lambda x:x.split(' ')[0]
    time_stamp1 = lambda x: (datetime.strptime(x, '%Y-%m-%d %H:%M:%S'))
    
    obs['date'] = pd.DataFrame(list(map(time_stamp1, obs['date'])))
    
    #extract year column
    getYear = lambda x: x.year
    obs['year'] = pd.DataFrame(list(map(getYear, obs['date'])))
    
    #get STD    
    dat = obs.copy()

    sd = pd.DataFrame(columns=['year', 'value'])
    years = dat['year'].unique()
    for jj in years:
        currentYear = dat[dat['year'] == jj]
        # print(currentYear)
        df = pd.DataFrame([jj, currentYear['surge'].std()]).T
        df.columns = ['year', 'value']
        sd = pd.concat([sd, df], axis = 0)
        # print(sd)
    
    os.chdir(out)
    
    sd.to_csv(tgList[ii])