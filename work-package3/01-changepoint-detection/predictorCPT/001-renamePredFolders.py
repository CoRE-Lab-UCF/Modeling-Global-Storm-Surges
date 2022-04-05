"""  
this function removes extensions from folders
to match the standard tide gauge names used
for GSSR

Created on Tue Apr 21 12:19:00 2021

@author: Michael Tadesse

"""

import os
from functools import reduce
import pandas as pd

dirHome = "F:\\02_era20C\\01_era20C_predictors"

os.chdir(dirHome)


def renameFolder():
    for tg in os.listdir():
        charToRemove = ",-"
        
        for ii in charToRemove:
            newName = tg.replace(ii, "_")
        #now rename folder
        os.rename(tg, newName)
    print("it is finished!")

renameFolder()


extenstion = ['_glossdm_bodc', '_uhslc', '_jma', '_bodc', '_noaa',\
              '_med_refmar', '_pde', '_meds', '_noc', '_ieo', '_idromare',\
                  '_eseas', 'france_refmar', '_noc', '_smhi', '_bsh',\
                      '_fmi', '_rws', '_dmi', '_statkart', '_coastguard',\
                          '_itt', '_comune_venezia', '_johnhunter', '_university_zagreb']
            

dat = os.listdir()

for ii in range(0, len(dat)):
    
    for ext in extenstion:

        if dat[ii].endswith(ext):
            print(dat[ii],"----ENDS WITH---- [", ext, "]")

            newName = dat[ii].replace(ext, "")
            break
        else:
            newName = dat[ii]
    os.rename(dat[ii], newName)
