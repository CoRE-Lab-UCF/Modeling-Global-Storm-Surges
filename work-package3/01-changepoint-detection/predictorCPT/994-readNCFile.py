"""  
this script is to extract individual predictors from era5 
and save them as csv files
"""


import os
import datetime
from glob import glob
import pandas as pd
from netCDF4 import Dataset
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
#locate the file that basemap needs
os.environ["PROJ_LIB"] = "C:\\Users\\WahlInstall\\"\
    "Anaconda3\\Library\\share\\basemap"
from mpl_toolkits.basemap import Basemap



dirHome = "G:\\report\\year-3\\07-Fall-2020\\#3Paper\\data\\"\
    "changePointTimeSeries\\mamun-cpt-approach\\era5\\basePrat-data"\
        "\\allPred\\allPredNC"

dirOut = "G:\\report\\year-3\\07-Fall-2020\\#3Paper\\data\\"\
    "changePointTimeSeries\\mamun-cpt-approach\\era5\\basePrat-data"\
        "\\allPred\\01-rawPred"

os.chdir(dirHome)

# changed name of nc file - was error previously
predList = glob('*{}'.format(".nc"))


def plotNC():
    """  
    this function overlays one of the predictors 
    on top of the bluemarble map
    """
    
    basePratLon = -59.633
    basePratLat = -62.483

    # plotting predictors 
    # plot 
    sns.set_context('notebook', font_scale = 1.5)

    plt.figure(figsize=(20, 10))
    m=Basemap(projection='cyl', lat_ts=20, llcrnrlon=-180, 
                urcrnrlon=180,llcrnrlat=-90,urcrnrlat=90, \
                    resolution='c')
    x,y = m(lon, lat)
    m.drawcoastlines()

    #draw parallels and meridians 
    parallels = np.arange(-80,81,20.)
    m.drawparallels(parallels,labels=[True,False,False,False], \
                    linewidth = 0)
    m.drawmeridians(np.arange(0.,420.,30.),labels=[0,0,0,1], linewidth = 0) # draw meridians

    m.bluemarble(alpha = 0.85)
    plt.pcolor(x, y, u10[0, :, :], cmap = "hsv")
    plt.colorbar()

    # add tide gauge location
    plt.scatter(basePratLon, basePratLat, marker = "*", s = 250, color = 'black')

    # plt.title("{} - tide gauges with {} or more years of data - total = {} tgs".format(reanalysis, yrLength, len(dat)))

    # plt.legend(loc = 3)

    plt.show()

for f in predList:
    os.chdir(dirHome)

    print(f, "\n")

    # loop though nc files from 1950-1978
    g = Dataset(f)
    
    print(g.variables)

    lon = g.variables['longitude'][:]
    lat = g.variables['latitude'][:]
    u10 = g.variables['u10']
    
    print("u10 shape = {}".format(u10.size))
    
    v10 = g.variables['v10']

    print("v10 shape = {}".format(u10.size))

    msl = g.variables['msl']

    print("msl shape = {}".format(msl.size))

    time = g.variables['time'][:]

    #prepare time format and concatenate it to subsetted pred
    time_original = pd.to_datetime('1900-01-01')
    int_changer = lambda x: int(x)
    time_int = pd.DataFrame(map(int_changer, time))    
    time_convertor = lambda x: time_original + datetime.timedelta(hours = x)
    time_readable = pd.DataFrame(map(time_convertor, time_int[0]), columns = ['date'])

    #############
    # plot netcdf
    #############
    # plotNC()

    u10Df = pd.DataFrame()
    v10Df = pd.DataFrame()
    mslDf = pd.DataFrame()

    for ii in range(len(lon)):
        for jj in range(len(lat)):
            # concatenate u10 
            # print("ii = {} - jj = {}".format(ii, jj))
            currentU10 = pd.DataFrame(u10[:, jj, ii])
            # print(currentU10)
            u10Df = pd.concat([u10Df, currentU10], axis = 1)

            # concatenate v10 
            currentv10 = pd.DataFrame(v10[:, jj, ii])
            v10Df = pd.concat([v10Df, currentv10], axis = 1)

            # concatenate msl 
            currentmsl = pd.DataFrame(msl[:, jj, ii])
            mslDf = pd.concat([mslDf, currentmsl], axis = 1)

    u10Df = pd.concat([time_readable, u10Df], axis = 1)
    v10Df = pd.concat([time_readable, v10Df], axis = 1)
    mslDf = pd.concat([time_readable, mslDf], axis = 1)

    # save df as csv
    os.chdir(dirOut)

    u10Df.to_csv("wnd_u_" + f.split('all_')[1].split('.nc')[0] + ".csv")
    v10Df.to_csv("wnd_v_" + f.split('all_')[1].split('.nc')[0] + ".csv")
    mslDf.to_csv("slp_" + f.split('all_')[1].split('.nc')[0] + ".csv")




