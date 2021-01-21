# -*- coding: utf-8 -*-
"""
Created on Mon Feb 10 10:19:16 2020
Figure 8 plots - Predictor Importance
@author: Michael Tadesse
"""
import os 
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
file:///F:/OneDrive - Knights - University of Central Florida/UCF/Projekt.28/Report/Spring 2019/%231 - Paper/Review/source_files/comment70/Figure8_plot.py
#load predictor importance csv files
os.chdir('F:\\OneDrive - Knights - University of Central Florida\\Daten\\MLR\\Model_2\\04_01_2019\\M2_Results')
lrrslag = pd.read_csv('predictor_importance_md2A.csv')

lrrslag['predictor'] = '-'

for ii in range(0,len(lrrslag)):
    if lrrslag['first'][ii] == 'pc_sst':
        lrrslag['predictor'][ii] = 'SST'
    elif lrrslag['first'][ii].startswith('pc_g'):
        lrrslag['predictor'][ii] = 'GPCP'
    elif lrrslag['first'][ii].startswith('pc_u'):
        lrrslag['predictor'][ii] = 'UWND'
    elif lrrslag['first'][ii].startswith('pc_v'):
        lrrslag['predictor'][ii] = 'VWND'
    elif lrrslag['first'][ii].startswith('pc_s'):
        lrrslag['predictor'][ii] = 'SLP'
#------------------------------------------------------------------------------        
os.chdir('F:\\OneDrive - Knights - University of Central Florida\\Daten\\MLR\\Model_3\\04_04_2019\\M3_Results')    
rfrslag = pd.read_csv('predictor_importance_m3A.csv')

rfrslag['predictor'] = '-'

for ii in range(0,len(rfrslag)):
    if rfrslag['imprt3'][ii] == 'pc_sst':
        rfrslag['predictor'][ii] = 'SST'
    elif rfrslag['imprt3'][ii].startswith('pc_g'):
        rfrslag['predictor'][ii] = 'GPCP'
    elif rfrslag['imprt3'][ii].startswith('pc_u'):
        rfrslag['predictor'][ii] = 'UWND'
    elif rfrslag['imprt3'][ii].startswith('pc_v'):
        rfrslag['predictor'][ii] = 'VWND'
    elif rfrslag['imprt3'][ii].startswith('pc_s'):
        rfrslag['predictor'][ii] = 'SLP'
#------------------------------------------------------------------------------        

lr_import = lrrslag['predictor'].value_counts().reset_index() 
lr_import['predictor'] = lr_import['predictor']*100/732
rf_import = rfrslag['predictor'].value_counts().reset_index()
rf_import['predictor'] = rf_import['predictor']*100/731


pred_import = pd.merge(lr_import, rf_import, how = 'inner', on = 'index')
pred_import.columns = ['predictors', 'Linear Regression', 'Random Forest']
mdf = pd.melt(pred_import, id_vars=['predictors'], value_vars=['Linear Regression', 'Random Forest'])
mdf.columns = ['predictors', 'Model', 'value']

#plotting
font = {'family': 'Helvetica',
        'color':  'black',
        'weight': 'normal',
        'size': 30,
        }

sns.barplot(x = 'predictors', y = 'value', hue = 'Model', data = mdf, palette = 'bright')
plt.xticks(fontsize=20)
plt.yticks(fontsize=20)
plt.xlabel('Predictors', fontdict  = font)
plt.ylabel('Percentage of Tide Gauges', fontdict = font)

plt.savefig('lrrs_lag_pred_import.svg') # save as SVG

#%% rfrs-lag
#load predictor importance csv files


