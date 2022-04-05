import os
import pandas as pd

dir_home = "G:\\report\\year-3\\07-Fall-2020\\#3Paper\\data\\changePointTimeSeries\\"\
        "mamun-cpt-approach\\era20c\\0001-predCPT\\wnd_u\\05-probHitRate"
dir_tg = "G:\\data\\allReconstructions\\02_era20c"


def getLonLat():
    """
    this function obtains the lon/lat for the hitrate data
    to be used for global plotting
    """
    os.chdir(dir_home)
    tgList = os.listdir()

    for ii in range(len(tgList)):
        tg = tgList[ii]

        print(tg)

        #get the corresponding file with lon/lat
        os.chdir(dir_tg)
        x = pd.read_csv(tg)
        lon = x['lon'][0]
        lat = x['lat'][0]

        #add lon/lat to hitrate file
        os.chdir(dir_home)
        dat = pd.read_csv(tg)
        dat['lon'] = lon
        dat['lat'] = lat

        #save it as csv - replace file
        dat.to_csv(tg)

#run script
getLonLat()