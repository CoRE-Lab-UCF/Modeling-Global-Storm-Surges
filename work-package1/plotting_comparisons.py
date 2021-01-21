# -*- coding: utf-8 -*-
"""
Created on Tue Aug 13 11:12:50 2019
To plot comparisons between Model A and Model B
@author: Mike Tadesse

"""
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import seaborn as sns
import pandas as pd

#load first model_rs.csv from (F...\#1 - Paper\Review\source_files\comment64)

sns.set_context('notebook', font_scale=1.5)

#plotting all in one figure
mdl_rs = pd.read_csv('model_rs.csv')
mdl_rs.drop('Unnamed: 0', axis = 1, inplace=True)

#load mdlab first - change column names

mdlab = pd.concat([mdl_rs, mdlar], axis = 0)

mdf = pd.melt(mdlab, id_vars=['model'], value_vars=['corr', 'rmse', 'nse'])
plt.figure(figsize=(10,6), dpi= 200)
# myColor = ['blue', 'green', 'red']
# sns.set_palette(myColor)
sns.boxplot(x = 'model', y ='value', hue = 'variable',  data = mdf, palette="husl")
# corr_patch = mpatches.Patch(color='blue', label = 'Correlation')
# rmse_patch = mpatches.Patch(color='green', label = 'RMSE (m)')
# nse_patch = mpatches.Patch(color='red', label = 'NSE')
plt.legend(loc = 'lower left', ncol = 1)
plt.xlabel('Model Configuration', fontname = 'Helvetica')
plt.ylabel('Correlation/RMSE/NSE', fontname = 'Helvetica', color = 'black')
ax = plt.gca()
ax.set_xticklabels(['LR-RS', 'LR-RS-lag', 'RF-RS-lag', 'LR-AR', 'LR-AR-lag', 'RF-AR-lag'])
plt.savefig('Figure10_v2.svg') # save as SVG






#plotting correlation 
plt.figure(figsize=(10,6), dpi= 200)
sns.boxplot(x = 'model', y ='corr', data = mdl_rs, palette="husl")
plt.ylabel('Correlation Coefficient', fontname = 'Helvetica', color = 'black')
plt.xlabel('Model Configuration')
ax = plt.gca()
ax.set_xticklabels(['LR-RS', 'LR-RS-lag', 'RF-RS-lag'])
plt.savefig('modelRS_boxplot_corr.svg') # save as SVG


#best suited for RMSE plot
plt.figure(figsize=(10,6), dpi= 200)
sns.boxplot(x = 'model', y ='rmse', data = mdl_rs, palette="husl")
plt.ylabel('RMSE (m)')
plt.xlabel('Model Configuration')
ax = plt.gca()
ax.set_xticklabels(['LR-RS', 'LR-RS-lag', 'RF-RS-lag'])
ax.minorticks_on()
ax.xaxis.set_tick_params(which='minor', bottom=False)
axes = plt.axes()
axes.set_ylim([0, 0.4])
plt.savefig('modelRS_boxplot_rmse.svg') # save as SVG



#best suited for NSE plot
plt.figure(figsize=(10,6), dpi= 200)
sns.boxplot(x = 'model', y ='nse', data = mdl_rs, palette="husl")
plt.ylabel('NSE')
plt.xlabel('Model Configuration')
ax = plt.gca()
ax.set_xticklabels(['LR-RS', 'LR-RS-lag', 'RF-RS-lag'])
plt.savefig('modelRS_boxplot_nse.svg') # save as SVG



#plot histograms one on top of each other
plt.figure(figsize=(8,6));
plt.hist(ma_b['corra'])
plt.hist(ma_b['corrb'], alpha = 0.4)
axes = plt.axes()
axes.set_ylim([0, 200])
plt.xlabel('Correlation coefficients', fontsize = 28)
plt.legend(['Model A', 'Model B'],fontsize = 28)


#%% Load modelA spydata
sns.boxplot(data = m1_2_3A[['corr_m1a', 'corr_m2a', 'corr_m3a']])
plt.ylabel('Correlation coefficients', fontsize = 28)
ax = plt.gca()
ax.set_xticklabels(['M1A', 'M2A', 'M3A'], fontsize = 28)
plt.savefig('modelA_boxplot_corr.svg') # save as SVG


plt.figure(figsize=(8, 6))
sns.boxplot(data = m1_2_3A[['rmse_m1a', 'rmse_m2a', 'rmse_m3a']])
plt.ylabel('RMSE (m)')
ax = plt.gca()
ax.set_xticklabels(['M1A', 'M2A', 'M3A'])
ax.minorticks_on()
ax.xaxis.set_tick_params(which='minor', bottom=False)
axes = plt.axes()
axes.set_ylim([0, 0.4])
plt.savefig('modelA_boxplot_rmse.svg')


plt.figure(figsize=(8, 6))
sns.boxplot(data = m1_2_3A[['nse_m1a', 'nse_m2a', 'nse_m3a']])
plt.ylabel('NSE')
ax = plt.gca()
ax.set_xticklabels(['M1A', 'M2A', 'M3A'])
plt.savefig('modelA_boxplot_nse.svg')
