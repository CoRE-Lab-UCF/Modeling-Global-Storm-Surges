import os 
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt 
from datetime import datetime
from sklearn import metrics

"""
this script merges observed and reconstructed surges
"""


dir_home = "G:\\report\\year-3\\07-Fall-2020\\#3Paper\\data\\"\
    "changePointTimeSeries\\mamun-cpt-approach\\twcr\\001-additionalTesting"

dir_surge = "G:\\data\\allReconstructions\\06_dmax_surge_georef"


os.chdir(dir_home)
tgList = os.listdir()

#loop through tgs
for tg in tgList:
    os.chdir(dir_home)
    print(tg)
    recon = pd.read_csv(tg)

    getDate = lambda x:x.split(' ')[0]
    recon['date'] = pd.DataFrame(list(map(getDate, recon['date'])))
    # print(recon)


    os.chdir(dir_surge)
    obs = pd.read_csv(tg)
    obs['date'] = pd.DataFrame(list(map(getDate, obs['date'])))
    # print(obs)

    #merge recon and obs
    datMerged = pd.merge(recon, obs, on = "date", how='inner')
    datMerged = datMerged[['date', 'lon_x', 'lat_x', 'surge', 'surge_reconsturcted']]
    print(datMerged)


    saveName = tg.split('.csv')[0] + 'Merged.csv'
    
    os.chdir(dir_home)
    datMerged.to_csv(saveName)