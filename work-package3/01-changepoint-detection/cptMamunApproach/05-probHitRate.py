import os
import pandas as pd


dir_home = "G:\\report\\year-3\\07-Fall-2020\\#3Paper\\data\\changePointTimeSeries\\"\
        "mamun-cpt-approach\\era20c\\0001-predCPT\\wnd_u\\04-probMinMax"
dir_orgn = "G:\\report\\year-3\\07-Fall-2020\\#3Paper\\data\\changePointTimeSeries\\"\
        "mamun-cpt-approach\\era20c\\0001-predCPT\\wnd_u\\originalBCP"
dir_out = "G:\\report\\year-3\\07-Fall-2020\\#3Paper\\data\\changePointTimeSeries\\"\
        "mamun-cpt-approach\\era20c\\0001-predCPT\\wnd_u\\05-probHitRate"

os.chdir(dir_home)
tgList = os.listdir()

#loop through tide gauges
for ii in range(len(tgList)):
    tg = tgList[ii]
    print(tg)
    
    os.chdir(dir_home)

    sortedProb = pd.read_csv(tg)

    os.chdir(dir_orgn)
    orgnProb = pd.read_csv(tg)
    

    datHitRate = pd.merge(orgnProb, sortedProb, on="year", \
        how="outer")[['year', 'minProb', 'maxProb', 'prob']]

    # get the hit rate - TRUE means changepoint found 
    datHitRate['hitrate'] = datHitRate['prob'] > datHitRate['maxProb']

    os.chdir(dir_out)
    datHitRate.to_csv(tg)

