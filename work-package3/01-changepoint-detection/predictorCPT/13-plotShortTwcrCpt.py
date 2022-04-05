"""
Modified on Fri Oct 01 06:53:00 2021

this script plots predictor and Recon STDs and the four BCPs with their average 
for twcr (1900-2010) and era20c

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

# era20c std directories
dirStdSlpEra20c = "G:\\report\\year-3\\07-Fall-2020\\#3Paper\\data\\changePointTimeSeries\\"\
    "mamun-cpt-approach\\era20c\\0001-predCPT\\slp\\annualSTD"
dirStdUwndEra20c = "G:\\report\\year-3\\07-Fall-2020\\#3Paper\\data\\changePointTimeSeries\\"\
    "mamun-cpt-approach\\era20c\\0001-predCPT\\wnd_u\\annualSTD"
dirStdVwndEra20c = "G:\\report\\year-3\\07-Fall-2020\\#3Paper\\data\\changePointTimeSeries\\"\
    "mamun-cpt-approach\\era20c\\0001-predCPT\\wnd_v\\annualSTD"
dirStdReconEra20c = "G:\\report\\year-3\\07-Fall-2020\\#3Paper\\data\\changePointTimeSeries\\"\
    "era20cSTD"

# short twcr std directories
dirStdSlpTwcr = "G:\\report\\year-3\\07-Fall-2020\\#3Paper\\data\\changePointTimeSeries\\"\
    "mamun-cpt-approach\\shortTwcr\\slp"
dirStdUwndTwcr = "G:\\report\\year-3\\07-Fall-2020\\#3Paper\\data\\changePointTimeSeries\\"\
    "mamun-cpt-approach\\shortTwcr\\wnd_u"
dirStdVwndTwcr = "G:\\report\\year-3\\07-Fall-2020\\#3Paper\\data\\changePointTimeSeries\\"\
    "mamun-cpt-approach\\shortTwcr\\wnd_v"
dirStdReconTwcr = "G:\\report\\year-3\\07-Fall-2020\\#3Paper\\data\\changePointTimeSeries\\"\
    "mamun-cpt-approach\\shortTwcr\\recon"

# obs suurge std 
dirStdObs = "G:\\report\\year-3\\07-Fall-2020\\#3Paper\\data\\changePointTimeSeries\\"\
    "mamun-cpt-approach\\obsSurge\\01-annualSTD"


# era20c cpt directories
dirBcpSlpEra20c = "G:\\report\\year-3\\07-Fall-2020\\#3Paper\\data\\changePointTimeSeries\\"\
    "mamun-cpt-approach\\era20c\\0001-predCPT\\slp\\originalBCP"
dirBcpUwndEra20c = "G:\\report\\year-3\\07-Fall-2020\\#3Paper\\data\\changePointTimeSeries\\"\
    "mamun-cpt-approach\\era20c\\0001-predCPT\\wnd_u\\originalBCP"
dirBcpVwndEra20c = "G:\\report\\year-3\\07-Fall-2020\\#3Paper\\data\\changePointTimeSeries\\"\
    "mamun-cpt-approach\\era20c\\0001-predCPT\\wnd_v\\originalBCP"
dirBcpReconEra20c = "G:\\report\\year-3\\07-Fall-2020\\#3Paper\\data\\changePointTimeSeries\\"\
    "era20cBCP"

# short twcr cpt directories
dirBcpSlpTwcr = "G:\\report\\year-3\\07-Fall-2020\\#3Paper\\data\\changePointTimeSeries\\"\
    "mamun-cpt-approach\\shortTwcr\\slpBcp"
dirBcpUwndTwcr = "G:\\report\\year-3\\07-Fall-2020\\#3Paper\\data\\changePointTimeSeries\\"\
    "mamun-cpt-approach\\shortTwcr\\wnduBcp"
dirBcpVwndTwcr = "G:\\report\\year-3\\07-Fall-2020\\#3Paper\\data\\changePointTimeSeries\\"\
    "mamun-cpt-approach\\shortTwcr\\wndvBcp"
dirBcpReconTwcr = "G:\\report\\year-3\\07-Fall-2020\\#3Paper\\data\\changePointTimeSeries\\"\
    "mamun-cpt-approach\\shortTwcr\\reconBcp"

# observed and recon surges

# era20c reconstruction
dirReconEra20c = "G:\\data\\allReconstructions\\02_era20c"
dirReconTwcr = "G:\\data\\allReconstructions\\01_20cr"
dirObs = "G:\\data\\allReconstructions\\06_dmax_surge_georef"


# merged cptSA file
dirCptSA = "G:\\report\\year-3\\07-Fall-2020\\#3Paper\\data\\changePointTimeSeries\\"\
    "mamun-cpt-approach\\twcr_era20c_1900_2010"

# era20c avg cpt
dirAvgCptEra20c = "G:\\report\\year-3\\07-Fall-2020\\#3Paper\\data\\changePointTimeSeries\\"\
    "mamun-cpt-approach\\era20c\\0001-predCPT\\combinedBCP"

dirAvgCptTwcr = "G:\\report\\year-3\\07-Fall-2020\\#3Paper\\data\\changePointTimeSeries\\"\
    "mamun-cpt-approach\\shortTwcr\\01-combinedBCP"

# image saving dir
dirOut = "G:\\report\\year-3\\07-Fall-2020\\#3Paper\\data\\changePointTimeSeries\\"\
    "mamun-cpt-approach\\twcr_era20c_cptPlots_v2"


def plotSTD_CPT(tg):

    print(tg)
    
    fig, ax = plt.subplots(3, 2, figsize=(20, 12))

    sns.set_context('paper', font_scale = 1.5)

    fig.tight_layout(pad = 3.0)

    # fig.delaxes(ax[2,1]) # use when using odd number of panes

    ## slp ##
    # era20c slp std
    os.chdir(dirStdSlpEra20c)
    dat = pd.read_csv(tg)
    ax[0,0].plot(dat['year'], dat['value'], color = "blue", label = "slpSTD-Era20C", lw = 2)
    ax[0,0].legend()
    ax[0,0].set_ylabel("annual variability in Pa", fontsize=16)

    ax[0,0].xaxis.set_tick_params(labelsize=16)
    ax[0,0].yaxis.set_tick_params(labelsize=16)

    ax[0,0].grid(b=None, which='major', axis= 'both', linestyle='-')
    # ax[0,0].minorticks_on()
    # ax[0,0].grid(b=None, which='minor', linestyle='--', axis="both", alpha=0.4)
    ax[0,0].set_xlim([1895, 2015]) # set x axis limit

    # twcr slp std
    os.chdir(dirStdSlpTwcr)
    dat = pd.read_csv(tg)
    ax[0,0].plot(dat['year'], dat['value'], color = "red", label = "slpSTD-Twcr", lw = 2)
    ax[0,0].legend()
    ax[0,0].set_ylabel("annual variability in Pa", fontsize=16)


    ax[0,0].xaxis.set_tick_params(labelsize=16)
    ax[0,0].yaxis.set_tick_params(labelsize=16)

    ax[0,0].grid(b=None, which='major', axis= 'both', linestyle='-')
    ax[0,0].minorticks_on()
    ax[0,0].grid(b=None, which='minor', linestyle='--', axis="both", alpha=0.4)
    ax[0,0].set_xlim([1895, 2015]) # set x axis limit

    ## wnd_u ##
    # era20c wnd_u std
    os.chdir(dirStdUwndEra20c)
    dat = pd.read_csv(tg)
    ax[0,1].plot(dat['year'], dat['value'], color = "green", label = "uwndSTD-Era20C", lw = 2)
    ax[0,1].legend()
    ax[0,1].set_ylabel("annual variability in m/s", fontsize=16)


    ax[0,1].xaxis.set_tick_params(labelsize=16)
    ax[0,1].yaxis.set_tick_params(labelsize=16)

    ax[0,1].grid(b=None, which='major', axis= 'both', linestyle='-')
    # ax[0,0].minorticks_on()
    # ax[0,0].grid(b=None, which='minor', linestyle='--', axis="both", alpha=0.4)
    ax[0,1].set_xlim([1895, 2015]) # set x axis limit

    # twcr wnd_u std
    os.chdir(dirStdUwndTwcr)
    dat = pd.read_csv(tg)
    ax[0,1].plot(dat['year'], dat['value'], color = "darkorange", label = "uwndSTD-Twcr", lw = 2)
    ax[0,1].legend()
    ax[0,1].set_ylabel("annual variability in m/s", fontsize=16)


    ax[0,1].xaxis.set_tick_params(labelsize=16)
    ax[0,1].yaxis.set_tick_params(labelsize=16)

    ax[0,1].grid(b=None, which='major', axis= 'both', linestyle='-')
    ax[0,1].minorticks_on()
    ax[0,1].grid(b=None, which='minor', linestyle='--', axis="both", alpha=0.4)
    ax[0,1].set_xlim([1895, 2015]) # set x axis limit

    ## wnd_v ##
    # era20c wnd_v std
    os.chdir(dirStdVwndEra20c)
    dat = pd.read_csv(tg)
    ax[1,0].plot(dat['year'], dat['value'], color = "magenta", label = "vwndSTD-Era20C", lw = 2)
    ax[1,0].legend()
    ax[1,0].set_ylabel("annual variability in m/s", fontsize=16)


    ax[1,0].xaxis.set_tick_params(labelsize=16)
    ax[1,0].yaxis.set_tick_params(labelsize=16)

    ax[1,0].grid(b=None, which='major', axis= 'both', linestyle='-')
    # ax[0,0].minorticks_on()
    # ax[0,0].grid(b=None, which='minor', linestyle='--', axis="both", alpha=0.4)
    ax[0,1].set_xlim([1895, 2015]) # set x axis limit

    # twcr wnd_v std
    os.chdir(dirStdVwndTwcr)
    dat = pd.read_csv(tg)
    ax[1,0].plot(dat['year'], dat['value'], color = "darkolivegreen", label = "vwndSTD-Twcr", lw = 2)
    ax[1,0].legend()
    ax[1,0].set_ylabel("annual variability in m/s", fontsize=16)


    ax[1,0].xaxis.set_tick_params(labelsize=16)
    ax[1,0].yaxis.set_tick_params(labelsize=16)

    ax[1,0].grid(b=None, which='major', axis= 'both', linestyle='-')
    ax[1,0].minorticks_on()
    ax[1,0].grid(b=None, which='minor', linestyle='--', axis="both", alpha=0.4)
    ax[1,0].set_xlim([1895, 2015]) # set x axis limit

    ## recon ##
    # era20c recon std
    os.chdir(dirStdReconEra20c)
    dat = pd.read_csv(tg)
    ax[1,1].plot(dat['year'], dat['value'], color = "brown", label = "reconSTD-Era20C", lw = 2)
    ax[1,1].legend()
    ax[1,1].set_ylabel("annual variability in m")


    ax[1,1].xaxis.set_tick_params(labelsize=16)
    ax[1,1].yaxis.set_tick_params(labelsize=16)

    ax[1,1].grid(b=None, which='major', axis= 'both', linestyle='-')
    # ax[0,0].minorticks_on()
    # ax[0,0].grid(b=None, which='minor', linestyle='--', axis="both", alpha=0.4)
    ax[0,1].set_xlim([1895, 2015]) # set x axis limit

    # twcr recon std
    os.chdir(dirStdReconTwcr)
    dat = pd.read_csv(tg)
    ax[1,1].plot(dat['year'], dat['value'], color = "slateblue", label = "reconSTD-Twcr", lw = 2)
    ax[1,1].legend()
    ax[1,1].set_ylabel("annual variability in m", fontsize=16)


    ax[1,1].xaxis.set_tick_params(labelsize=16)
    ax[1,1].yaxis.set_tick_params(labelsize=16)

    ax[1,1].grid(b=None, which='major', axis= 'both', linestyle='-')
    ax[1,1].minorticks_on()
    ax[1,1].grid(b=None, which='minor', linestyle='--', axis="both", alpha=0.4)
    ax[1,1].set_xlim([1895, 2015]) # set x axis limit


    # obs surge std
    os.chdir(dirStdObs)
    dat = pd.read_csv(tg)
    ax[1,1].scatter(dat['year'], dat['value'], color = "blue", label = "obsSTD", lw = 1)
    ax[1,1].legend()
    ax[1,1].set_ylabel("annual variability in m")


    ax[1,1].xaxis.set_tick_params(labelsize=16)
    ax[1,1].yaxis.set_tick_params(labelsize=16)

    ax[1,1].grid(b=None, which='major', axis= 'both', linestyle='-')
    ax[1,1].minorticks_on()
    ax[1,1].grid(b=None, which='minor', linestyle='--', axis="both", alpha=0.4)
    ax[1,1].set_xlim([1895, 2015]) # set x axis limit

   
    # predictor+recon average cpt from cptSA
    os.chdir(dirCptSA)
    dat = pd.read_csv("cptSAComparison.csv")
        
    cpt_30E = dat[dat['tg'] == tg]['p_30E'].values[0]
    cpt_25E = dat[dat['tg'] == tg]['p_25E'].values[0]
    cpt_20E = dat[dat['tg'] == tg]['p_20E'].values[0]
    cpt_15E = dat[dat['tg'] == tg]['p_15E'].values[0]

    cpt_30T = dat[dat['tg'] == tg]['p_30T'].values[0]
    cpt_25T = dat[dat['tg'] == tg]['p_25T'].values[0]
    cpt_20T = dat[dat['tg'] == tg]['p_20T'].values[0]
    cpt_15T = dat[dat['tg'] == tg]['p_15T'].values[0]


    # changepoints
    ax[1,1].axvline(x = cpt_30E, color = "black", ls = "--", 
        lw = 2.2, label = "Era20C-30%: {}".format(cpt_30E))
    # ax[1,1].axvline(x = cpt_25E, color = "dimgrey", ls = "--", 
    #     lw = 1.9, label = "Era20C-25%: {}".format(cpt_25E))
    ax[1,1].axvline(x = cpt_20E, color = "darkgrey", ls = "--", 
        lw = 1.75, label = "Era20C-20%: {}".format(cpt_20E))
    # ax[1,1].axvline(x = cpt_15E, color = "silver", ls = "--", 
    #     lw = 1.5, label = "Era20C-15%: {}".format(cpt_15E))
    
    ax[1,1].axvline(x = cpt_30T, color = "red", ls = "-.", 
        lw = 2.2, label = "Twcr-30%: {}".format(cpt_30T))
    # ax[1,1].axvline(x = cpt_25T, color = "seagreen", ls = "-.", 
    #     lw = 1.9, label = "Twcr-25%: {}".format(cpt_25T))
    ax[1,1].axvline(x = cpt_20T, color = "lightcoral", ls = "-.", 
        lw = 1.75, label = "Twcr-20%: {}".format(cpt_20T))
    # ax[1,1].axvline(x = cpt_15T, color = "lightgreen", ls = "-.", 
    #     lw = 1.5, label = "Twcr-15%: {}".format(cpt_15T))

    ax[1,1].legend()


    # era20c avg bcp
    os.chdir(dirAvgCptEra20c)
    era20cAvg = pd.read_csv(tg)
    era20cAvg['p_avg'] = era20cAvg.iloc[:,2:6].mean(axis = 1)

    # twcr avg bcp
    os.chdir(dirAvgCptTwcr)
    twcrAvg = pd.read_csv(tg)
    twcrAvg['p_avg'] = twcrAvg.iloc[:,2:6].mean(axis = 1)


    # era20c changepoints
    ax[2,0].axvline(x = cpt_30E, color = "black", ls = "--", 
        lw = 2.2, label = "Era20C-30%: {}".format(cpt_30E))
    # ax[2,0].axvline(x = cpt_25E, color = "dimgrey", ls = "--", 
    #     lw = 1.9, label = "Era20C-25%: {}".format(cpt_25E))
    ax[2,0].axvline(x = cpt_20E, color = "darkgrey", ls = "--", 
        lw = 1.75, label = "Era20C-20%: {}".format(cpt_20E))
    # ax[2,0].axvline(x = cpt_15E, color = "silver", ls = "--", 
    #     lw = 1.5, label = "Era20C-15%: {}".format(cpt_15E))
    
    ax[2,0].axvline(x = cpt_30T, color = "red", ls = "-.", 
        lw = 2.2, label = "Twcr-30%: {}".format(cpt_30T))
    # ax[2,0].axvline(x = cpt_25T, color = "seagreen", ls = "-.", 
    #     lw = 1.9, label = "Twcr-25%: {}".format(cpt_25T))
    ax[2,0].axvline(x = cpt_20T, color = "lightcoral", ls = "-.", 
        lw = 1.75, label = "Twcr-20%: {}".format(cpt_20T))
    # ax[2,0].axvline(x = cpt_15T, color = "lightgreen", ls = "-.", 
    #     lw = 1.5, label = "Twcr-15%: {}".format(cpt_15T))



    ax[2,0].scatter(era20cAvg['year'], era20cAvg['p_avg'], lw = 1, \
        color = "#1B4F72", label = "Era20C-average BCP")
    ax[2,0].scatter(twcrAvg['year'], twcrAvg['p_avg'], lw = 1, \
        color = "#00FF00", label = "Twcr-average BCP")
    ax[2,0].set_ylim([0,1])
    ax[2,0].set_ylabel("changepoint probability", fontsize=16)


    ax[2,0].xaxis.set_tick_params(labelsize=16)
    ax[2,0].yaxis.set_tick_params(labelsize=16)

    
    ax[2,0].grid(b=None, which='major', axis= 'both', linestyle='-')
    ax[2,0].minorticks_on()
    ax[2,0].grid(b=None, which='minor', linestyle='--', axis="both", alpha=0.4)
    ax[2,0].set_xlim([1895, 2015]) # set x axis limit

    ax[2,0].legend()


    #define lambda functions 
    time_stamp1 = lambda x: (datetime.strptime(x, '%Y-%m-%d %H:%M:%S'))
    time_stamp2 = lambda x: (datetime.strptime(x, '%Y-%m-%d'))
    getYear = lambda x: x.year
    # adding observed + recon surges
    
    # adding obs surge
    os.chdir(dirObs)
    dat = pd.read_csv(tg)
    dat['date'] = pd.DataFrame(list(map(time_stamp2, dat['ymd'])), 
                                          columns = ['date'])
    dat['year'] = pd.DataFrame(list(map(getYear, dat['date'])), 
                                          columns = ['year'])
    dat = dat[(dat['year'] >= 1900) & (dat['year'] <= 2010)]


    ax[2,1].plot(dat['date'], dat['surge'], color = "blue", \
        label = "Observation", lw = 2)

    # adding era20c surge
    os.chdir(dirReconEra20c)
    dat = pd.read_csv(tg)
    dat['date'] = pd.DataFrame(list(map(time_stamp1, dat['date'])), 
                                          columns = ['date'])
    dat['year'] = pd.DataFrame(list(map(getYear, dat['date'])), 
                                          columns = ['year'])
    dat = dat[(dat['year'] >= 1900) & (dat['year'] <= 2010)]
    

    ax[2,1].plot(dat['date'], dat['surge_reconsturcted'], color = "magenta", \
        label = "Era20C-Reconstruction", lw = 2)
    
    # adding twcr surge
    os.chdir(dirReconTwcr)
    dat = pd.read_csv(tg)
    dat['date'] = pd.DataFrame(list(map(time_stamp1, dat['date'])), 
                                          columns = ['date'])
    dat['year'] = pd.DataFrame(list(map(getYear, dat['date'])), 
                                          columns = ['year'])
    dat = dat[(dat['year'] >= 1900) & (dat['year'] <= 2010)]


    # axis properties
    ax[2,1].plot(dat['date'], dat['surge_reconsturcted'], color = "green", \
        label = "Twcr-Reconstruction", lw = 2)
    
    ax[2,1].set_ylabel("surge height (m)", fontsize=16)


    ax[2,1].xaxis.set_tick_params(labelsize=16)
    ax[2,1].yaxis.set_tick_params(labelsize=16)

    
    ax[2,1].grid(b=None, which='major', axis= 'both', linestyle='-')
    ax[2,1].minorticks_on()
    ax[2,1].grid(b=None, which='minor', linestyle='--', axis="both", alpha=0.4)
    # ax[2,1].set_xlim([1895, 2015]) # set x axis limit
    
    ax[2,1].legend()





    # plt.suptitle(tg.split('.csv')[0], y = 0.9999999, fontweight="bold")
   
   
    # save image
    os.chdir(dirOut)
    # plt.savefig(tg.split('.csv')[0]+".jpg", dpi=400)

    plt.show()



############################################
# # loop through twcr tgs

# os.chdir(dirCptSA)
# dat = pd.read_csv("cptSAComparison.csv")

# # print(dat)

# for tg in dat['tg']:
#     plotSTD_CPT(tg)
############################################

tg = "astoria,or_572a_usa.csv"
plotSTD_CPT(tg)