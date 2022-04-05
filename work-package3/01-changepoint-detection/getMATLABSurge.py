# -*- coding: utf-8 -*-
"""
Created on Fri Oct 30 09:10:29 2020

script to convert .mat surge files
to csv

@author: Michael Tadesse
"""
import scipy.io as sio
import pandas as pd

tg = 'boston.mat'

dat = sio.loadmat(tg)

#get time
time = dat['dt']

getTime = lambda x: x[0][0] 

dt = pd.DataFrame(list(map(getTime, time)))

#get surge

surge = dat['Surge']

getSurge = lambda x: x[0]

surge = pd.DataFrame(list(map(getSurge, surge)))

#concatenate time and surge

surgeDat = pd.concat([dt, surge], axis = 1)
surgeDat.columns = ['date', 'surge']

#save csv
saveName = tg.split('.mat')[0] + '.csv'

surgeDat.to_csv(saveName)