"""  
this function gets the slp, uwnd, and vwnd
predictors - saves them in the predCPT folder
"""
import shutil
import os
import pandas as pd
from os.path import exists

dirHome = "G:\\report\\year-3\\07-Fall-2020\\#3Paper\\"\
    "data\\changePointTimeSeries\\mamun-cpt-approach\\era20c\\05-probHitRate"
dirSource = "F:\\02_era20C\\01_era20C_predictors"
dirDest = "G:\\report\\year-3\\07-Fall-2020\\#3Paper"\
    "\\data\\changePointTimeSeries\\mamun-cpt-approach\\era20c\\0001-predCPT"

def getPredictor(pred):
    """  
    pred: could be slp, wnd_u, or wnd_v
    """
    os.chdir(dirHome)

    cptList = os.listdir()

    for ii in cptList:
        
        tg = ii.split('.csv')[0]
        print(tg)

        os.chdir(dirSource + "\\" + tg)

        dat = pred + ".csv"

        if not exists(dat):
            print("not found")
        else:
            source = os.path.join(os.path.abspath(os.getcwd()), dat)
            print(source)
            destination = os.path.join(os.path.join(dirDest, pred), ii)
            print(destination)

            try:
                shutil.copyfile(source, destination)
            except shutil.SameFileError:
                print("source and destination represent the same file")
            except:
                print("error occured while copying file")


getPredictor("wnd_v")