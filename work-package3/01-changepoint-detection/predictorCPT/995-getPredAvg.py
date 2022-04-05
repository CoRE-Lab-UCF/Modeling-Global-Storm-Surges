"""  
this script gets the average of era5 predictors before 
calculating the annual std  
"""

import os
import pandas as pd 

dirHome = "G:\\report\\year-3\\07-Fall-2020\\#3Paper\\data\\"\
    "changePointTimeSeries\\mamun-cpt-approach\\era5\\basePrat-data"\
        "\\allPred\\01-rawPred"
dirOut = "G:\\report\\year-3\\07-Fall-2020\\#3Paper\\data\\"\
    "changePointTimeSeries\\mamun-cpt-approach\\era5\\basePrat-data"\
        "\\allPred\\02-meanPred"


os.chdir(dirHome)

predList = os.listdir()

# loop through the pred files
for pp in predList:
    os.chdir(dirHome)
    
    print(pp)

    dat = pd.read_csv(pp)
    datMean = pd.concat([dat['date'], dat.mean(axis = 1)], axis = 1)
    
    os.chdir(dirOut)
    datMean.to_csv(pp)