# -*- coding: utf-8 -*-
"""
Created on Wed Jul  8 10:27:43 2020

To plot reconstructions for a given tide gauge

@author: Michael Tadesse
"""

def plotter():
    tideGauge = input("type the name of the tide gauge: ")
    plotIt(tideGauge)

def plotIt(tg):
    """
    plot comparison of all surge reconstrructions
    for any given tide gauge
    
    tg: tide gauge name
    
    """
    #import packages
    import os
    import pandas as pd
    from datetime import datetime
    import matplotlib.pyplot as plt
    import seaborn as sns

        
        
    
    #define recon directories
    reconPath = {'twcr': 'D:\\data\\allReconstructions\\20cr',
                 'era20c': 'D:\\data\\allReconstructions\\era20c',
                 'erainterim': 'D:\\data\\allReconstructions\\erainterim',
                 'merra': 'D:\\data\\allReconstructions\\merra',
                 'obsSurge': 'D:\\data\\allReconstructions\\05_dmax_surge_georef'
                 }
    
    #prepare time for plotting
    time_stamp = lambda x: (datetime.strptime(x, '%Y-%m-%d %H:%M:%S'))

    
    #loop through the recon folders
    for recon in reconPath.keys():
        #load the recon csv
        if recon == 'twcr':   
            os.chdir(reconPath['twcr'])
            surgeTwcr = pd.read_csv(tg)
            surgeTwcr['date'] = pd.DataFrame(list(map(time_stamp, 
                                                      surgeTwcr['date'])), 
                                             columns = ['date'])
        elif recon == 'era20c':
            os.chdir(reconPath['era20c'])
            surgeEra20c = pd.read_csv(tg)
            surgeEra20c['date'] = pd.DataFrame(list(map(time_stamp, 
                                                      surgeEra20c['date'])), 
                                             columns = ['date'])
        elif recon == 'erainterim':
            os.chdir(reconPath['erainterim'])
            surgeEraint = pd.read_csv(tg)
            surgeEraint['date'] = pd.DataFrame(list(map(time_stamp, 
                                                      surgeEraint['date'])), 
                                             columns = ['date'])
        elif recon == 'merra':
            os.chdir(reconPath['merra'])
            surgeMerra = pd.read_csv(tg)
            surgeMerra['date'] = pd.DataFrame(list(map(time_stamp, 
                                                      surgeMerra['date'])), 
                                             columns = ['date'])
        elif recon == 'obsSurge':
            os.chdir(reconPath['obsSurge'])
            obsSurge = pd.read_csv(tg)
            time_str = lambda x: str(datetime.strptime(x, '%Y-%m-%d %H:%M:%S').strftime("%Y-%m-%d"))
            time_stamp_Surge = lambda x: (datetime.strptime(x, '%Y-%m-%d'))

            obsSurge['date'] = pd.DataFrame(list(map(time_str, 
                                                      obsSurge['date'])), 
                                             columns = ['date'])
            obsSurge['date'] = pd.DataFrame(list(map(time_stamp_Surge, 
                                                      obsSurge['date'])), 
                                             columns = ['date'])
    
    #start plotting
    sns.set_context('notebook', font_scale = 2)
    plt.figure(figsize=(20, 12))
    plt.plot(obsSurge['date'], obsSurge['surge'], 
             label = 'Observation', color = 'blue')
    plt.plot(surgeTwcr['date'], surgeTwcr['surge_reconsturcted'], 
             label = '20CR', color = 'green')
    plt.plot(surgeEra20c['date'], surgeEra20c['surge_reconsturcted'], 
             label = 'Era-20C', color = 'black')
    plt.plot(surgeEraint['date'], surgeEraint['surge_reconsturcted'], 
             label = 'Era-Int', color = 'brown')
    plt.plot(surgeMerra['date'], surgeMerra['surge_reconsturcted'], 
             label = 'MERRA', color = 'magenta')
    
    plt.title(tg.split('.csv')[0])
    plt.legend()