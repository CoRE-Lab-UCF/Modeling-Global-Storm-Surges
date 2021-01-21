# -*- coding: utf-8 -*-
"""
Created on Thu Apr  9 09:06:30 2020

Loading Predictor importance correlation data
Visualizing it

@author: Michael Tadesse
"""

import os 
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

dir_in = 'F:\\OneDrive - Knights - University of Central Florida\\UCF\\Projekt.28\\Report\\05-Spring-2020\\#2 - Paper\\data\\eraint_pred_surge_corr'
# dir_out = 
#cd to the pred_surge_corr directory
os.chdir(dir_in)

#looping through TGs
corr = pd.DataFrame(columns = ['prcp', 'slp', 'wnd_u', 'wnd_v', 'sst'])
for tg in range(len(os.listdir())):
    print(tg)
    
    tg_name = os.listdir()[tg]
    
    new_name = tg_name.split('.csv')[0]
    
    
    #load csv
    dat = pd.read_csv(tg_name)
    dat.set_index('Unnamed: 0', inplace = True)
    mean_corr = pd.DataFrame(dat.loc['mean']).T
    mean_corr['tg'] = new_name
    mean_corr.reset_index(inplace = True)
    mean_corr.drop('index', axis = 1, inplace = True)
    mean_corr.set_index('tg', inplace = True)
    mean_corr['lon'], mean_corr['lat'] = dat.loc['lon'].unique(), dat.loc['lat'].unique()
    corr = pd.concat([corr, mean_corr], axis = 0)
    

#visualization
sns.set_context('notebook', font_scale=2)
plt.figure()
sns.set_palette("Paired")
sns.boxplot(data = corr.iloc[:, 2:])
plt.ylabel('Correlation')
plt.title('Median Correlation of ERA-Interim Predictors - 10X10 grid [196 TGs]')
    

#tropical regions
corr_trop = corr[(corr['lat'] < 30) & (corr['lat'] > -30)]
plt.figure()
sns.set_palette("Paired")
sns.boxplot(data = corr_trop.iloc[:, 2:])
plt.ylabel('Correlation')
plt.title('Median Correlation of ERA-Interim Predictors - 10X10 grid [Tropical Regions Only]')
  

#extratropical regions
corr_extrop = corr[(corr['lat'] > 30) | (corr['lat'] < -30)]
plt.figure()
sns.set_palette("bright")
sns.boxplot(data = corr_extrop.iloc[:, 2:])
plt.ylabel('Correlation')
plt.title('Median Correlation of ERA-Interim Predictors - 10X10 grid [Extratropical Regions Only]')
 






