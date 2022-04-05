"""
Created on Wed Dec 08 11:23:00 2021

plot time series

@author: Michael Tadesse

"""
import pandas as pd
import matplotlib.pyplot as plt

def plotTimeSeries(dat, tg, type):
    """  
    o: for original time seres
    i: for interquartile range time series
    s: for annual std time series
    """

    plt.figure(figsize = (16,4))

    if type == 's':
        plt.plot(dat['year'], dat['value'], 'red')
        plt.ylabel('Annual STD (m)')
        plt.title(tg.split('.csv')[0])
    elif type == 'o':
        dat['date'] = pd.to_datetime(dat['date'])
        plt.plot(dat['date'], dat['surge_reconsturcted'], 'blue')
        plt.ylabel('Daily Maximum Surge (m)')
        plt.title(tg.split('.csv')[0])
    elif type == 'i':
        plt.plot(dat['year'], dat['value'], 'olive')
        plt.ylabel('Annual Interquartile Range (m)')
        plt.title(tg.split('.csv')[0])

    plt.show()
