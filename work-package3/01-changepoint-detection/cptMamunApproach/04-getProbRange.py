import os
import pandas as pd

dir_home = "G:\\report\\year-3\\07-Fall-2020\\#3Paper\\data\\changePointTimeSeries"\
    "\\mamun-cpt-approach\\era20c\\0001-predCPT\\wnd_u\\03-probRang"
dir_out = "G:\\report\\year-3\\07-Fall-2020\\#3Paper\\data\\changePointTimeSeries"\
        "\\mamun-cpt-approach\\era20c\\0001-predCPT\\wnd_u\\04-probMinMax"

def getProbRange():
    """
    this function gets the probability range interval
    gets the min and max of the N iteration bcp probabilities
    """
    os.chdir(dir_home)
    pList = os.listdir()

    for ii in range(len(pList)):
        p= pList[ii]
        print(p)

        os.chdir(dir_home)
        dat = pd.read_csv(p)
        dat.drop(['Unnamed: 0'], axis = 1, inplace = True)
        print(dat.columns)

        dat['minProb'] = dat.iloc[:, 1:].min(axis= 1)
        dat['maxProb'] = dat.iloc[:, 1:].max(axis= 1)

        dat.sort_values(by = 'year', inplace = True)

        os.chdir(dir_out)

        dat[['year', 'minProb', 'maxProb']].to_csv(p)

#run function
getProbRange()
