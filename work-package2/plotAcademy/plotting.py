# -*- coding: utf-8 -*-
"""
Created on Wed Jan 22 10:29:29 2020

@author: Michael Tadesse
"""
import matplotlib.pyplot as plt
import matplotlib.lines as mlines
import seaborn as sns
import pandas as pd
import numpy as np

sns.set_context('notebook', font_scale= 2)

dat = pd.read_csv('modela_rel_rmse.csv', header=None) 

dat.columns = ['Model', 'Latitude', 'Relative RMSE', 'tg']

dat['Model'].replace(1, 'lrrs', inplace = True)
dat['Model'].replace(2, 'lrrslag', inplace = True)
dat['Model'].replace(3, 'rfrslag', inplace = True)


markers = {'M1': 'D', 'M2':'P', 'M3':'o'}
plt.figure(); sns.scatterplot(x = dat['Relative RMSE'], \
                              y = dat['Latitude'], hue='tg', \
                                  style = 'Model', s = 100, \
                                      markers=markers,data = dat, legend = False)

diamond = mlines.Line2D([], [], color = None, marker = 'D', \
                        linestyle = 'None',markersize = 13, \
                            label = 'M1', fillstyle = 'none')
pentagon = mlines.Line2D([], [], color = None, marker = 'P', \
                        linestyle = 'None', markersize = 13, \
                            label = 'M2', fillstyle = 'none')
circle = mlines.Line2D([], [], color = None, marker = 'o', \
                        linestyle = 'None', markersize = 13, \
                            label = 'M3', fillstyle = 'none')
    
plt.legend(handles = [diamond, pentagon, circle])

#add a fill on the figure
plt.axhspan(30, 80, xmin = 0, xmax = 1, color = 'darkgrey', alpha = 0.2)
plt.axhspan(-80, -30, xmin = 0, xmax = 1, color = 'darkgrey', alpha = 0.2)

plt.xlabel('Relative RMSE (%)')


