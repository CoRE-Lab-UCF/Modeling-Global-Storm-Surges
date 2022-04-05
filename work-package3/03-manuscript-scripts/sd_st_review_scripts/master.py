"""
Created on Wed Dec 08 11:23:00 2021

get the interquartile range 

@author: Michael Tadesse

"""

import os 
import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime
from annualSTD import getAnnualStd
from getAnnualIQR import getAnnualIQR
from plotTimeSeries import plotTimeSeries
from getObsSurge import getObsSurge



dir_home = "G:\\data\\allReconstructions\\01_20cr"

os.chdir(dir_home)


tg = "hornbaek_838a_denmark.csv"

dat = pd.read_csv(tg)[['date', 'surge_reconsturcted']]



def start(dat, prompt):
    if prompt == 'obs':
        # plot original time series
        plotTimeSeries(dat, tg, 'o')
    elif prompt == 'diff':
        os.chdir(dir_home)
        recon = pd.read_csv(tg)
        recon['date'] = pd.to_datetime(dat['date'], format='%Y-%m-%d')
        recon.reset_index(inplace = True)
        recon = recon[['date', 'surge_reconsturcted']]
        print(recon)

        obs = getObsSurge(tg)
        obs = obs[['date', 'surge']]
        print(obs)

        # get same period
        obs_recon = pd.merge(obs, recon, on='date', how='inner')
        print(obs_recon)
        os.chdir("G:\\report\\year-3\\07-Fall-2020\\#3Paper\\data"\
                "\\changePointTimeSeries\\additionalTest\\difference")
        obs_recon.to_csv(tg)
        
        plt.figure(figsize = (16,4))
        plt.plot(obs_recon['date'], obs_recon['surge'] - obs_recon['surge_reconsturcted'])
        plt.show()

    elif prompt == 'std':
        # get annual std
        aSTD = getAnnualStd(dat)
        print(aSTD)
        plotTimeSeries(aSTD, tg, 's')
    elif prompt == 'iqr':
        # get annual std
        iqr = getAnnualIQR(dat)
        os.chdir("G:\\report\\year-3\\07-Fall-2020\\#3Paper\\"\
                "data\\changePointTimeSeries\\additionalTest\\iqr")
        iqr.to_csv(tg)
        print(iqr)
        plotTimeSeries(iqr, tg, 'i')    

start(dat, 'iqr')