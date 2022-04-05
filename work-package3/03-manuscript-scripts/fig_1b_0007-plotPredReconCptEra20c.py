"""  
this script plots predictor and Recon STDs and the four BCPs with their average - era20c
"""

import os 
import pandas as pd
from functools import reduce
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from datetime import datetime

# era20c std directories
dirStdSlp = "G:\\report\\year-3\\07-Fall-2020\\#3Paper\\data\\changePointTimeSeries\\"\
    "mamun-cpt-approach\\era20c\\0001-predCPT\\slp\\annualSTD"
dirStdUwnd = "G:\\report\\year-3\\07-Fall-2020\\#3Paper\\data\\changePointTimeSeries\\"\
    "mamun-cpt-approach\\era20c\\0001-predCPT\\wnd_u\\annualSTD"
dirStdVwnd = "G:\\report\\year-3\\07-Fall-2020\\#3Paper\\data\\changePointTimeSeries\\"\
    "mamun-cpt-approach\\era20c\\0001-predCPT\\wnd_v\\annualSTD"
dirStdRecon = "G:\\report\\year-3\\07-Fall-2020\\#3Paper\\data\\changePointTimeSeries\\"\
    "era20cSTD"

# era20c cpt directories
dirBcpSlp = "G:\\report\\year-3\\07-Fall-2020\\#3Paper\\data\\changePointTimeSeries\\"\
    "mamun-cpt-approach\\era20c\\0001-predCPT\\slp\\originalBCP"
dirBcpUwnd = "G:\\report\\year-3\\07-Fall-2020\\#3Paper\\data\\changePointTimeSeries\\"\
    "mamun-cpt-approach\\era20c\\0001-predCPT\\wnd_u\\originalBCP"
dirBcpVwnd = "G:\\report\\year-3\\07-Fall-2020\\#3Paper\\data\\changePointTimeSeries\\"\
    "mamun-cpt-approach\\era20c\\0001-predCPT\\wnd_v\\originalBCP"
dirBcpRecon = "G:\\report\\year-3\\07-Fall-2020\\#3Paper\\data\\changePointTimeSeries\\"\
    "era20cBCP"

# era20c cptSA file
dirCptSA = "G:\\report\\year-3\\07-Fall-2020\\#3Paper\\data\\changePointTimeSeries\\"\
    "mamun-cpt-approach\\era20c\\0001-predCPT\\cptSA"

# era20c avg cpt
dirAvgCpt = "G:\\report\\year-3\\07-Fall-2020\\#3Paper\\data\\changePointTimeSeries\\"\
    "mamun-cpt-approach\\era20c\\0001-predCPT\\combinedBCP"

# image saving dir
dirOut = "G:\\report\\year-3\\07-Fall-2020\\#3Paper\\p28ThirdManuscript\\manuscript\\figures"


# observed surge annual std
dirObsStd = "G:\\report\\year-3\\07-Fall-2020\\#3Paper\\data\\"\
        "changePointTimeSeries\\mamun-cpt-approach\\obsSurge\\01-annualSTD"



def plotSTD_CPT(tg):

    print(tg)
    
    fig, ax = plt.subplots(3, 2, figsize=(20, 12))

    fig.tight_layout(pad = 3.0)
    
    sns.set_context('paper', font_scale = 2.0)

    # to remove unwanted figure pane
    # fig.delaxes(ax[2,1]) # use when using odd number of panes


    # slp std
    os.chdir(dirStdSlp)
    dat = pd.read_csv(tg)
    ax[0,0].plot(dat['year'], dat['value'], color = "blue", label = "slpSTD", lw = 2)
    ax[0,0].legend()
    ax[0,0].set_ylabel("annual variability in Pa", fontsize = 18)

    ax[0,0].xaxis.set_tick_params(labelsize=16)
    ax[0,0].yaxis.set_tick_params(labelsize=16)

    ax[0,0].grid(b=None, which='major', axis= 'both', linestyle='-')
    ax[0,0].minorticks_on()
    ax[0,0].grid(b=None, which='minor', linestyle='--', axis="both", alpha=0.4)
    ax[0,0].set_xlim([1830, 2020]) # set x axis limit

    # uwnd std
    os.chdir(dirStdUwnd)
    dat = pd.read_csv(tg)
    ax[0,1].plot(dat['year'], dat['value'], color = "green", label = "uwndSTD", lw = 2)
    ax[0,1].legend()
    ax[0,1].set_ylabel("annual variability in m/s", fontsize = 18)

    ax[0,1].xaxis.set_tick_params(labelsize=16)
    ax[0,1].yaxis.set_tick_params(labelsize=16)

    ax[0,1].minorticks_on()
    ax[0,1].grid(b=None, which='major', axis= 'both', linestyle='-')
    ax[0,1].grid(b=None, which='minor', linestyle='--', axis="both", alpha=0.4)
    ax[0,1].set_xlim([1830, 2020]) # set x axis limit

    # vwnd std
    os.chdir(dirStdVwnd)
    dat = pd.read_csv(tg)
    ax[1,0].plot(dat['year'], dat['value'], color = "magenta", label = "vwndSTD", lw = 2)
    ax[1,0].legend()
    ax[1,0].set_ylabel("annual variability in m/s", fontsize = 18)

    ax[1,0].xaxis.set_tick_params(labelsize=16)
    ax[1,0].yaxis.set_tick_params(labelsize=16)

    ax[1,0].grid(b=None, which='major', axis= 'both', linestyle='-')
    ax[1,0].minorticks_on()
    ax[1,0].grid(b=None, which='minor', linestyle='--', axis="both", alpha=0.4)
    ax[1,0].set_xlim([1830, 2020]) # set x axis limit

    # recon std
    os.chdir(dirStdRecon)
    dat = pd.read_csv(tg)
    ax[1,1].plot(dat['year'], dat['value'], color = "red", label = "reconSTD", lw = 2)
    ax[1,1].set_ylabel("annual variability in m", fontsize = 18)

    ax[1,1].xaxis.set_tick_params(labelsize=16)
    ax[1,1].yaxis.set_tick_params(labelsize=16)

    ax[1,1].grid(b=None, which='major', axis= 'both', linestyle='-')
    ax[1,1].minorticks_on()
    ax[1,1].grid(b=None, which='minor', linestyle='--', axis="both", alpha=0.4)
    ax[1,1].set_xlim([1830, 2020]) # set x axis limit

    # predictor+recon average cpt from cptSA
    os.chdir(dirCptSA)
    dat = pd.read_csv("era20cCptSA.csv")
    cpt_30 = dat[dat['tg'] == tg]['p_30'].values[0]
    cpt_25 = dat[dat['tg'] == tg]['p_25'].values[0]
    cpt_20 = dat[dat['tg'] == tg]['p_20'].values[0]
    cpt_15 = dat[dat['tg'] == tg]['p_15'].values[0]
    

    # print(cpt_30)

    # changepoints
    ax[1,1].axvline(x = cpt_30, color = "black", ls = "--", 
        lw = 2.0, label = "30%: {}".format(cpt_30))
    ax[1,1].axvline(x = cpt_25, color = "dimgrey", ls = "--", 
        lw = 1.75, label = "25%: {}".format(cpt_25))
    ax[1,1].axvline(x = cpt_20, color = "darkgrey", ls = "--", 
        lw = 1.5, label = "20%: {}".format(cpt_20))
    ax[1,1].axvline(x = cpt_15, color = "silver", ls = "--", 
        lw = 1.5, label = "15%: {}".format(cpt_15))
    ax[1,1].legend()

    ######################################################################################

    # slp bcp
    os.chdir(dirBcpSlp)
    dat = pd.read_csv(tg)
    ax[2,0].scatter(dat['year'], dat['prob'], s = 10,  color = "blue", label = "slpBCP")
    ax[2,0].set_ylim([0,1])
    ax[2,0].set_ylabel("changepoint probability", fontsize = 18)

    ax[2,0].xaxis.set_tick_params(labelsize=16)
    ax[2,0].yaxis.set_tick_params(labelsize=16)

    ax[2,0].grid(b=None, which='major', axis= 'both', linestyle='-')
    ax[2,0].minorticks_on()
    ax[2,0].grid(b=None, which='minor', linestyle='--', axis="both", alpha=0.4)
    ax[2,0].set_xlim([1830, 2020]) # set x axis limit



    # uwnd bcp
    os.chdir(dirBcpUwnd)
    dat = pd.read_csv(tg)
    ax[2,0].scatter(dat['year'], dat['prob'], s = 10, color = "green", label = "uwndBCP")
    ax[2,0].set_ylim([0,1])
    ax[2,0].set_ylabel("changepoint probability", fontsize = 18)

    ax[2,0].xaxis.set_tick_params(labelsize=16)
    ax[2,0].yaxis.set_tick_params(labelsize=16)



    # vwnd bcp
    os.chdir(dirBcpVwnd)
    dat = pd.read_csv(tg)
    ax[2,0].scatter(dat['year'], dat['prob'], s = 10,  color = "magenta", label = "vwndBCP")
    ax[2,0].set_ylim([0,1])
    ax[2,0].set_ylabel("changepoint probability", fontsize = 18)

    ax[2,0].xaxis.set_tick_params(labelsize=16)
    ax[2,0].yaxis.set_tick_params(labelsize=16)



    # recon bcp
    os.chdir(dirBcpRecon)
    dat = pd.read_csv(tg)
    ax[2,0].scatter(dat['year'], dat['prob'], s = 10, color = "red", label = "reconBCP")
    ax[2,0].set_ylim([0,1])
    ax[2,0].set_ylabel("changepoint probability", fontsize = 18)

    ax[2,0].xaxis.set_tick_params(labelsize=16)
    ax[2,0].yaxis.set_tick_params(labelsize=16)


    # era20c avg bcp
    os.chdir(dirAvgCpt)
    dat = pd.read_csv(tg)
    dat['p_avg'] = dat.iloc[:,2:6].mean(axis = 1)

    # changepoints
    ax[2,0].axvline(x = cpt_30, color = "black", ls = "--", 
        lw = 2.0, label = "30%: {}".format(cpt_30))
    ax[2,0].axvline(x = cpt_25, color = "dimgrey", ls = "--", 
        lw = 2.0, label = "25%: {}".format(cpt_25))
    ax[2,0].axvline(x = cpt_20, color = "darkgrey", ls = "--", 
        lw = 2.0, label = "20%: {}".format(cpt_20))
    ax[2,0].axvline(x = cpt_15, color = "silver", ls = "--", 
        lw = 2.0, label = "15%: {}".format(cpt_15))

    ax[2,0].plot(dat['year'], dat['p_avg'], lw = 1, color = "black", label = "average BCP")
    ax[2,0].legend(ncol = 2)

    # obsSurge std
    os.chdir(dirObsStd)
    dat = pd.read_csv(tg)
    ax[2,1].set_xlim([1830, 2020]) # set x axis limit
    ax[2,1].plot(dat['year'], dat['value'],  color = "teal", label = "obsSTD")
    ax[2,1].set_ylabel("annual variability in m", fontsize = 18)

    ax[2,1].xaxis.set_tick_params(labelsize=16)
    ax[2,1].yaxis.set_tick_params(labelsize=16)

    ax[2,1].grid(b=None, which='major', axis= 'both', linestyle='-')
    ax[2,1].minorticks_on()
    ax[2,1].grid(b=None, which='minor', linestyle='--', axis="both", alpha=0.4)
    ax[2,1].legend()



    
    # plt.suptitle(tg.split('.csv')[0] + " - era20c", y = 0.9999999, fontweight="bold")
    # plt.show()  

    # save image
    os.chdir(dirOut)
    plt.savefig("fig_1b_astoria,or_572a_usa.svg", dpi=400)


######################################
# # loop through twcr tgs

# os.chdir(dirCptSA)
# dat = pd.read_csv("twcrCptSA.csv")

# # print(dat)

# for tg in dat['tg']:
#     plotSTD_CPT(tg)
######################################


# plot single tg result
plotSTD_CPT('astoria,or_572a_usa.csv')