"""
Created on Wed Sep 22 07:41:00 2021

testing quantile regression

@author: Michael Tadesse

"""

import os
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib
import matplotlib.pyplot as plt
import statsmodels.api as sm
import statsmodels.formula.api as smf


dirHome = "G:\\report\\year-3\\07-Fall-2020\\"\
        "#3Paper\\data\\trend-analysis\\data\\02-era20c\\01-postCPT"

os.chdir(dirHome)

dat = pd.read_csv("cuxhaven_germany.csv")
dat.columns = ['ind', 'date', 'surge_reconsturcted', 'pred_int_lower',
    'pred_int_upper', 'lon', 'lat']

print(dat)

mod = smf.quantreg("surge_reconsturcted ~ ind", dat)
res = mod.fit(q=0.99)
print(res.summary())

#define figure and axis
fig, ax = plt.subplots(figsize=(8, 6))

#get y values
get_y = lambda a, b: a + b * dat['ind']
y = get_y(res.params['Intercept'], res.params['ind'])

#plot data points with quantile regression equation overlaid
ax.plot(dat['ind'], y, color='black')
ax.scatter(dat['ind'], dat['surge_reconsturcted'], alpha=.3)
ax.set_xlabel('ind', fontsize=14)
ax.set_ylabel('99th percentile surge', fontsize=14)

plt.show()