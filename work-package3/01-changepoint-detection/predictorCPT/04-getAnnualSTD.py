"""  
this script computes the annual STD of each predictor
"""

import os 
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt 
from datetime import datetime

# change predictor here - slp - wnd_u - wnd_v -
home = "G:\\report\\year-3\\07-Fall-2020\\#3Paper\\data\\"\
    "changePointTimeSeries\\mamun-cpt-approach\\era5\\basePrat-data"\
        "\\allPred\\03-concatPred"
out = "G:\\report\\year-3\\07-Fall-2020\\#3Paper\\data\\"\
    "changePointTimeSeries\\mamun-cpt-approach\\era5\\basePrat-data"\
        "\\allPred\\04-annualSTD"

os.chdir(home)
tgList = os.listdir()

for ii in range(0, len(tgList)):
    os.chdir(home)
    print(tgList[ii])
    recon = pd.read_csv(tgList[ii])
    

    #get date time series
    getDate = lambda x:x.split(' ')[0]
    time_stamp1 = lambda x: (datetime.strptime(x, '%Y-%m-%d %H:%M:%S'))
    
    recon['date'] = pd.DataFrame(list(map(time_stamp1, recon['date'])))

    #extract year column
    getYear = lambda x: x.year
    recon['year'] = pd.DataFrame(list(map(getYear, recon['date'])))

    print(recon)


    #get STD    
    dat = recon.copy()

    sd = pd.DataFrame(columns=['year', 'value'])
    years = dat['year'].unique()
    for jj in years:
        currentYear = dat[dat['year'] == jj]
        # print(currentYear)
        df = pd.DataFrame([jj, currentYear["0"].std()]).T
        df.columns = ['year', 'value']
        sd = pd.concat([sd, df], axis = 0)
        # print(sd)
    
    os.chdir(out)
    
    sd.to_csv(tgList[ii])