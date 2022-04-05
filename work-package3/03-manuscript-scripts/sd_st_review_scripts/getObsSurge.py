"""
Created on Mon Dec 13 09:07:00 2021

get observed surge 

@author: Michael Tadesse

"""

import os 
import pandas as pd
from datetime import datetime


def getObsSurge(tg):

    dir_home = "G:\\report\\year-3\\07-Fall-2020\\#3Paper\\"\
    "data\\trend-analysis\\data\\03-obsSurge\\data"

    os.chdir(dir_home)

    time_stamp2 = lambda x: (datetime.strptime(x, '%Y-%m-%d'))


    dat = pd.read_csv(tg)
    dat['date'] = pd.DataFrame(list(map(time_stamp2, dat['ymd'])))
    return dat
