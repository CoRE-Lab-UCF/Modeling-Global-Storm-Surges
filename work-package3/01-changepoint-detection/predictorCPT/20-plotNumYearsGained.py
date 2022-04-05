"""  
this script plots the number of years of data gained
from the reconstructions 
"""

import os
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from mpl_toolkits.axes_grid.inset_locator import inset_axes
#locate the file that basemap needs
os.environ["PROJ_LIB"] = "C:\\Users\\WahlInstall\\"\
    "Anaconda3\\Library\\share\\basemap"
from mpl_toolkits.basemap import Basemap


# get data 
dirDict = {
    "twcr":"G:\\report\\year-3\\07-Fall-2020\\#3Paper\\data\\"\
            "changePointTimeSeries\\mamun-cpt-approach\\twcr\\0001-predCPT\\cptSA",
    "era20c":"G:\\report\\year-3\\07-Fall-2020\\#3Paper\\data\\"\
            "changePointTimeSeries\\mamun-cpt-approach\\era20c\\0001-predCPT\\cptSA"
}


def plotIt(recon):
    """  
    this function plots the numYearsGained
    """
    os.chdir(dirDict[recon])

    dat = pd.read_csv(recon + "RecordLengthComparison.csv") 

    dat['yrGainedSign'] = 'nan' # {r1, r2, r3, r4, r5}


    for ii in range(len(dat)):
        
        print(dat['tg'][ii])

        if dat['numYearsGained'][ii] <= -30:
            dat['yrGainedSign'][ii] = "(-60)-(-30)"
        elif (dat['numYearsGained'][ii] > -30) & (dat['numYearsGained'][ii] <= -15):
            dat['yrGainedSign'][ii] = "(-30)-(-15)"
        elif (dat['numYearsGained'][ii] > -15) & (dat['numYearsGained'][ii] <= 0):
            dat['yrGainedSign'][ii] = "(-15)-(0)"
        elif (dat['numYearsGained'][ii] > 0) & (dat['numYearsGained'][ii] <= 30):
            dat['yrGainedSign'][ii] = "0-30"
        elif (dat['numYearsGained'][ii] > 30) & (dat['numYearsGained'][ii] <= 60):
            dat['yrGainedSign'][ii] = "30-60"
        elif (dat['numYearsGained'][ii] > 60) & (dat['numYearsGained'][ii] <= 90):
            dat['yrGainedSign'][ii] = "60-90"
        elif (dat['numYearsGained'][ii] > 90) & (dat['numYearsGained'][ii] <= 120):
            dat['yrGainedSign'][ii] = "90-120"
        elif (dat['numYearsGained'][ii] > 120) & (dat['numYearsGained'][ii] <= 160):
            dat['yrGainedSign'][ii] = "120-160"

    # dat.to_csv(recon + "RecordLengthComparisonPlotter.csv")

    # plot 
    sns.set_context('notebook', font_scale = 1.5)

    plt.figure(figsize=(20, 10))
    m=Basemap(projection='cyl', lat_ts=20, llcrnrlon=-180, 
                urcrnrlon=180,llcrnrlat=-90,urcrnrlat=90, \
                    resolution='c')
    x,y = m(dat['lon'].tolist(), dat['lat'].tolist())
    m.drawcoastlines()

    #draw parallels and meridians 
    parallels = np.arange(-80,81,20.)
    m.drawparallels(parallels,labels=[True,False,False,False], \
                    linewidth = 0)
    m.drawmeridians(np.arange(0.,420.,30.),labels=[0,0,0,1], linewidth = 0) # draw meridians

    m.bluemarble(alpha = 0.85)
    
    ax = sns.scatterplot(x = x, y = y, s = 70, hue = 'yrGainedSign',  
            data = dat, edgecolor='black', linewidth=0.4, 
                palette = { 
                   "nan": "maroon",
                   "(-60)-(-30)":'red', 
                   "(-30)-(-15)":'lightcoral', 
                   "(-15)-(0)":'thistle', 
                   "0-30":'skyblue',
                   "30-60":'deepskyblue',
                   "60-90": "dodgerblue",
                   "90-120": "blue",
                   "120-160": "darkblue"
                   })


    plt.title("Extra Number of Years Gained From {} Surge Reconstruction (After Changepoint Analysis)".
                format(recon.upper()))

    plt.legend(loc = 3)

    # plt.savefig(recon + "RecordLengthComparison.svg", dpi = 400)

    plt.show()



plotIt("era20c")