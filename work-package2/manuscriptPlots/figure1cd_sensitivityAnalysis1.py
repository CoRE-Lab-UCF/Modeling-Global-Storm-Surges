# -*- coding: utf-8 -*-
"""
Created on Mon Sep 14 17:53:27 2020

Figure 1c and 1d 

@author: Michael Tadesse
"""

import os 
import matplotlib.pyplot as plt 
import seaborn as sns
#get the grid_stat file from 
##"F:\01_erainterim\06_eraint_results\grid_size"

sns.set_context('notebook', font_scale = 2)

plt.figure(figsize = (10,6))
markers = {"10x10": "o", "8x8": "o", "6x6":'o', "4x4":'o', "3x3":'o', "2x2":'o', "1x1":'o'}
sns.scatterplot('time', 'avg_corr', style = 'grid_size', s = 200, hue = 'grid_size', data = dat)
plt.grid(alpha = 0.5)
plt.ylabel('Average Correlation')
plt.xlabel('Run-time (hrs.)')
plt.legend(markerscale = 2)

os.chdir("G:\\data\\p28DataDescriptor\\manuscriptFiles\\figures\\figure1")
plt.savefig('figure1c.svg', dpi = 400)


#figure 1d
plt.figure(figsize = (10,6))
markers = {"10x10": "o", "8x8": "o", "6x6":'o', "4x4":'o', "3x3":'o', "2x2":'o', "1x1":'o'}
sns.scatterplot('time', dat['avg_rmse']*100, style = 'grid_size', s = 200, hue = 'grid_size', data = dat)
plt.grid(alpha = 0.5)
plt.ylabel('Average RMSE (cm)')
plt.xlabel('Run-time (hrs.)')
plt.legend(markerscale = 2)

os.chdir("G:\\data\\p28DataDescriptor\\manuscriptFiles\\figures\\figure1")
plt.savefig('figure1d.svg', dpi = 400)