# -*- coding: utf-8 -*-
"""
Created on Tue Jun 23 14:45:47 2020

@author: Michael Tadesse
"""
import os
from functools import reduce
import pandas as pd

###########################################
#rename files or folders
###########################################
def renameFiles():
    for tg in os.listdir():
        charToRemove = ",-"
        
        for ii in charToRemove:
            newName = tg.replace(ii, "_")
        #now rename folder
        os.rename(tg, newName)
    print("it is finished!")
    
    
def pathChanger(data):
    """
    changes the extension of the files
    specify the name of the reanalysis 
    """
    for tg in range(0, len(dat)):
        if pd.isnull(dat['merraPath'][tg]):
            continue
        print(dat['merraPath'][tg])
        strToRemove = ['csv']
        
        for ii in strToRemove:
            newPath = dat['merraPath'][tg].replace(ii, "7z")
        dat['merraPath'][tg] = newPath

###################################################
#rename metadata csvs - when editing inside the csv 
###################################################
    
dir_in = os.chdir("E:\\03_20cr\\08_20cr_surge_reconstruction\\bestReconstruction\\metaData")
dat = pd.read_csv("20cr_modelValidationKFOLD.csv")

def renameMetaData():
    for ii in range(0, len(dat)):
        oldName = dat['tg'][ii]
        charToRemove = ",-"
        
        for jj in charToRemove:
            newName= oldName.replace(jj, "_")
        print(oldName, " ", newName)
        dat.iloc[ii, 1] = newName
        

renameMetaData()

dat.drop('Unnamed: 0', axis = 1, inplace = True)

dat.to_csv('20cr_Validation.csv')


###################################################
#remove extensions within csv files + add path
###################################################

#get files first 
os.chdir("E:\\webmap\\metadata")


twcr = pd.read_csv('20cr_Validation.csv')
era20c = pd.read_csv('era20c_Validation.csv')
eraint = pd.read_csv('eraint_Validation.csv')
merra = pd.read_csv('merra_Validation.csv')
erafive = pd.read_csv('erafiveRenamed.csv')

#dealign with extensions

extenstion = ['_glossdm_bodc', '_uhslc', '_jma', '_bodc', '_noaa',\
              '_med_refmar', '_pde', '_meds', '_noc', '_ieo', '_idromare',\
                  '_eseas', 'france_refmar', '_noc', '_smhi', '_bsh',\
                      '_fmi', '_rws', '_dmi', '_statkart', '_coastguard',\
                          '_itt', '_comune_venezia', '_johnhunter', '_university_zagreb']

#change reanalysis here
dat = erafive.copy()  
dat['path'] = 'nan'  

for ii in range(0, len(dat)):
    
    for ext in extenstion:

        if dat['tg'][ii].endswith(ext+".csv"):
            print(dat['tg'][ii],"----ENDS WITH---- [", ext, "]")
                                
            #split it
            new_name = dat['tg'][ii].split(ext+'.csv')[0] + str(".csv")
            
            #rename file
            dat.iloc[ii, 1] = new_name
            #change path location here
            dat.iloc[ii, 11] = "./erafive/"+new_name
            break
        
dat = dat[['tg', 'lon', 'lat', 'path']]

#save metadat as csv
dat.to_csv('erafiveMetadata.csv')
###############################################################################
#rename columns
twcr.columns = ['Unnamed: 0', 'tg', 'lon', 'lat', 'twcrPath']
era20c.columns = ['Unnamed: 0', 'tg', 'lonx', 'latx', 'era20cPath']
eraint.columns = ['Unnamed: 0', 'tg', 'lony', 'laty', 'eraintPath']
merra.columns = ['Unnamed: 0', 'tg', 'lonz', 'latz', 'merraPath']
erafive.columns = ['Unnamed: 0', 'tg', 'lona', 'lata', 'erafivePath']

###############################################################################
#merge all metadata files
df = [twcr, era20c, eraint, merra, erafive]

df_merged = reduce(lambda  left,right: pd.merge(left,right,on=['tg'],
                                            how='outer'), df)
df_merged = df_merged[['tg', 'lon', 'lat', 'twcrPath', 'era20cPath', \
                       'eraintPath', 'merraPath', 'erafivePath']]
    
#missing name for tide gauges
df_merged.iloc[842,3] = './20cr/vigo_ieo_spain.csv'
df_merged.iloc[842,4] = './era20c/vigo_ieo_spain.csv'
df_merged.iloc[842,5] = './eraint/vigo_ieo_spain.csv'
df_merged.iloc[842,6] = './merra/vigo_ieo_spain.csv' 
df_merged.iloc[842,7] = './erafive/vigo_ieo_spain.csv'    
   
    
    
df_merged.iloc[709,3] = './20cr/santander_ieo_spain.csv'
df_merged.iloc[709,4] = './era20c/santander_ieo_spain.csv'
df_merged.iloc[709,5] = './eraint/santander_ieo_spain.csv'
df_merged.iloc[709,6] = './merra/santander_ieo_spain.csv'
df_merged.iloc[709,7] = './erafive/santander_ieo_spain.csv'