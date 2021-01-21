# -*- coding: utf-8 -*-
"""
Created on Mon Sep 28 11:52:48 2020

@author: Michael Tadesse
"""


import os 
import pandas as pd

dir_in = "/lustre/fs0/home/mtadesse/eraFiveConcat"

os.chdir(dir_in)
tgList = os.listdir()


x = 65
y = 66

#looping through individual tide gauges
for ii in range(x, y):
    os.chdir(tgList[ii])
    
    print(tgList[ii])
    
    uwnd = pd.read_csv('wnd_u.csv')
    vwnd = pd.read_csv('wnd_v.csv')
    
    #check sizes of uwnd and vwnd
    if uwnd.shape == vwnd.shape:
        print("all good!")
    else:
        print("sizes not equal")
        
    uwnd.drop(['Unnamed: 0', 'Unnamed: 0.1'], axis = 1, inplace = True)
    vwnd.drop(['Unnamed: 0', 'Unnamed: 0.1'], axis = 1, inplace = True)
    
    #sort by date
    uwnd = uwnd.sort_values(by = 'date')
    vwnd = vwnd.sort_values(by = 'date')
    
    #reset indices
    uwnd.reset_index(inplace = True)
    vwnd.reset_index(inplace = True)
    
    uwnd.drop(['index'], axis = 1, inplace = True)
    vwnd.drop(['index'], axis = 1, inplace = True)
    
    #get squares of uwnd and vwnd
    uSquare = uwnd.iloc[:, 1:]**2
    vSquare = vwnd.iloc[:, 1:]**2
    
    #sum and take square root
    wndResultant = (uSquare + vSquare)**0.5
    wndResultant = pd.concat([pd.DataFrame(uwnd['date']), wndResultant], axis = 1)
    
    #save file
    wndResultant.to_csv("wndRest.csv")
    os.chdir(dir_in)
