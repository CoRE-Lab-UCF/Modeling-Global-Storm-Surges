"""  
this script plots predictor and Recon STDs and CPTs
"""

import os 
import pandas as pd
from functools import reduce
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from datetime import datetime

# std directories
dirStdSlp = "G:\\report\\year-3\\07-Fall-2020\\#3Paper\\data\\changePointTimeSeries\\"\
    "mamun-cpt-approach\\twcr\\0001-predCPT\\slp\\annualSTD"
dirStdUwnd = "G:\\report\\year-3\\07-Fall-2020\\#3Paper\\data\\changePointTimeSeries\\"\
    "mamun-cpt-approach\\twcr\\0001-predCPT\\wnd_u\\annualSTD"
dirStdVwnd = "G:\\report\\year-3\\07-Fall-2020\\#3Paper\\data\\changePointTimeSeries\\"\
    "mamun-cpt-approach\\twcr\\0001-predCPT\\wnd_v\\annualSTD"
dirStdRecon = "G:\\report\\year-3\\07-Fall-2020\\#3Paper\\data\\changePointTimeSeries\\"\
    "20crSTD"

# cpt directories
dirBcpSlp = "G:\\report\\year-3\\07-Fall-2020\\#3Paper\\data\\changePointTimeSeries\\"\
    "mamun-cpt-approach\\twcr\\0001-predCPT\\slp\\originalBCP"
dirBcpUwnd = "G:\\report\\year-3\\07-Fall-2020\\#3Paper\\data\\changePointTimeSeries\\"\
    "mamun-cpt-approach\\twcr\\0001-predCPT\\wnd_u\\originalBCP"
dirBcpVwnd = "G:\\report\\year-3\\07-Fall-2020\\#3Paper\\data\\changePointTimeSeries\\"\
    "mamun-cpt-approach\\twcr\\0001-predCPT\\wnd_v\\originalBCP"
dirBcpRecon = "G:\\report\\year-3\\07-Fall-2020\\#3Paper\\data\\changePointTimeSeries\\"\
    "20crBCP"

# #define a plot object that can be manipulated
#update the rows of the subplot here 
fig, ax = plt.subplots(4, 2, figsize=(10, 8))
fig.tight_layout(pad = 0.8)


def plotSTD_CPT(tg):

    # slp std
    os.chdir(dirStdSlp)
    dat = pd.read_csv(tg)
    ax[0,0].plot(dat['year'], dat['value'], color = "blue", label = "slpSTD", lw = 2)
    ax[0,0].legend()
    ax[0,0].set_ylabel("variability in Pa")

    # uwnd std
    os.chdir(dirStdUwnd)
    dat = pd.read_csv(tg)
    ax[1,0].plot(dat['year'], dat['value'], color = "green", label = "uwndSTD", lw = 2)
    ax[1,0].legend()
    ax[1,0].set_ylabel("variability in m")

    # vwnd std
    os.chdir(dirStdVwnd)
    dat = pd.read_csv(tg)
    ax[2,0].plot(dat['year'], dat['value'], color = "magenta", label = "vwndSTD", lw = 2)
    ax[2,0].legend()
    ax[2,0].set_ylabel("variability in m")

    # recon std
    os.chdir(dirStdRecon)
    dat = pd.read_csv(tg)
    ax[3,0].plot(dat['year'], dat['value'], color = "red", label = "reconSTD", lw = 2)
    ax[3,0].legend()
    ax[3,0].set_ylabel("variability in m")

    ######################################################################################

    # slp bcp
    os.chdir(dirBcpSlp)
    dat = pd.read_csv(tg)
    ax[0,1].plot(dat['year'], dat['prob'], color = "blue", label = "slpBCP", lw = 2)
    ax[0,1].legend()
    ax[0,1].set_ylim([0,1])
    ax[0,1].set_ylabel("probability")



    # uwnd bcp
    os.chdir(dirBcpUwnd)
    dat = pd.read_csv(tg)
    ax[1,1].plot(dat['year'], dat['prob'], color = "green", label = "uwndBCP", lw = 2)
    ax[1,1].legend()
    ax[1,1].set_ylim([0,1])
    ax[1,1].set_ylabel("probability")


    # vwnd bcp
    os.chdir(dirBcpVwnd)
    dat = pd.read_csv(tg)
    ax[2,1].plot(dat['year'], dat['prob'], color = "magenta", label = "vwndBCP", lw = 2)
    ax[2,1].legend()
    ax[2,1].set_ylim([0,1])
    ax[2,1].set_ylabel("probability")


    # recon bcp
    os.chdir(dirBcpRecon)
    dat = pd.read_csv(tg)
    ax[3,1].plot(dat['year'], dat['prob'], color = "red", label = "reconBCP", lw = 2)
    ax[3,1].legend()
    ax[3,1].set_ylim([0,1])
    ax[3,1].set_ylabel("probability")


    
    plt.suptitle(tg.split('.csv')[0], y = 0.9999999, fontweight="bold")
    plt.show()  


plotSTD_CPT('fremantle_012_australia.csv')