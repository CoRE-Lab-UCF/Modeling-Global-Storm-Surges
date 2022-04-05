"""  
this script just plots
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

dirSTD = "G:\\report\\year-3\\07-Fall-2020\\#3Paper\\data\\changePointTimeSeries\\"\
        "mamun-cpt-approach\\twcr\\0001-predCPT\\wnd_v\\annualSTD"

dirBCP = "G:\\report\\year-3\\07-Fall-2020\\#3Paper\\data\\changePointTimeSeries"\
        "\\mamun-cpt-approach\\twcr\\0001-predCPT\\wnd_v\\originalBCP"

dirReconSTD = "G:\\report\\year-3\\07-Fall-2020\\#3Paper\\data\\"\
        "changePointTimeSeries\\20crSTD"

dirReconBCP = "G:\\report\\year-3\\07-Fall-2020\\#3Paper\\"\
        "data\\changePointTimeSeries\\20crBCP"

datAllCpt = "G:\\report\\year-3\\07-Fall-2020\\#3Paper\\data\\changePointTimeSeries\\"\
        "mamun-cpt-approach\\twcr\\0001-predCPT\\combinedBCP"




dirEra5STD = "G:\\report\\year-3\\07-Fall-2020\\#3Paper\\data\\"\
    "changePointTimeSeries\\mamun-cpt-approach\\era5\\basePrat-data"\
        "\\allPred\\04-annualSTD"
dirTwcrSTD = "G:\\report\\year-3\\07-Fall-2020\\#3Paper\\data\\changePointTimeSeries\\"\
        "mamun-cpt-approach\\twcr\\0001-predCPT\\wnd_v\\annualSTD"

dirEra20cSTD = "G:\\report\\year-3\\07-Fall-2020\\#3Paper\\data\\"\
        "changePointTimeSeries\\mamun-cpt-approach\\era20c\\0001-predCPT\\wnd_v\\annualSTD"

# era5
os.chdir(dirEra5STD)
dat = pd.read_csv("wnd_vSTD.csv")

plt.figure(figsize=(10,4))
plt.plot(dat['year'], dat['value'],  color = "black", lw = 2.5, \
        label = "era5-wnd_v-std")

# twcr
os.chdir(dirTwcrSTD)
dat = pd.read_csv("base_prat_b_730b_chile.csv")
plt.plot(dat['year'], dat['value'],  color = "green", lw = 2.5, label = "twcr-wnd_v-std")

# era20c
os.chdir(dirEra20cSTD)
dat = pd.read_csv("base_prat_b_730b_chile.csv")
plt.plot(dat['year'], dat['value'],  color = "magenta", lw = 2.5, label = "era20c-wnd_v-std")


plt.ylabel("annual variability in Pa")
plt.grid(b=None, which='major', axis= 'both', linestyle='-')
plt.minorticks_on()
plt.grid(b=None, which='minor', linestyle='--', axis="both", alpha=0.4)

plt.legend()
plt.show()






# os.chdir(dirRecon)
# os.chdir(dirSTD)
# os.chdir(dirBCP)
# os.chdir(dirReconSTD)
# os.chdir(dirReconBCP)
# os.chdir(datAllCpt)

# # dat = pd.read_csv('twcrRecon_Pred_CPT_v2.csv')
# tg = "newyork_thebattery__usa.csv"
# dat = pd.read_csv(tg)
# dat['p_avg'] = dat.iloc[:, 2:6].mean(axis = 1)

# print(dat)

# plt.figure(figsize=(15, 5))
# plt.scatter(dat['year'], dat['p_slp'], s = 16, color = "blue", label = "p_slp")
# plt.scatter(dat['year'], dat['p_u'], s = 16, color = "green", label = "p_u")
# plt.scatter(dat['year'], dat['p_v'], s = 16, color = "magenta", label = "p_v")
# plt.scatter(dat['year'], dat['p_recon'], s = 16, color = "red", label = "p_recon")
# plt.plot(dat['year'], dat['p_avg'],  color = "black", lw = 2.5, label = "p_avg")
# plt.ylabel("changepoint probability")
# plt.legend()
# plt.grid(b=None, which='major', axis= 'both', linestyle='-')
# plt.minorticks_on()
# plt.grid(b=None, which='minor', linestyle='--', axis="both", alpha=0.4)
# plt.title(tg.split('.csv')[0])
# plt.show()


# compute differences between cpts with reconCPT
# dat['recon_slp'] = abs(dat['reconCPT'] - dat['slpCPT']) 
# dat['recon_wndu'] = abs(dat['reconCPT'] - dat['wnduCPT'])
# dat['recon_wndv'] = abs(dat['reconCPT'] - dat['wndvCPT'])

# dat['maxDiff'] = dat.iloc[:,12:15].idxmax(axis = 1)
# dat['minDiff'] = dat.iloc[:,12:15].idxmin(axis = 1)

# print(dat)

# dfMergedUnique = dat[dat['uniqueCPT'] == True]


# print(dfMergedUnique['maxDiff'].value_counts())
# print(dfMergedUnique['minDiff'].value_counts())

# # bar plot cpt for comparisons

# width = 0.5

# plt.figure(figsize=(10, 5))
# plt.bar(dat['Unnamed: 0'] - 2*width, dat['reconCPT'] - dat['minCPT'], width,  color = "green", label = "reconCPT")
# # plt.bar(dat['Unnamed: 0'] - width, dat['slpCPT'] - dat['minCPT'], width, color = "red", label = "slpCPT")
# # plt.bar(dat['Unnamed: 0'], dat['wnduCPT'] - dat['minCPT'], width, color = "black", label = "wnduCPT")
# # plt.bar(dat['Unnamed: 0'] + width, dat['wndvCPT'] - dat['minCPT'], width, color = "magenta", label = "wndvCPT")
# plt.ylabel('Diffrence in years from the farthest CPT')
# plt.legend()
# plt.show()


# # scatter plot cpt for comparisons
# plt.figure(figsize=(10, 5))
# plt.plot(dat['Unnamed: 0'], dat['reconCPT']-dat['slpCPT'], color = "green", label = "reconCPT vs slpCPT")
# plt.plot(dat['Unnamed: 0'], dat['reconCPT']-dat['wnduCPT'], color = "magenta", label = "reconCPT vs wnduCPT")
# plt.plot(dat['Unnamed: 0'], dat['reconCPT']-dat['wndvCPT'], color = "blue", label = "reconCPT vs wndvCPT")
# # plt.scatter(dat['Unnamed: 0'], dat['wnduCPT'], color = "black", label = "wnduCPT")
# # plt.scatter(dat['Unnamed: 0'], dat['wndvCPT'], color = "magenta", label = "wndvCPT")
# plt.legend()
# plt.show()

# scatter plot cpt for comparing cpt differences
# plt.figure(figsize=(10, 5))
# plt.plot(dat['Unnamed: 0'], dat['recon_slp'], color = "green", label = "reconCPT vs slpCPT")
# plt.plot(dat['Unnamed: 0'], dat['recon_wndu'], color = "magenta", label = "reconCPT vs wnduCPT")
# plt.plot(dat['Unnamed: 0'], dat['recon_wndv'], color = "blue", label = "reconCPT vs wndvCPT")
# plt.scatter(dat['Unnamed: 0'], dat['wnduCPT'], color = "black", label = "wnduCPT")
# plt.scatter(dat['Unnamed: 0'], dat['wndvCPT'], color = "magenta", label = "wndvCPT")
# plt.legend()
# plt.show()