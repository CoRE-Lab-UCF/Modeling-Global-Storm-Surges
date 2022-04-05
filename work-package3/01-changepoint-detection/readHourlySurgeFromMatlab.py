# -*- coding: utf-8 -*-
"""
Created on Fri Nov 13 12:55:13 2020

Load .mat files to work on python

@author: mi292519
"""

from scipy.io import loadmat
import pandas as pd

dat = loadmat('fernandinaBeach.mat')

#read date and surge
dt = dat['dt']
surge = dat['Surge']

#get the date from the arrays
getDate = lambda x: x[0][0]
ferDate = pd.DataFrame(list(map(getDate, dt)))

#get surge from the arrays
getSurge = lambda x: x[0]

ferSurge = pd.DataFrame(list(map(getSurge, surge)))


#combine date and surge
ferDat = pd.concat([ferDate, ferSurge], axis = 1)
ferDat.columns = ['date', 'surge']

#save as csv
ferDat.to_csv("fernandina.csv")