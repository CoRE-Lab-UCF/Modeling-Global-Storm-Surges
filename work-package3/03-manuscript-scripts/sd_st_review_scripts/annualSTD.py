"""
Created on Wed Dec 08 11:58:00 2021

get annual STD of a time series 

@author: Michael Tadesse

"""

import os 
import pandas as pd
from functools import reduce
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from datetime import datetime


def getAnnualStd(recon):

    # #get date time series
    # getDate = lambda x:x.split(' ')[0]
    # time_stamp1 = lambda x: (datetime.strptime(x, '%Y-%m-%d %H:%M:%S'))

    # recon['date'] = pd.DataFrame(list(map(time_stamp1, recon['date'])))

    recon['date'] = pd.to_datetime(recon['date'])

    #extract year column
    getYear = lambda x: x.year
    recon['year'] = pd.DataFrame(list(map(getYear, recon['date'])))

    # print(recon)


    #get STD    
    dat = recon.copy()

    sd = pd.DataFrame(columns=['year', 'value'])
    years = dat['year'].unique()
    for jj in years:
        currentYear = dat[dat['year'] == jj]
        # print(currentYear)
        df = pd.DataFrame([jj, currentYear["surge_reconsturcted"].std()]).T
        df.columns = ['year', 'value']
        sd = pd.concat([sd, df], axis = 0)
        # print(sd)
    
    return sd