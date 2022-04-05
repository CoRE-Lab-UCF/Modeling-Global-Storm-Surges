"""  
this script compares twcr recon cpt vs twcr pred cpts
"""

import os 
import pandas as pd
from functools import reduce
import numpy as np
import matplotlib.pyplot as plt 
from datetime import datetime


# cpt directories
dirRecon = "G:\\report\\year-3\\07-Fall-2020\\#3Paper\\data\\"\
            "changePointTimeSeries\\mamun-cpt-approach\\twcr\\06-globalCpt"
dirSLP = "G:\\report\\year-3\\07-Fall-2020\\#3Paper\\data\\changePointTimeSeries"\
        "\\mamun-cpt-approach\\twcr\\0001-predCPT\\slp\\06-globalCpt"
dirWNDU = "G:\\report\\year-3\\07-Fall-2020\\#3Paper\\data\\changePointTimeSeries"\
        "\\mamun-cpt-approach\\twcr\\0001-predCPT\\wnd_u\\06-globalCpt"
dirWNDV = "G:\\report\\year-3\\07-Fall-2020\\#3Paper\\data\\changePointTimeSeries"\
        "\\mamun-cpt-approach\\twcr\\0001-predCPT\\wnd_v\\06-globalCpt"


# recon cpt
os.chdir(dirRecon) 
reconCPT = pd.read_csv('twcrGlobalCPT.csv')
reconCPT = reconCPT[['tg', 'lon', 'lat', 'year']]
reconCPT.columns = ['tg', 'lon', 'lat', 'reconCPT']
print(reconCPT)

# slp cpt
os.chdir(dirSLP) 
slpCPT = pd.read_csv('twcrSLPGlobalCPT.csv')
slpCPT = slpCPT[['tg', 'year']]
slpCPT.columns = ['tg', 'slpCPT']
print(slpCPT)

# wndu cpt
os.chdir(dirWNDU) 
wnduCPT = pd.read_csv('twcrWNDUGlobalCPT.csv')
wnduCPT = wnduCPT[['tg', 'year']]
wnduCPT.columns = ['tg', 'wnduCPT']
print(wnduCPT)

# wndv cpt
os.chdir(dirWNDV) 
wndvCPT = pd.read_csv('twcrWNDVGlobalCPT.csv')
wndvCPT = wndvCPT[['tg', 'year']]
wndvCPT.columns = ['tg', 'wndvCPT']
print(wndvCPT)


# compile all dfs
dfCompiled = [reconCPT, slpCPT, wnduCPT, wndvCPT]
print(dfCompiled)

# merge dfs
dfMerged = reduce(lambda left, right: \
        pd.merge(left, right, on = ['tg'], how="outer"), dfCompiled)


# find pred with most recent cpt
dfMerged['recentCPT'] = dfMerged.iloc[:, 4:7].idxmax(axis = 1);
dfMerged['farthestCPT'] = dfMerged.iloc[:, 4:7].idxmin(axis = 1);
dfMerged['uniqueCPT'] = ~dfMerged.iloc[:, 4:7].nunique(axis = 1).eq(1);


print(dfMerged)
dfMergedUnique = dfMerged[dfMerged['uniqueCPT'] == True]

print(dfMergedUnique)

print(dfMergedUnique['recentCPT'].value_counts())
print(dfMergedUnique['farthestCPT'].value_counts())

# print(dfMerged.iloc[:, 4:7].nunique(axis = 1).eq(1))


# save as csv
os.chdir(dirRecon)
# dfMerged.to_csv('twcrRecon_Pred_CPT.csv')

# reset index for plotting
dfMerged.reset_index(inplace = True)

# # scatter plot cpt for comparisons
# plt.figure(figsize=(10, 5))
# plt.scatter(dfMerged['index'], dfMerged['reconCPT'], color = "green", label = "reconCPT")
# plt.scatter(dfMerged['index'], dfMerged['slpCPT'], color = "red", label = "slpCPT")
# plt.scatter(dfMerged['index'], dfMerged['wnduCPT'], color = "black", label = "wnduCPT")
# plt.scatter(dfMerged['index'], dfMerged['wndvCPT'], color = "magenta", label = "wndvCPT")
# plt.legend()
# plt.show()


# bar plot cpt for comparisons
plt.figure(figsize=(10, 5))
plt.bar(dfMerged['index'], dfMerged['reconCPT'], color = "green", label = "reconCPT")
plt.bar(dfMerged['index'], dfMerged['slpCPT'], color = "red", label = "slpCPT")
plt.bar(dfMerged['index'], dfMerged['wnduCPT'], color = "black", label = "wnduCPT")
plt.bar(dfMerged['index'], dfMerged['wndvCPT'], color = "magenta", label = "wndvCPT")
plt.legend()
plt.show()