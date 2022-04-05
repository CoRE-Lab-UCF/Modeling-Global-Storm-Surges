import os 
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt 
from datetime import datetime
from scipy import stats

"""
this script computes the annual correlation
"""


dir_home = "G:\\report\\year-3\\07-Fall-2020\\#3Paper\\data\\"\
        "changePointTimeSeries\\mamun-cpt-approach\\era20c\\001-tgsAnnualCorr\\merged"

dir_out = "G:\\report\\year-3\\07-Fall-2020\\#3Paper\\data\\"\
        "changePointTimeSeries\\mamun-cpt-approach\\era20c\\"\
                "001-tgsAnnualCorr\\annualCorr"


os.chdir(dir_home)
tgList = os.listdir()

#loop through tide gauges
for tg in tgList:
    os.chdir(dir_home)
    dat = pd.read_csv(tg)
    
    getYear = lambda x: x.split('-')[0]
    dat['year'] = pd.DataFrame(list(map(getYear, dat['date'])))

    #get annual correlation
    corr = pd.DataFrame(columns=['year', 'correlation'])
    years = dat['year'].unique()

    for jj in years:
        currentYear = dat[dat['year'] == jj]
        rho = stats.pearsonr(currentYear['surge'], currentYear['surge_reconsturcted'])[0]
        pval = stats.pearsonr(currentYear['surge'], currentYear['surge_reconsturcted'])[1]

        if pval >= 0.05:
            df = pd.DataFrame([jj, 'nan']).T
        else:
            df = pd.DataFrame([jj, rho]).T

        df.columns = ['year', 'correlation']
        corr = pd.concat([corr, df], axis = 0)

    os.chdir(dir_out)

    corr.to_csv(tg)