# -*- coding: utf-8 -*-
"""
Created on Mon Sep  7 16:17:30 2020

To concatenate validation csvs


@author: Michael Tadesse
"""

import os 
import pandas as pd

dir_in = "G:\\05_era5\\08_era5_surge_reconstruction\\mlr\\eraFiveMLRValidation"

os.chdir(dir_in)

first = True
for file in os.listdir():
    print(file)
    dat = pd.read_csv(file)
    dat.drop('Unnamed: 0', axis = 1, inplace = True)
    if first:
        df = dat
        first = False
    else:
        df = pd.concat([df, dat], axis = 0)

df = df.sort_values('tg')
df.reset_index(inplace = True)
df.drop('index', axis = 1, inplace = True)

df.to_csv('erafiveMLRValidation.csv')