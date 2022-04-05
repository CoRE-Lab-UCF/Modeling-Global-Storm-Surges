"""

Created on Thu Mar 04 07:59:00 2022

plot the changepoint analysis (G20CR+GE20C) combined

@author: Michael Getachew Tadesse

"""

import os 
import math
import pandas as pd
from functools import reduce
import numpy as np
import seaborn as sns
import matplotlib as mpl
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from datetime import datetime


########################
# directories
########################


# twcr std directories
dirStdSlp_t = "G:\\report\\year-3\\07-Fall-2020\\#3Paper\\data\\changePointTimeSeries\\"\
    "mamun-cpt-approach\\twcr\\0001-predCPT\\slp\\annualSTD"
dirStdUwnd_t = "G:\\report\\year-3\\07-Fall-2020\\#3Paper\\data\\changePointTimeSeries\\"\
    "mamun-cpt-approach\\twcr\\0001-predCPT\\wnd_u\\annualSTD"
dirStdVwnd_t = "G:\\report\\year-3\\07-Fall-2020\\#3Paper\\data\\changePointTimeSeries\\"\
    "mamun-cpt-approach\\twcr\\0001-predCPT\\wnd_v\\annualSTD"
dirStdRecon_t = "G:\\report\\year-3\\07-Fall-2020\\#3Paper\\data\\changePointTimeSeries\\"\
    "20crSTD"

# era20c std directories
dirStdSlp_e = "G:\\report\\year-3\\07-Fall-2020\\#3Paper\\data\\changePointTimeSeries\\"\
    "mamun-cpt-approach\\era20c\\0001-predCPT\\slp\\annualSTD"
dirStdUwnd_e = "G:\\report\\year-3\\07-Fall-2020\\#3Paper\\data\\changePointTimeSeries\\"\
    "mamun-cpt-approach\\era20c\\0001-predCPT\\wnd_u\\annualSTD"
dirStdVwnd_e = "G:\\report\\year-3\\07-Fall-2020\\#3Paper\\data\\changePointTimeSeries\\"\
    "mamun-cpt-approach\\era20c\\0001-predCPT\\wnd_v\\annualSTD"
dirStdRecon_e = "G:\\report\\year-3\\07-Fall-2020\\#3Paper\\data\\changePointTimeSeries\\"\
    "era20cSTD"

# twcr cpt directories
dirBcpSlp_t = "G:\\report\\year-3\\07-Fall-2020\\#3Paper\\data\\changePointTimeSeries\\"\
    "mamun-cpt-approach\\twcr\\0001-predCPT\\slp\\originalBCP"
dirBcpUwnd_t = "G:\\report\\year-3\\07-Fall-2020\\#3Paper\\data\\changePointTimeSeries\\"\
    "mamun-cpt-approach\\twcr\\0001-predCPT\\wnd_u\\originalBCP"
dirBcpVwnd_t = "G:\\report\\year-3\\07-Fall-2020\\#3Paper\\data\\changePointTimeSeries\\"\
    "mamun-cpt-approach\\twcr\\0001-predCPT\\wnd_v\\originalBCP"
dirBcpRecon_t = "G:\\report\\year-3\\07-Fall-2020\\#3Paper\\data\\changePointTimeSeries\\"\
    "20crBCP"

# era20c cpt directories
dirBcpSlp_e = "G:\\report\\year-3\\07-Fall-2020\\#3Paper\\data\\changePointTimeSeries\\"\
    "mamun-cpt-approach\\era20c\\0001-predCPT\\slp\\originalBCP"
dirBcpUwnd_e = "G:\\report\\year-3\\07-Fall-2020\\#3Paper\\data\\changePointTimeSeries\\"\
    "mamun-cpt-approach\\era20c\\0001-predCPT\\wnd_u\\originalBCP"
dirBcpVwnd_e = "G:\\report\\year-3\\07-Fall-2020\\#3Paper\\data\\changePointTimeSeries\\"\
    "mamun-cpt-approach\\era20c\\0001-predCPT\\wnd_v\\originalBCP"
dirBcpRecon_e = "G:\\report\\year-3\\07-Fall-2020\\#3Paper\\data\\changePointTimeSeries\\"\
    "era20cBCP"


# twcr cptSA file
dirCptSA_t = "G:\\report\\year-3\\07-Fall-2020\\#3Paper\\data\\changePointTimeSeries\\"\
    "mamun-cpt-approach\\twcr\\0001-predCPT\\cptSA"

# twcr avg cpt
dirAvgCpt_t = "G:\\report\\year-3\\07-Fall-2020\\#3Paper\\data\\changePointTimeSeries\\"\
    "mamun-cpt-approach\\twcr\\0001-predCPT\\combinedBCP"


# era20c cptSA file
dirCptSA_e = "G:\\report\\year-3\\07-Fall-2020\\#3Paper\\data\\changePointTimeSeries\\"\
    "mamun-cpt-approach\\era20c\\0001-predCPT\\cptSA"

# era20c avg cpt
dirAvgCpt_e = "G:\\report\\year-3\\07-Fall-2020\\#3Paper\\data\\changePointTimeSeries\\"\
    "mamun-cpt-approach\\era20c\\0001-predCPT\\combinedBCP"

# image saving dir
dirOut = "G:\\report\\year-3\\07-Fall-2020\\#3Paper\\p28ThirdManuscript\\manuscript\\figures"

# modified to plot extended astoria STD
dirObsStd = "G:\\report\\year-3\\07-Fall-2020\\#3Paper\\data\\"\
                "changePointTimeSeries\\mamun-cpt-approach\\extended_tgs"



def plotSTD_CPT(tg):

    print(tg)
    
    fig, ax = plt.subplots(3, 2, figsize=(20, 12))

    fig.tight_layout(pad = 3.0)
    
    sns.set_context('paper', font_scale = 2.0)

    # format axis decimal places
    fmt = lambda x, pos: '{}'.format(math.ceil((x)*100.0)/100.0, pos)

    # to remove unwanted figure pane
    # fig.delaxes(ax[2,1]) # use when using odd number of panes




    # G-20CR slp std
    os.chdir(dirStdSlp_t)
    dat = pd.read_csv(tg)
    ax[0,0].plot(dat['year'], dat['value'], color = "#e6194b", label = "slpSTD [G-20CR]", lw = 2)
    ax[0,0].legend()
    ax[0,0].set_ylabel("annual variability in Pa", fontsize = 18)

    ax[0,0].xaxis.set_tick_params(labelsize=16)
    ax[0,0].yaxis.set_tick_params(labelsize=16)

    ax[0,0].grid(b=None, which='major', axis= 'both', linestyle='-')
    ax[0,0].minorticks_on()
    ax[0,0].grid(b=None, which='minor', linestyle='--', axis="both", alpha=0.4)
    ax[0,0].set_xlim([1830, 2020]) # set x axis limit

    # G-E20C slp std
    os.chdir(dirStdSlp_e)
    dat = pd.read_csv(tg)
    ax[0,0].plot(dat['year'], dat['value'], color = "#0082c8", label = "slpSTD [G-E20C]", lw = 2)
    ax[0,0].legend()
    ax[0,0].set_ylabel("annual variability in Pa", fontsize = 18)

    ax[0,0].xaxis.set_tick_params(labelsize=16)
    ax[0,0].yaxis.set_tick_params(labelsize=16)

    ax[0,0].grid(b=None, which='major', axis= 'both', linestyle='-')
    ax[0,0].minorticks_on()
    ax[0,0].grid(b=None, which='minor', linestyle='--', axis="both", alpha=0.4)
    ax[0,0].set_xlim([1830, 2020]) # set x axis limit


    # G-20CR uwnd std
    os.chdir(dirStdUwnd_t)
    dat = pd.read_csv(tg)
    ax[0,1].plot(dat['year'], dat['value'], color = "#f58231", label = "uwndSTD [G-20CR]", lw = 2)
    ax[0,1].legend()
    ax[0,1].set_ylabel("annual variability in m/s", fontsize = 18)

    ax[0,1].xaxis.set_tick_params(labelsize=16)
    ax[0,1].yaxis.set_tick_params(labelsize=16)
    
    ax[0,1].minorticks_on()
    ax[0,1].grid(b=None, which='major', axis= 'both', linestyle='-')
    ax[0,1].grid(b=None, which='minor', linestyle='--', axis="both", alpha=0.4)
    ax[0,1].set_xlim([1830, 2020]) # set x axis limit


    # G-E20C uwnd std
    os.chdir(dirStdUwnd_e)
    dat = pd.read_csv(tg)
    ax[0,1].plot(dat['year'], dat['value'], color = "#911eb4", label = "uwndSTD [G-E20C]", lw = 2)
    ax[0,1].legend()
    ax[0,1].set_ylabel("annual variability in m/s", fontsize = 18)

    ax[0,1].xaxis.set_tick_params(labelsize=16)
    ax[0,1].yaxis.set_tick_params(labelsize=16)
    
    ax[0,1].minorticks_on()
    ax[0,1].grid(b=None, which='major', axis= 'both', linestyle='-')
    ax[0,1].grid(b=None, which='minor', linestyle='--', axis="both", alpha=0.4)
    ax[0,1].set_xlim([1830, 2020]) # set x axis limit


    # G-20CR vwnd std
    os.chdir(dirStdVwnd_t)
    dat = pd.read_csv(tg)
    ax[1,0].plot(dat['year'], dat['value'], color = "#800000", label = "vwndSTD [G-20CR]", lw = 2)
    ax[1,0].legend()
    ax[1,0].set_ylabel("annual variability in m/s", fontsize = 18)

    ax[1,0].xaxis.set_tick_params(labelsize=16)
    ax[1,0].yaxis.set_tick_params(labelsize=16)
    
    ax[1,0].grid(b=None, which='major', axis= 'both', linestyle='-')
    ax[1,0].minorticks_on()
    ax[1,0].grid(b=None, which='minor', linestyle='--', axis="both", alpha=0.4)
    ax[1,0].set_xlim([1830, 2020]) # set x axis limit

    # G-E20C vwnd std
    os.chdir(dirStdVwnd_e)
    dat = pd.read_csv(tg)
    ax[1,0].plot(dat['year'], dat['value'], color = "#000080", label = "vwndSTD [G-E20C]", lw = 2)
    ax[1,0].legend()
    ax[1,0].set_ylabel("annual variability in m/s", fontsize = 18)

    ax[1,0].xaxis.set_tick_params(labelsize=16)
    ax[1,0].yaxis.set_tick_params(labelsize=16)
    
    ax[1,0].grid(b=None, which='major', axis= 'both', linestyle='-')
    ax[1,0].minorticks_on()
    ax[1,0].grid(b=None, which='minor', linestyle='--', axis="both", alpha=0.4)
    ax[1,0].set_xlim([1830, 2020]) # set x axis limit

    
    # G-20CR std
    os.chdir(dirStdRecon_t)
    dat = pd.read_csv(tg)
    ax[1,1].plot(dat['year'], dat['value'], color = "green", label = "reconSTD [G-20CR]", lw = 2)
    ax[1,1].set_ylabel("annual variability in m", fontsize = 18)

    ax[1,1].xaxis.set_tick_params(labelsize=16)
    ax[1,1].yaxis.set_tick_params(labelsize=16)
    
    # ax[1,1].grid(b=None, which='major', axis= 'both', linestyle='-')
    # ax[1,1].minorticks_on()
    # ax[1,1].grid(b=None, which='minor', linestyle='--', axis="both", alpha=0.4)
    ax[1,1].set_xlim([1830, 2020]) # set x axis limit

    # G-E20C std
    os.chdir(dirStdRecon_e)
    dat = pd.read_csv(tg)
    ax[1,1].plot(dat['year'], dat['value'], color = "magenta", label = "reconSTD [G-E20C]", lw = 2)
    ax[1,1].set_ylabel("annual variability in m", fontsize = 18)

    ax[1,1].xaxis.set_tick_params(labelsize=16)
    ax[1,1].yaxis.set_tick_params(labelsize=16)
    
    # ax[1,1].grid(b=None, which='major', axis= 'both', linestyle='-')
    # ax[1,1].minorticks_on()
    # ax[1,1].grid(b=None, which='minor', linestyle='--', axis="both", alpha=0.4)
    ax[1,1].set_xlim([1830, 2020]) # set x axis limit


    # obsSurge std
    os.chdir(dirObsStd)
    dat = pd.read_csv(tg)
    ax[1,1].set_xlim([1830, 2020]) # set x axis limit
    ax[1,1].plot(dat['year'], dat['value'],  color = "blue", label = "obsSTD")
    ax[1,1].set_ylabel("annual variability in m", fontsize = 18)

    ax[1,1].xaxis.set_tick_params(labelsize=16)
    ax[1,1].yaxis.set_tick_params(labelsize=16)

    ax[1, 1].yaxis.set_major_formatter(mpl.ticker.FuncFormatter(fmt))
    
    # ax[1,1].grid(b=None, which='major', axis= 'both', linestyle='-')
    # ax[1,1].minorticks_on()
    # ax[1,1].grid(b=None, which='minor', linestyle='--', axis="both", alpha=0.4)
    ax[1,1].legend()

    ##################################
    # G-20CR change point probability 
    ##################################
    # slp bcp
    os.chdir(dirBcpSlp_t)
    dat = pd.read_csv(tg)
    ax[2,0].scatter(dat['year'], dat['prob'], s = 10,  color = "#e6194b", label = "slpBCP")
    ax[2,0].set_ylim([0,1])
    ax[2,0].set_ylabel("changepoint probability", fontsize = 18)

    ax[2,0].xaxis.set_tick_params(labelsize=16)
    ax[2,0].yaxis.set_tick_params(labelsize=16)
    
    # ax[2,0].grid(b=None, which='major', axis= 'both', linestyle='-')
    # ax[2,0].minorticks_on()
    # ax[2,0].grid(b=None, which='minor', linestyle='--', axis="both", alpha=0.4)
    ax[2,0].set_xlim([1830, 2020]) # set x axis limit



    # uwnd bcp
    os.chdir(dirBcpUwnd_t)
    dat = pd.read_csv(tg)
    ax[2,0].scatter(dat['year'], dat['prob'], s = 10, color = "#f58231", label = "uwndBCP")
    ax[2,0].set_ylim([0,1])
    ax[2,0].set_ylabel("changepoint probability", fontsize = 18)

    ax[2,0].xaxis.set_tick_params(labelsize=16)
    ax[2,0].yaxis.set_tick_params(labelsize=16)
    


    # vwnd bcp
    os.chdir(dirBcpVwnd_t)
    dat = pd.read_csv(tg)
    ax[2,0].scatter(dat['year'], dat['prob'], s = 10,  color = "#800000", label = "vwndBCP")
    ax[2,0].set_ylim([0,1])
    ax[2,0].set_ylabel("changepoint probability", fontsize = 18)

    ax[2,0].xaxis.set_tick_params(labelsize=16)
    ax[2,0].yaxis.set_tick_params(labelsize=16)
    


    # recon bcp
    os.chdir(dirBcpRecon_t)
    dat = pd.read_csv(tg)
    ax[2,0].scatter(dat['year'], dat['prob'], s = 10, color = "green", label = "reconBCP")
    ax[2,0].set_ylim([0,1])
    ax[2,0].set_ylabel("changepoint probability", fontsize = 18)

    ax[2,0].xaxis.set_tick_params(labelsize=16)
    ax[2,0].yaxis.set_tick_params(labelsize=16)
    

    
    # recon cpt from cptSA
    os.chdir(dirCptSA_t)
    dat = pd.read_csv("twcrCptSA.csv")
    cpt_30_t = dat[dat['tg'] == tg]['p_30'].values[0]
    cpt_25_t = dat[dat['tg'] == tg]['p_25'].values[0]
    cpt_20_t = dat[dat['tg'] == tg]['p_20'].values[0]
    cpt_15_t = dat[dat['tg'] == tg]['p_15'].values[0]

    # twcr avg bcp
    os.chdir(dirAvgCpt_t)
    dat = pd.read_csv(tg)
    dat['p_avg'] = dat.iloc[:,2:6].mean(axis = 1)
    
    # changepoints
    ax[2,0].axvline(x = cpt_30_t, color = "black", ls = "--", 
        lw = 2.0, label = "30%: {}".format(cpt_30_t))
    ax[2,0].axvline(x = cpt_25_t, color = "dimgrey", ls = "--", 
        lw = 2.0, label = "25%: {}".format(cpt_25_t))
    ax[2,0].axvline(x = cpt_20_t, color = "darkgrey", ls = "--", 
        lw = 2.0, label = "20%: {}".format(cpt_20_t))
    ax[2,0].axvline(x = cpt_15_t, color = "silver", ls = "--", 
        lw = 2.0, label = "15%: {}".format(cpt_15_t))

    ax[2,0].plot(dat['year'], dat['p_avg'], lw = 2, color = "black", label = "average BCP")
    ax[2,0].legend(ncol = 2)


    ##################################
    # G-E20C change point probability 
    ##################################

    # slp bcp
    os.chdir(dirBcpSlp_e)
    dat = pd.read_csv(tg)
    ax[2,1].scatter(dat['year'], dat['prob'], s = 10,  color = "#0082c8", label = "slpBCP")
    ax[2,1].set_ylim([0,1])
    ax[2,1].set_ylabel("changepoint probability", fontsize = 18)

    ax[2,1].xaxis.set_tick_params(labelsize=16)
    ax[2,1].yaxis.set_tick_params(labelsize=16)

    # ax[2,1].grid(b=None, which='major', axis= 'both', linestyle='-')
    # ax[2,1].minorticks_on()
    # ax[2,1].grid(b=None, which='minor', linestyle='--', axis="both", alpha=0.4)
    ax[2,1].set_xlim([1830, 2020]) # set x axis limit

    # uwnd bcp
    os.chdir(dirBcpUwnd_e)
    dat = pd.read_csv(tg)
    ax[2,1].scatter(dat['year'], dat['prob'], s = 10, color = "#911eb4", label = "uwndBCP")
    ax[2,1].set_ylim([0,1])
    ax[2,1].set_ylabel("changepoint probability", fontsize = 18)

    ax[2,1].xaxis.set_tick_params(labelsize=16)
    ax[2,1].yaxis.set_tick_params(labelsize=16)



    # vwnd bcp
    os.chdir(dirBcpVwnd_e)
    dat = pd.read_csv(tg)
    ax[2,1].scatter(dat['year'], dat['prob'], s = 10,  color = "#000080", label = "vwndBCP")
    ax[2,1].set_ylim([0,1])
    ax[2,1].set_ylabel("changepoint probability", fontsize = 18)

    ax[2,1].xaxis.set_tick_params(labelsize=16)
    ax[2,1].yaxis.set_tick_params(labelsize=16)



    # recon bcp
    os.chdir(dirBcpRecon_e)
    dat = pd.read_csv(tg)
    ax[2,1].scatter(dat['year'], dat['prob'], s = 10, color = "magenta", label = "reconBCP")
    ax[2,1].set_ylim([0,1])
    ax[2,1].set_ylabel("changepoint probability", fontsize = 18)

    ax[2,1].xaxis.set_tick_params(labelsize=16)
    ax[2,1].yaxis.set_tick_params(labelsize=16)


    # G-E20C recon cpt from cptSA
    os.chdir(dirCptSA_e)
    dat = pd.read_csv("era20cCptSA.csv")
    cpt_30_e = dat[dat['tg'] == tg]['p_30'].values[0]
    cpt_25_e = dat[dat['tg'] == tg]['p_25'].values[0]
    cpt_20_e = dat[dat['tg'] == tg]['p_20'].values[0]
    cpt_15_e = dat[dat['tg'] == tg]['p_15'].values[0]

    # G-20CR avg bcp
    os.chdir(dirAvgCpt_e)
    dat = pd.read_csv(tg)
    dat['p_avg'] = dat.iloc[:,2:6].mean(axis = 1)
    
    # changepoints
    ax[2,1].axvline(x = cpt_30_e, color = "black", ls = "--", 
        lw = 2.0, label = "30%: {}".format(cpt_30_e))
    ax[2,1].axvline(x = cpt_25_e, color = "dimgrey", ls = "--", 
        lw = 2.0, label = "25%: {}".format(cpt_25_e))
    ax[2,1].axvline(x = cpt_20_e, color = "darkgrey", ls = "--", 
        lw = 2.0, label = "20%: {}".format(cpt_20_e))
    ax[2,1].axvline(x = cpt_15_e, color = "silver", ls = "--", 
        lw = 2.0, label = "15%: {}".format(cpt_15_e))

    ax[2,1].plot(dat['year'], dat['p_avg'], lw = 2, color = "black", label = "average BCP")
    ax[2,1].legend(ncol = 2)

    os.chdir(dirOut)
    plt.savefig("fig1_all.svg", dpi = 400)
    plt.show()


# plot single tg result
plotSTD_CPT('astoria,or_572a_usa.csv')