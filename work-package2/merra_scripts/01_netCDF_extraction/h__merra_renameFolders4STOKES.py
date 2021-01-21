# -*- coding: utf-8 -*-
"""
Created on Wed Jun 17 10:45:17 2020

MERRA - Folder renaming script

@author: Micheal Tadesse
"""
import os

os.chdir("\\lustre\\fs0\\home\\mtadesse\\merraLocalized")

#rename a folder
for file in os.listdir():
    fileStrings = file.split('-')[1:];
    fileName = fileStrings[0];
    for ii in range(1, len(fileStrings)):
        fileName = '-'.join([fileName, fileStrings[ii]]); 
    print(file, " --- ", fileName);
    
    #now rename folder
    os.rename(file, fileName)
    

