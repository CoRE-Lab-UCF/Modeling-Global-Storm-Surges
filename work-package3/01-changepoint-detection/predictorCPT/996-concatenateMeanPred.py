"""  
this script concatenates mean era5 predictors before 
calculating the annual std  
"""

import os
import pandas as pd 
from glob import glob


dirHome = "G:\\report\\year-3\\07-Fall-2020\\#3Paper\\data\\"\
    "changePointTimeSeries\\mamun-cpt-approach\\era5\\basePrat-data"\
        "\\allPred\\02-meanPred"
dirOut = "G:\\report\\year-3\\07-Fall-2020\\#3Paper\\data\\"\
    "changePointTimeSeries\\mamun-cpt-approach\\era5\\basePrat-data"\
        "\\allPred\\03-concatPred"


def concatPred(pred):
    os.chdir(dirHome)
    predList = glob('{}*'.format(pred))
    print(predList)

    predDF = pd.DataFrame()
    for pp in predList:
        print(pp)

        dat = pd.read_csv(pp)
        predDF = pd.concat([predDF, dat], axis = 0)
    
    os.chdir(dirOut)
    predDF.to_csv(pred + ".csv")



concatPred("wnd_v")