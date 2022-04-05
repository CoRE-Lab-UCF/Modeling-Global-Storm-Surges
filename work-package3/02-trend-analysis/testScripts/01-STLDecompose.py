#get libraries
import os 
import pandas as pd 
from datetime import datetime
from statsmodels.tsa.seasonal import seasonal_decompose
from statsmodels.tsa.seasonal import STL
import matplotlib.pyplot as plt

dir_in = "G:\\report\\year-3\\07-Fall-2020\\#3Paper\\data\\changePointTimeSeries"\
        "\\mamun-cpt-approach\\era20c\\08-postCPT"
dir_out = "G:\\report\\year-3\\07-Fall-2020\\#3Paper\\data\\changePointTimeSeries\\"\
        "mamun-cpt-approach\\era20c\\09-deSeasoned"


os.chdir(dir_in)

tgList = os.listdir()

#loop through tgs
for tg in tgList:
        print(tg)
        dat = pd.read_csv(tg)
        
        time_stamp = lambda x: (datetime.strptime(x, '%Y-%m-%d %H:%M:%S'))

        dat['date'] = pd.DataFrame(list(map(time_stamp, dat['date'])))

        series = dat[['date', 'lon', 'lat', 'surge_reconsturcted']]
        series.set_index('date', inplace = True)

        ### Season-Trend decomposition using LOESS
        res = STL(series['surge_reconsturcted']).fit()
        seasonal = pd.DataFrame(res.seasonal)

        os.chdir(dir_out)
        series['seasonal'] = seasonal
        series['sasnAdjusted'] = series['surge_reconsturcted'] - series['seasonal']
        series['sasnAdjusted_mm'] = series['sasnAdjusted']*1000
        series.to_csv(tg)

        os.chdir(dir_in)

