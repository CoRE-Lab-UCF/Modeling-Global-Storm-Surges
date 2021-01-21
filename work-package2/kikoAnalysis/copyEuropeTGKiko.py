# -*- coding: utf-8 -*-
"""
Created on Fri Sep 25 11:10:45 2020

@author: mi292519
"""

import os
import shutil
import pandas as pd

#get tgEurope from kikoAnalysis
tgEurope = pd.read_csv()



#set output files folder
dir_out_surge = 'G:\\data\\kikoAnalysis\\tgEurope'


for ii in range(len(tgEurope)):
    print(tgEurope['tg'][ii])
    os.chdir('G:\\data\\allReconstructions\\06_dmax_surge_georef')
    source = os.path.join(os.path.abspath(os.getcwd()), tgEurope['tg'][ii]+".csv")
    destination = os.path.join(dir_out_surge, tgEurope['tg'][ii]+".csv")
    shutil.copyfile(source, destination)