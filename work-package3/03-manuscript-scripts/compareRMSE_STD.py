"""
Created on Mon Jan 10 10:32:00 2022

To compare and contrast RMSE and STD time series 
for changepoint detection methods

@author: Michael Getachew Tadesse

"""

import os 
import math 
import pandas as pd 
import matplotlib as mpl
import matplotlib.pyplot as plt
import seaborn as sns

dir_home = "G:\\report\\year-3\\07-Fall-2020\\#3Paper\\data\\"\
                "changePointTimeSeries\\additionalTest\\rmse_vs_std\\rmse"


def plotIt():
    """ 
    plots the rmse and bcp time series
    for the selected tide gauge
    """

    os.chdir(dir_home)

    # plotting
    fig, ax = plt.subplots(4, 2, figsize=(14, 14))
    fig.tight_layout(pad = 3.0)
    sns.set_context('paper', font_scale = 2.0)

    # format axis decimal places
    fmt = lambda x, pos: '{}'.format(math.ceil((x)*100.0)/100.0, pos)

    # tide gauges
    tg_list = [ ["brest", "era20c"], ["cuxhaven", "era20c"], 
                    ["fremantle", "twcr"], ["seattle", "twcr"] ]


    # panel counter
    panel = 0

    for tg in tg_list:


        rmse = pd.read_csv(tg[0]+"_rmse_"+tg[1]+".csv")
        std = pd.read_csv(tg[0]+"_std_"+tg[1]+".csv")
        rmse_bcp = pd.read_csv(tg[0]+"_rmse_bcp_"+tg[1]+".csv")
        std_bcp = pd.read_csv(tg[0]+"_std_bcp_"+tg[1]+".csv")

        # find starting year + ending year
        start_year = max(rmse['year'][0], std['year'][0])
        end_year = min(rmse['year'][len(rmse) - 1], std['year'][len(std) -1])

        # subset data
        rmse = rmse[ (rmse['year'] >= start_year) & (rmse['year'] <= end_year) ]
        std = std[ (std['year'] >= start_year) & (std['year'] <= end_year) ]
        rmse_bcp = rmse_bcp[ (rmse_bcp['year'] >= start_year) & (rmse_bcp['year'] <= end_year) ]
        std_bcp = std_bcp[ (std_bcp['year'] >= start_year) & (std_bcp['year'] <= end_year) ]


        # plotting

        ax[panel, 0].plot(rmse['year'], rmse['value'], color = "#00994C", label = "rmse", lw = 2)
        ax[panel, 0].plot(std['year'], std['value'], color = "#CC6600", label = "std", lw = 2)
        
        ax[panel, 0].legend()
        ax[panel, 0].set_ylabel("Value in meters", fontsize = 18)

        ax[panel, 0].xaxis.set_tick_params(labelsize=16)
        ax[panel, 0].yaxis.set_tick_params(labelsize=16)

        ax[panel, 0].grid(b=None, which='major', axis= 'both', linestyle='-')
        ax[panel, 0].minorticks_on()
        ax[panel, 0].grid(b=None, which='minor', linestyle='--', axis="both", alpha=0.4)

        ax[panel, 0].yaxis.set_major_formatter(mpl.ticker.FuncFormatter(fmt))

        # ax[0,0].set_xlim([1830, 2020]) # set x axis limit


        ax[panel, 1].plot(std_bcp['year'], std_bcp['prob'], color = "#CC6600", label = "std-bcp", lw = 2)
        ax[panel, 1].plot(rmse_bcp['year'], rmse_bcp['prob'], color = "#00994C", label = "rmse-bcp", lw = 2)
        
        ax[panel, 1].legend()
        ax[panel, 1].set_ylabel("Change Point Probability", fontsize = 18)

        ax[panel, 1].xaxis.set_tick_params(labelsize=16)
        ax[panel, 1].yaxis.set_tick_params(labelsize=16)
        ax[panel, 1].set_ylim(0, 1)

        ax[panel, 1].grid(b=None, which='major', axis= 'both', linestyle='-')
        ax[panel, 1].minorticks_on()
        ax[panel, 1].grid(b=None, which='minor', linestyle='--', axis="both", alpha=0.4)

        panel +=1

    plt.savefig("rmse_vs_std.svg", dpi=400)
    plt.show()



plotIt()