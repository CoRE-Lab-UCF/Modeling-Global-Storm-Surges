# -*- coding: utf-8 -*-
"""
Created on Wed Jun 17 10:45:17 2020

MERRA - Folder renaming script

@author: Micheal Tadesse
"""
import os

dirNames = "/lustre/fs0/home/mtadesse/05_dmax_surge_georef"
dirIn = "/lustre/fs0/home/mtadesse/merraAllLagged"


#cd to the folder where surge names are kept
os.chdir(dirNames)
realNames = sorted(os.listdir())

#rename the lagged files
os.chdir(dirIn)
fakeNames = sorted(os.listdir())

for file in range(0, len(os.listdir())):
    print(fakeNames[file], " to ", realNames[file])
    
    #now rename folder
    os.rename(fakeNames[file], realNames[file])
    

