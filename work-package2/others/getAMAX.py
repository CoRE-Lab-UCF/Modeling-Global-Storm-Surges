# -*- coding: utf-8 -*-
"""
Created on Fri Jun  5 11:18:43 2020

Get annual maximum surge time series

@author: Michael Tadesse
"""
#import packages
import os
import pandas as pd


#define directories
dir_in = 'F:\\OneDrive - Knights - University of Central Florida\\UCF\Projekt.28\\Report\\05-Spring-2020\\#2 - Paper\\data\\erainterim\\01_eraInterim\\surgeReconstructed'
csv_path = 'F:\\OneDrive - Knights - University of Central Florida\\UCF\Projekt.28\\Report\\05-Spring-2020\\#2 - Paper\\data\\erainterim\\01_eraInterim\\amaxSurge'

#load files first
os.chdir(dir_in)

#looping through tgs
for tg in os.listdir():
    #read individual csv files
    dat = pd.read_csv(tg)
    dat.drop('Unnamed: 0', axis = 1, inplace = True)


    #get the year part
    getYear = lambda x: x.split('-')[0]
    dat['year'] = pd.DataFrame(list(map(getYear, dat['date'])))
    
    
    #looping thorough the years to extract amax
    firstTry = True
    for yr in dat['year'].unique():
        print(yr)
        
        currentYearData = dat[dat['year'] == yr]
        currentAmax =  currentYearData['surge_reconsturcted'].max()
        
        #find the row where amax is located
        amax = currentYearData[currentYearData['surge_reconsturcted'] == currentAmax]
        
        #reorder columns
        amax = amax.reindex(['lon', 'lat', 'year', 'surge_reconsturcted', \
                      'pred_int_lower', 'pred_int_upper', 'date'], axis = 1)
        
        if firstTry:
            annualMax = amax
            firstTry = False
    
        else:
            annualMax = pd.concat([annualMax, amax], axis = 0, sort= False)
        
        annualMax.reset_index(inplace = True)
        annualMax.drop(['index','date'], axis = 1, inplace = True)
    
    #save it as csv
    os.chdir(csv_path)
    annualMax.to_csv(tg)
    os.chdir(dir_in)

    

    
    