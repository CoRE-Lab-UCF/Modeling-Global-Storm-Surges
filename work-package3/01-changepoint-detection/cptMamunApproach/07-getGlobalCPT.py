"""  
change name of file for reanalysis type
"""

import os
import pandas as pd

dir_home = "G:\\report\\year-3\\07-Fall-2020\\#3Paper\\data\\changePointTimeSeries\\"\
        "mamun-cpt-approach\\twcr\\0001-predCPT\\wnd_v\\05-probHitRate"
dir_out = "G:\\report\\year-3\\07-Fall-2020\\#3Paper\\data\\changePointTimeSeries\\"\
        "mamun-cpt-approach\\twcr\\0001-predCPT\\wnd_v\\06-globalCpt"


def getGlobalCPT():
    """
    this function gets the most recent CPT of all
    available tide gauges - also georeferenced
    """

    os.chdir(dir_home)
    tgList = os.listdir()

    #create an empty dataframe
    df = pd.DataFrame(columns = ['tg', 'lon', 'lat', 'year', 'minProb','maxProb', 'prob'])

    #loop over tide gauges
    for ii in range(len(tgList)):
        tg = tgList[ii]
        print(tg)

        os.chdir(dir_home)

        dat = pd.read_csv(tg)
        datHit = dat[dat['hitrate'] == True].iloc[-1:,:]
        
        #when no change point is detected
        #change year to 1900 for era20c; 1836 for twcr
        if (datHit.empty):
            print('\nempty dataframe \n')
            newDf = pd.DataFrame([tg, dat['lon'][0], dat['lat'][0], \
                1836, 'nan', 'nan', 'nan']).T
            newDf.columns = ['tg', 'lon', 'lat', 'year', 'minProb','maxProb', 'prob']

        else:
            newDf = pd.DataFrame([tg, datHit['lon'].values[0], datHit['lat'].values[0], \
                datHit['year'].values[0], datHit['minProb'].values[0], \
                    datHit['maxProb'].values[0], datHit['prob'].values[0]]).T
            newDf.columns = ['tg', 'lon', 'lat', 'year', 'minProb','maxProb', 'prob']
        
        newDf.columns = ['tg', 'lon', 'lat', 'year', 'minProb','maxProb', 'prob']

        df = pd.concat([df, newDf], axis = 0)
    
    # #save sa csv
    os.chdir(dir_out)
    df.to_csv('twcrWNDVGlobalCPT.csv')

#run function
getGlobalCPT()