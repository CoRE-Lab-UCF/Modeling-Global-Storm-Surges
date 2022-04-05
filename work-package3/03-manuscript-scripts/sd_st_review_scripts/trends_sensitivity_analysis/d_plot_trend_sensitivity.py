"""
Created on Sun Dec 19 14:34:00 2021
Modified on Wed Jan 12 15:43:00 2022

plot trend sensitivity analysis  

@author: Michael Tadesse

"""

import os 
import numpy as np
import pandas as pd
from matplotlib import colors
import matplotlib.pyplot as plt
import seaborn as sns
from datetime import datetime
import statsmodels.stats.stattools as stools
import statsmodels.api as sm



dir_home = "G:\\report\\year-3\\07-Fall-2020\\#3Paper\\data"\
            "\\trend-analysis\\data\\chosen_tgs_sensitivity\\trends"
dir_out = "G:\\report\\year-3\\07-Fall-2020\\#3Paper\\"\
            "p28ThirdManuscript\\manuscript\\figures\\"\
                    "additional-analysis\\trend_sensitivity\\p_001_v2"



def getData(tg, data):
    """  
    plot the trend sensitivity analysis
    with a heatmap

    data = [ 'obs', 'twcr', 'era20c' ]

    """

    os.chdir(dir_home)

    # read file
    dat = pd.read_csv(tg + data + '.csv')


    # remove the .0 part 
    styling = lambda x: int(x)
    dat['year'] = pd.DataFrame(list(map(styling, dat['year'])))
    dat['window'] = pd.DataFrame(list(map(styling, dat['window'])))


    trend = dat.pivot(index = 'year', columns = 'window', values = 'trend').transpose()

    ########
    # pvalue
    ########

    getSignificance = lambda x: '*' if x <= 0.05 else '' 
    getEmpty = lambda x: "" if not np.isnan(x) else " " 

    dat['signif'] = pd.DataFrame(list(map(getSignificance, dat['pval'])))

    # create a dataframe with the length of dat
    # this will be a layeyer behind the real trend layer 
    # this is used to show where data are missing 

    dat_dummy = pd.DataFrame(np.ones(len(dat)))
    dat_dummy.columns = ['dummy']
    dat_dummy['year'] = dat['year']
    dat_dummy['window'] = dat['window']

    
    dat_dummy['available'] = pd.DataFrame(list(map(getEmpty, dat_dummy['dummy'])))


    print(dat_dummy)

    pval = dat.pivot(index = 'year', columns = 'window', values = 'signif').transpose()
    
    
    dummy = dat_dummy.pivot(index = 'year', columns = 'window', values = 'dummy').transpose()
    dat_nan = dat_dummy.pivot(index = 'year', columns = 'window', values = 'available').transpose()
    

    print(dat_nan)

    return trend, pval, dummy, dat_nan




def plotIt(tg):
    """  
    plot heatmap for obs, twcr, and era20c for
    a given tide gauge
    """
    sns.set_context('paper', font_scale = 1.75)
    fig, (ax1, ax2, ax3, axcb) = plt.subplots(1, 4, figsize=(20, 12),
            gridspec_kw={'width_ratios':[1,1,1,0.08]})
    # fig.tight_layout(pad = 0.75)

    data = { 'obs':[ax1, False, ''], 'twcr':[ax2, False, ''], 'era20c':[ax3, True, axcb] } 

    for d in data.keys():
        print(d)
        trend, pval, dummy, dat_nan = getData(tg, d)

        # print(dat_nan)

        # color map
        cmap = sns.diverging_palette(250, 15, s=80, l=55, n=50) 

        # # plot heatmap     
        # underlying "no data" layer                       
        g = sns.heatmap(dummy, cmap = "binary", yticklabels = 5, xticklabels = 7,
                vmin = -6, vmax = 6, annot = dat_nan, fmt = "s",  
                        annot_kws={"size": 10,}, cbar=data[d][1], 
                            cbar_ax = data[d][2], ax=data[d][0])

        # main trend heat map layer
        g = sns.heatmap(trend, cmap = "seismic", yticklabels = 5, xticklabels = 7,
                vmin = -6, vmax = 6, annot = pval, fmt = "",  
                        annot_kws={"size": 10,}, cbar=data[d][1], 
                            cbar_ax = data[d][2], ax=data[d][0])

        g.set_ylabel('')
        g.invert_yaxis()
        g.set_xlabel('')
        g.set_title(d)


    ax1.set_ylabel('Number of years for trend fitting')
    plt.suptitle('{} Trends in mm/year'.format(tg))

    # save plot
    os.chdir(dir_out)
    plt.savefig(tg+".svg", dpi = 400)
    plt.savefig(tg+".png", dpi = 400)
    # plt.show()


# run code
os.chdir("G:\\report\\year-3\\07-Fall-2020\\#3Paper\\data"\
    "\\trend-analysis\\data\\chosen_tgs_sensitivity\\percentiles\\99")
tg_list = os.listdir()


for tg in tg_list:
    tg_name = tg.split(".csv")[0]
    plotIt(tg_name)