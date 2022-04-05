# -*- coding: utf-8 -*-
"""
Created on Tue Jan 26 16:35:44 2021

Get BCP changepoint results for all tgs

@author: Michael Tadesse
"""
import os 
import pandas as pd

"""
p25: 0.25 <= p < 0.5
p50: 0.5 <= p < 0.75
p75: 0.75 <= p < 1.0

the most recent year is picked for each probability range


"""

home = "D:\\OneDrive - Knights - University of Central Florida\\UCF\\Projekt.28\\Report\\07-Fall-2020\\#3Paper\\data\\changePointTimeSeries\\20crBCP"
out = "D:\\OneDrive - Knights - University of Central Florida\\UCF\\Projekt.28\\Report\\07-Fall-2020\\#3Paper\\data\\changePointTimeSeries\\20crBCPProb"

os.chdir(home);
tgList = os.listdir();

#create an empty dataframe
df = pd.DataFrame(columns=['tg','p25','p50','p75'])

for tg in tgList:
    print(tg)
    dat = pd.read_csv(tg)
    
    try:
        p25 = dat[(dat['prob'] >= 0.25) & (dat['prob'] < 0.5)].iloc[-1,:].year;
    except IndexError:
        p25 = 'nan';
        
    try:
        p50 = dat[(dat['prob'] >= 0.50) & (dat['prob'] < 0.75)].iloc[-1,:].year;
    except IndexError:
        p50 = 'nan';
        
    try:
        p75 = dat[(dat['prob'] >= 0.75) & (dat['prob'] <= 1.0)].iloc[-1,:].year;
    except IndexError:
        p75 = 'nan';
        
    
    ##remove .csv extensions
    tgName = tg.split('.csv')[0]
    
    newDf = pd.DataFrame([tgName, p25, p50, p75]).T;
    newDf.columns = ['tg', 'p25', 'p50', 'p75'];
    
    df = pd.concat([df, newDf], axis = 0)
    

#write to csv
os.chdir(out)
df.to_csv('20crBCPProb.csv')
    


#get lon and lat
os.chdir("H:\\webmap\\metadata")
datGeo = pd.read_csv("allMetadataV7.csv")
test = datGeo[['tg','lon', 'lat']]
newDatGeo = pd.merge(df, test, on='tg', how='left')
newDatGeo = newDatGeo[['tg', 'lon', 'lat', 'p25', 'p50', 'p75']]
os.chdir(out)
newDatGeo.to_csv('20crBCPProbv2.csv')
    


    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    