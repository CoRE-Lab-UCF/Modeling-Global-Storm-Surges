"""  
this script gets the boolean value for probability thresholds
of [0.05, 0.5]
"""

import os 
import pandas as pd
from functools import reduce
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from datetime import datetime

dirHome = "G:\\report\\year-3\\07-Fall-2020\\#3Paper\\data\\changePointTimeSeries\\"\
    "mamun-cpt-approach\\shortTwcr\\01-combinedBCP"
dirOut = "G:\\report\\year-3\\07-Fall-2020\\#3Paper\\data\\changePointTimeSeries\\"\
    "mamun-cpt-approach\\shortTwcr\\02-cptProbs"

os.chdir(dirHome)
tgList = os.listdir()

for tg in tgList:

    os.chdir(dirHome)

    print(tg)

    dat = pd.read_csv(tg)
    dat['p_avg'] = dat.iloc[:,2:6].mean(axis = 1)

    # prob thresholds
    dat['p_5'] = dat['p_avg'] >= 0.05
    dat['p_10'] = dat['p_avg'] >= 0.1
    dat['p_15'] = dat['p_avg'] >= 0.15
    dat['p_20'] = dat['p_avg'] >= 0.2
    dat['p_25'] = dat['p_avg'] >= 0.25
    dat['p_30'] = dat['p_avg'] >= 0.3
    dat['p_40'] = dat['p_avg'] >= 0.4
    dat['p_50'] = dat['p_avg'] >= 0.50

    # print(dat)

    os.chdir(dirOut)

    # save as csv
    dat.to_csv(tg)