import os 
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt 

dir_home = "G:\\report\\year-3\\07-Fall-2020\\#3Paper\\data\\"\
"changePointTimeSeries\\mamun-cpt-approach\\era20c\\001-tgsAnnualCorr\\annualCorr"

os.chdir(dir_home)

tgList = os.listdir()

#loop through tide gauges
for tg in tgList:
    dat = pd.read_csv(tg)
    plt.figure()
    plt.plot(dat['year'], dat['correlation'])
    ylabel = ("Pearson Correlation")
    plt.savefig(tg + '.jpeg', dpi=300)