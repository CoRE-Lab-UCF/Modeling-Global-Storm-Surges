import os
import pandas as pd


dir_home = "G:\\report\\year-3\\07-Fall-2020\\#3Paper\\data\\changePointTimeSeries\\"\
        "mamun-cpt-approach\\comparison"
dir_tgs = "G:\\data\\allReconstructions\\06_dmax_surge_georef"

os.chdir(dir_home)

cptFile = pd.read_csv("twcrEra20cMerged.csv")

cptFile['start'] = 'nan'
cptFile['end'] = 'nan'
cptFile['length'] = 'nan'


# is the changepoint in the middle of start and end
# and is not 1836 nor 1900?
cptFile['twcr'] = 'nan' 
cptFile['era20c'] = 'nan'
cptFile['both'] = 'nan'

for ii in range(len(cptFile['tg'])):

    os.chdir(dir_home)

    tg = cptFile['tg'][ii]
    
    print(tg)

    os.chdir(dir_tgs)

    dat = pd.read_csv(tg)

    cptFile.loc[ii, 'start'] = dat['date'][0].split('-')[0]
    cptFile.loc[ii, 'end'] = dat['date'][len(dat) - 1].split('-')[0]
    cptFile.loc[ii, 'length'] = int(cptFile.loc[ii, 'end']) - int(cptFile.loc[ii, 'start'])


    if (cptFile.loc[ii, 'year_twcr'] != 1836) \
        and (cptFile.loc[ii, 'year_twcr'] >= int(cptFile.loc[ii, 'start'])):
        cptFile.loc[ii, 'twcr'] = True

    if cptFile.loc[ii, 'year_era20c'] != 1900 \
        and (cptFile.loc[ii, 'year_era20c'] >= int(cptFile.loc[ii, 'start'])):
        cptFile.loc[ii, 'era20c'] = True

    # if both are inside start and end
    if (cptFile.loc[ii, 'era20c'] ==True) and (cptFile.loc[ii, 'twcr'] == True):
        cptFile.loc[ii, 'both'] = True

os.chdir(dir_home)
cptFile.to_csv('twcrEra20cMergedStartEnd.csv')