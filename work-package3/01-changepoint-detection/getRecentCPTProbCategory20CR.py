# -*- coding: utf-8 -*-
"""
Created on Mon Feb  1 09:28:19 2021

get most recent changepoin year  + probability category
caveat: check if you want to plot w/o p25

@author: Michael Tadesse
"""
import os
import pandas as pd

home = "D:\\OneDrive - Knights - University of Central"\
    " Florida\\UCF\\Projekt.28\\Report\\07-Fall-2020\\"\
        "#3Paper\\data\\changePointTimeSeries\\20crBCPProb"
os.chdir(home)

##################################################
dat = pd.read_csv('20crBCPProbNoP25.csv')
dat.drop('Unnamed: 0', axis = 1, inplace = True)
##################################################


#get the recent cpt year
#add +1 on the last index to include the last element
dat['recentCpt'] = dat.iloc[:,3:6].max(axis = 1)

#get probability category
dat['pCat'] = 'nan'
dat['pCat'] = dat.iloc[:, 3:6].idxmax(axis = 1)
        
#fill in NaN with 1900/1836
orgnYear = 1836;
dat['recentCpt'].fillna(orgnYear, inplace = True);

# #changed this to p<0.5 when I removed p25 from dat
dat['pCat'].fillna('p<0.5', inplace = True);

#changed this to p<0.5 when I removed p25 from dat
# dat['pCat'].fillna('p<0.25', inplace = True);


#save as csv
# dat.to_csv('20crRecentCPTNop25.csv')
dat.to_csv('20crRecentCPTNoP25.csv')