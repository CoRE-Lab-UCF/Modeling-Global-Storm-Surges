# -*- coding: utf-8 -*-
"""
Created on Fri Jun 26 09:21:26 2020

Concatenate MERRA validation csv files

@author: Michael Tadesse
"""

import pandas as pd
import os

dir_in = "G:\\04_merra\\04_merra_model_validation\\lrreg"
dir_out = "G:\\04_merra\\04_merra_model_validation"

#cd to csv folders
os.chdir(dir_in)

tgNames = os.listdir()

#looping through the csv files
lrValidation = pd.DataFrame(columns = ['tg', 'lon', 'lat', 'num_year', 
                                       'num_95pcs', 'corrn','rmse'])

for tg in tgNames:
    print(tg)
    currentFile = pd.read_csv(tg)
    #rename tg name inside the csv
    currentFile['tg'] = tg
    currentFile.drop('Unnamed: 0', axis = 1, inplace = True)
    lrValidation = pd.concat([lrValidation, currentFile], axis = 0)
print("it is done!")

os.chdir(dir_out)

lrValidation.to_csv('merra_lrregValidation.csv')

