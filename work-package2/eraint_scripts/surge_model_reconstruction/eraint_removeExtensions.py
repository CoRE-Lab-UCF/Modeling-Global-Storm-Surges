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
    
    dir_in = 'F:\\01_erainterim\\08_eraint_surge_reconstruction\\bestReconstruction\\surgeReconstructed'
    dir_out = 'F:\\01_erainterim\\08_eraint_surge_reconstruction\\bestReconstruction\\surgeReconstructed_new'


    os.chdir(dir_in)
    
    tg_list = os.listdir()
    extenstion = ['-glossdm-bodc', '-uhslc', '-jma', '-bodc', '-noaa',\
                  '-med-refmar', '-pde', '-meds', '-noc', '-ieo', '-idromare',\
                      '-eseas', 'france-refmar', '_noc', '-smhi', '-bsh',\
                          '-fmi', '-rws', '-dmi', '-statkart', '-coastguard',\
                              '-itt', '-comune_venezia', '-johnhunter', '-university_zagreb']
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
            

            

                
        
    
    
    
    
