"""  
this script analyzes the comparison in changepoints
between twcr and era20c averaged bcp - for 1900-2010
"""
import os 
import pandas as pd

dirHome = "G:\\report\\year-3\\07-Fall-2020\\#3Paper\\data\\changePointTimeSeries"\
    "\\mamun-cpt-approach\\twcr_era20c_1900_2010"

os.chdir(dirHome)

dat = pd.read_csv("cptSAComparison.csv")

# print(dat[(dat["p_5T"] - dat["p_5E"]) >10][["p_5T", "p_5E"]])

# check if there is a difference of 10 or more years for 
# every cutoff probability
dat['p5'] = abs(dat["p_5T"] - dat["p_5E"]) > 10
dat['p10'] = abs(dat["p_10T"] - dat["p_10E"]) > 10
dat['p15'] = abs(dat["p_15T"] - dat["p_15E"]) > 10
dat['p20'] = abs(dat["p_20T"] - dat["p_20E"]) > 10
dat['p25'] = abs(dat["p_25T"] - dat["p_25E"]) > 10
dat['p30'] = abs(dat["p_30T"] - dat["p_30E"]) > 10
dat['p40'] = abs(dat["p_40T"] - dat["p_40E"]) > 10
dat['p50'] = abs(dat["p_50T"] - dat["p_50E"]) > 10


dat['p5E'] = 'nan'
dat['p10E'] = 'nan'
dat['p15E'] = 'nan'
dat['p20E'] = 'nan'
dat['p25E'] = 'nan'
dat['p30E'] = 'nan'
dat['p40E'] = 'nan'
dat['p50E'] = 'nan'


for ii in range(len(dat)):
    print(dat['tg'][ii])

    # p5
    if dat['p5'][ii]:
        dat['p5E'][ii] = dat["p_5E"][ii] < dat["p_5T"][ii] # true -> era20c has earlier cpt
    else:
        dat['p5E'][ii] = 'nan' # no diff b/n twcr and era20c
        
    # p10
    if dat['p10'][ii]:
        dat['p10E'][ii] = dat["p_10E"][ii] < dat["p_10T"][ii] # true -> era20c has earlier cpt
    else:
        dat['p10E'][ii] = 'nan' # no diff b/n twcr and era20c
  
    # p15
    if dat['p15'][ii]:
        dat['p15E'][ii] = dat["p_15E"][ii] < dat["p_15T"][ii] # true -> era20c has earlier cpt
    else:
        dat['p15E'][ii] = 'nan' # no diff b/n twcr and era20c
   
    # p20
    if dat['p20'][ii]:
        dat['p20E'][ii] = dat["p_20E"][ii] < dat["p_20T"][ii] # true -> era20c has earlier cpt
    else:
        dat['p20E'][ii] = 'nan' # no diff b/n twcr and era20c
    
    # p25
    if dat['p25'][ii]:
        dat['p25E'][ii] = dat["p_25E"][ii] < dat["p_25T"][ii] # true -> era20c has earlier cpt
    else:
        dat['p25E'][ii] = 'nan' # no diff b/n twcr and era20c
    
    # p30
    if dat['p30'][ii]:
        dat['p30E'][ii] = dat["p_30E"][ii] < dat["p_30T"][ii] # true -> era20c has earlier cpt
    else:
        dat['p30E'][ii] = 'nan' # no diff b/n twcr and era20c
    
    # p40
    if dat['p40'][ii]:
        dat['p40E'][ii] = dat["p_40E"][ii] < dat["p_40T"][ii] # true -> era20c has earlier cpt
    else:
        dat['p40E'][ii] = 'nan' # no diff b/n twcr and era20c
    
    # p50
    if dat['p50'][ii]:
        dat['p50E'][ii] = dat["p_50E"][ii] < dat["p_50T"][ii] # true -> era20c has earlier cpt
    else:
        dat['p50E'][ii] = 'nan' # no diff b/n twcr and era20c

dat.to_csv("twcrEra20c_cptComparison.csv")