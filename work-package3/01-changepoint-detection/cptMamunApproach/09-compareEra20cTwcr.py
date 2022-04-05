import os
import pandas as pd

dir_home = "G:\\report\\year-3\\07-Fall-2020\\#3Paper\\data\\changePointTimeSeries\\"\
            "mamun-cpt-approach\\comparison"

def compare():
    """
    this function compares era20c and twcr changepoints
    """
    os.chdir(dir_home)
    twcrDat = pd.read_csv("twcrGlobalCPT.csv")

    twcrDat.columns = ['Unnamed: 0', 'tg', 'lon_twcr', 'lat_twcr', 'year_twcr', \
                'minProb_twcr', 'maxProb_twcr', 'prob_twcr']

    era20cDat = pd.read_csv("era20cGlobalCPT.csv")
    
    era20cDat.columns = ['Unnamed: 0', 'tg', 'lon', 'lat', 'year_era20c', \
                'minProb_era20c', 'maxProb_era20c', 'prob_era20c']

    # print(twcrDat)
    # print(era20cDat)

    #merge twcr and era20c
    mergeDat = pd.merge(era20cDat, twcrDat, on="tg", how = "inner")
    print(mergeDat)

    # print(mergeDat.isna().any(axis = 1))
    newDat = mergeDat[['tg', 'lon', 'lat', 'year_twcr', 'year_era20c']]
    newDat['hitrate'] = newDat['year_twcr'] <= newDat['year_era20c']
    # print(newDat[newDat['hitrate'] == False])

    newDat['reanalysis'] = 'nan'
    for ii in range(len(newDat)):
        if newDat['hitrate'][ii] == True:
            newDat['reanalysis'][ii] = '20CR'
        else:
            newDat['reanalysis'][ii] = 'ERA-20C'


    print(newDat[newDat['reanalysis'] == 'ERA-20C'])
    newDat.to_csv('twcrEra20cMerged.csv')

#run function
compare()