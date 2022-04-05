import os
import pandas as pd

dir_home = "G:\\report\\year-3\\07-Fall-2020\\#3Paper\\data\\changePointTimeSeries"\
    "\\mamun-cpt-approach\\era20c\\0001-predCPT\\wnd_v\\02-randomizedBCP"
dir_out = "G:\\report\\year-3\\07-Fall-2020\\#3Paper\\data\\changePointTimeSeries"\
    "\\mamun-cpt-approach\\era20c\\0001-predCPT\\wnd_v\\03-probRang"

def concatProbRange():
    """
    this function prepares a dataframe of
    N changepoint probabilities for each year
    for each tide gauge
    """
    os.chdir(dir_home)

    tgList = os.listdir()

    #loop through the tide gauges
    for ii in range(len(tgList)):
        tg = tgList[ii]
        print(tg)

        os.chdir(dir_home + "\\" + tg)

        itrList = os.listdir()

        isFirst = True; #first csv 

        for itr in itrList:
            print(itr)
            
            if isFirst:
                stdDat = pd.read_csv(itr)
                print(stdDat)
                stdDat.drop(['Unnamed: 0', 'mean'], axis = 1, inplace = True)
                dat = stdDat
                isFirst = False;
            else:
                stdDat = pd.read_csv(itr)
                stdDat.drop(['Unnamed: 0', 'mean'], axis = 1, inplace = True)
                dat = pd.merge(dat, stdDat, on = "year", how = "outer") 

        # save merge probability range
        os.chdir(dir_out)
        dat.to_csv(tg)

concatProbRange()


