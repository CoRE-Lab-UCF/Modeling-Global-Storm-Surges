# -*- coding: utf-8 -*-
"""
Created on Mon Oct 26 09:44:15 2020

get the annual maximum bias time series


@author: Michael Tadesse
"""

bias = pd.DataFrame(columns=['year', 'value'])
years = dat['year'].unique()
for ii in years:
    currentYear = dat[dat['year'] == ii]
    df = pd.DataFrame([ii, abs(currentYear['bias']).max()]).T
    df.columns = ['year', 'value']
    bias = pd.concat([bias, df], axis = 0)
    print(bias)