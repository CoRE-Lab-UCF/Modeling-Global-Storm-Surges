"""
Created on Fri Nov 30 10:46:00 2021

This script plots predictor + recon variability
for twcr data - manuscript figure

@author: Michael Tadesse
"""

import os 
import pandas as pd
from functools import reduce
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from datetime import datetime
import seaborn as sns

# twcr std directories
dirStdSlp = "G:\\report\\year-3\\07-Fall-2020\\#3Paper\\data\\changePointTimeSeries\\"\
    "mamun-cpt-approach\\twcr\\0001-predCPT\\slp\\annualSTD"
dirStdUwnd = "G:\\report\\year-3\\07-Fall-2020\\#3Paper\\data\\changePointTimeSeries\\"\
    "mamun-cpt-approach\\twcr\\0001-predCPT\\wnd_u\\annualSTD"
dirStdVwnd = "G:\\report\\year-3\\07-Fall-2020\\#3Paper\\data\\changePointTimeSeries\\"\
    "mamun-cpt-approach\\twcr\\0001-predCPT\\wnd_v\\annualSTD"
dirStdRecon = "G:\\report\\year-3\\07-Fall-2020\\#3Paper\\data\\changePointTimeSeries\\"\
    "20crSTD"

# image saving dir
dirOut = "G:\\report\\year-3\\07-Fall-2020\\#3Paper\\p28ThirdManuscript\\manuscript\\figures"

# wanted tide gauges
tgs = [['astoria,or_572a_usa.csv', 'blue'],
       ['fremantle_012_australia.csv', 'limegreen'],
       ['base_prat_b_730b_chile.csv',  'red'],
       ['ny_alesund,norway_001.csv', 'black'],
       ['kerguelen_180a_france.csv', 'magenta']]


def plotSTD_CPT(tgs):

    sns.set_context('paper', font_scale = 2.0)
    fig, ax = plt.subplots(2, 2, figsize=(20, 12))
    fig.tight_layout(pad = 3.0)
    
    # fig.delaxes(ax[2,1]) # use when using odd number of panes
    
    # loop through twcr tgs
    for tg in tgs:

        print(tg[0])

        # slp std
        os.chdir(dirStdSlp)
        dat = pd.read_csv(tg[0])
        ax[0,0].scatter(dat['year'], dat['value'], color = tg[1], label = tg[0].split('.csv')[0], lw = 2)
        ax[0,0].legend()
        ax[0,0].set_ylabel("SLP annual variability in Pa")
        ax[0,0].grid(b=None, which='major', axis= 'both', linestyle='-')
        ax[0,0].minorticks_on()
        ax[0,0].grid(b=None, which='minor', linestyle='--', axis="both", alpha=0.4)
        ax[0,0].set_xlim([1830, 2020]) # set x axis limit

        ax[0,0].title.set_text("Sea Level Pressure (SLP)")

        # uwnd std
        os.chdir(dirStdUwnd)
        dat = pd.read_csv(tg[0])
        ax[0,1].scatter(dat['year'], dat['value'], color = tg[1], label = tg[0].split('.csv')[0], lw = 2)
        # ax[0,1].legend()
        ax[0,1].set_ylabel("Standard Deviation in m/s")
        ax[0,1].minorticks_on()
        ax[0,1].grid(b=None, which='major', axis= 'both', linestyle='-')
        ax[0,1].grid(b=None, which='minor', linestyle='--', axis="both", alpha=0.4)
        ax[0,1].set_xlim([1830, 2020]) # set x axis limit

        ax[0,1].title.set_text("Zonal Wind Speed (Wnd_U)")

        # vwnd std
        os.chdir(dirStdVwnd)
        dat = pd.read_csv(tg[0])
        ax[1,0].scatter(dat['year'], dat['value'], color = tg[1], label = tg[0].split('.csv')[0], lw = 2)
        # ax[1,0].legend()
        ax[1,0].set_ylabel("Standard Deviation in m/s")
        ax[1,0].grid(b=None, which='major', axis= 'both', linestyle='-')
        ax[1,0].minorticks_on()
        ax[1,0].grid(b=None, which='minor', linestyle='--', axis="both", alpha=0.4)
        ax[1,0].set_xlim([1830, 2020]) # set x axis limit

        ax[1,0].title.set_text("Meridional Wind Speed (Wnd_V)")


        # recon std
        os.chdir(dirStdRecon)
        dat = pd.read_csv(tg[0])
        ax[1,1].plot(dat['year'], dat['value'], color = tg[1], label = tg[0].split('.csv')[0], lw = 2)
        # ax[1,1].legend()
        ax[1,1].set_ylabel("Standard Deviation in m")
        ax[1,1].grid(b=None, which='major', axis= 'both', linestyle='-')
        ax[1,1].minorticks_on()
        ax[1,1].grid(b=None, which='minor', linestyle='--', axis="both", alpha=0.4)
        ax[1,1].set_xlim([1830, 2020]) # set x axis limit

        ax[1,1].title.set_text("Daily Maximum Surge")



    # plt.suptitle(tg[0].split('.csv')[0] + " - twcr", y = 0.9999999, fontweight="bold")
    # plt.show()  

    # save image
    os.chdir(dirOut)
    plt.savefig("twcrOutlierTideGauges.svg", dpi=400)

plotSTD_CPT(tgs)
