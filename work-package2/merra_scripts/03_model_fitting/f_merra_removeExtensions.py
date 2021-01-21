# -*- coding: utf-8 -*-
"""
Created on Mon May 18 10:39:37 2020

This program removes the filename extensions 
from surge reconstruction files

@author: Michael Tadesse
"""

def removeExtension():
    """
    removes file extensions
    """
    
    import os    
    
    dir_in = 'G:\\05_era5\\kikoStuff\\05_dmax_surge_georef'
    dir_out = 'G:\\05_era5\\kikoStuff\\dmaxRenamed'


    os.chdir(dir_in)
    
    tg_list = os.listdir()
    extenstion = ['_glossdm_bodc', '_uhslc', '_jma', '_bodc', '_noaa',\
                  '_med_refmar', '_pde', '_meds', '_noc', '_ieo', '_idromare',\
                      '_eseas', 'france_refmar', '_noc', '_smhi', '_bsh',\
                          '_fmi', '_rws', '_dmi', '_statkart', '_coastguard',\
                              '_itt', '_comune_venezia', '_johnhunter', '_university_zagreb']
    for tg in tg_list:
        
        source = os.path.join(os.path.abspath(os.getcwd()), tg)

        for ext in extenstion:

            if tg.endswith(ext+".csv"):
                print(tg,"----ENDS WITH---- [", ext, "]")
                                    
                #split it
                new_name = tg.split(ext+'.csv')[0] + str(".csv")
                destination = os.path.join(dir_out, new_name)
                
                #rename file
                os.rename(source, destination)
                os.chdir(dir_in)
                break
            

            

                
        
    
    
    
    
