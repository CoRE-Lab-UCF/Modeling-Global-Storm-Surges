import os 
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt 
from datetime import datetime
from sklearn.metrics import mean_squared_error
from scipy import stats

"""
this script computes the annual correlation
"""


dir_home = "G:\\report\\year-3\\07-Fall-2020\\#3Paper\\data\\"\
    "changePointTimeSeries\\mamun-cpt-approach\\twcr\\001-additionalTesting\\mergedSurge"

dir_out = "G:\\report\\year-3\\07-Fall-2020\\#3Paper\\data\\"\
    "changePointTimeSeries\\mamun-cpt-approach\\twcr\\001-additionalTesting\\annualRMSE"


os.chdir(dir_home)
tgList = os.listdir()

#loop through tide gauges
for tg in tgList:
    os.chdir(dir_home)
    dat = pd.read_csv(tg)
    
    getYear = lambda x: x.split('-')[0]
    dat['year'] = pd.DataFrame(list(map(getYear, dat['date'])))

    #get annual rmse
    rmse = pd.DataFrame(columns=['year', 'rmse'])
    years = dat['year'].unique()

    for jj in years:
        currentYear = dat[dat['year'] == jj]
        mse = mean_squared_error(currentYear['surge'], \
                currentYear['surge_reconsturcted'])

        df = pd.DataFrame([jj, mse**0.5]).T

        df.columns = ['year', 'rmse']
        rmse = pd.concat([rmse, df], axis = 0)

    os.chdir(dir_out)

    rmse.to_csv(tg)