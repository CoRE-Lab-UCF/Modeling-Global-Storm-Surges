"""
Created on Sun Dec 19 12:34:00 2021
Modified on Mon Dec 27 11:07:00 2021
Modified on Fri Jan 21 11:59:00 2022

perform trend analysis for G-20CR|G-E20C|G-Int|G-Merra|G-E5|G-EnsMean  

@author: Michael Getachew Tadesse

"""

import os 
import pandas as pd
import statsmodels.api as sm
from datetime import datetime
import statsmodels.stats.stattools as stools



dir_home = "G:\\report\\year-3\\07-Fall-2020\\#3Paper\\data\\"\
            "trend-analysis\\data\\allSevenTrends\\percentiles\\99"
dir_out = "G:\\report\\year-3\\07-Fall-2020\\#3Paper\\data\\"\
            "trend-analysis\\data\\allSevenTrends\\trends"



def computeTrend(dat, data, ar):
    """ 
    implements simple linear regression 
    data : { obs, twcr, era20c } 
    """
    x = dat['year']
    y = dat[data]

    x2 = sm.add_constant(x)
    est = sm.OLS(y, x2)
    if ar == "HAC":
        lag = int(4*(len(dat)*0.01)**(2/9))
        # print("lag = ", lag)
        
        # adding heteroscedasticity-consistent standard errors
        est2 = est.fit(cov_type = 'HAC', cov_kwds={'maxlags':lag}) 
    else:
        est2 = est.fit() # default - without heteroscedasticity checking
    
    # print(est2.summary())


    return est2.params[1]*1000, est2.pvalues[1]




def main():
    """  """
    os.chdir(dir_home)

    # create an empty dataframe 
    df = pd.DataFrame(columns = ['tg', 'lon', 'lat', 'tobs', 't20cr', 'te20c', 
                                        'teint', 'tmer', 'te5', 'tens','pobs', 'p20cr', 
                                                'pe20c', 'peint', 'pmer', 'pe5', 'pens' ])

    for tg in os.listdir():

        dat = pd.read_csv(tg)

        # get lon+lat
        lon = dat['lon'].unique()[0]
        lat = dat['lat'].unique()[0]
       
        # check year starts @ 1980 and ends in 2010
        start_year = dat['year'][0]
        end_year = dat['year'][len(dat) - 1]
    
        # limit time between 1980 and 2010
        if (start_year != 1980) | (end_year != 2010):
            print(tg, "--","start/end year not fulfilled")
            continue

        # compute trends
        # check 75% completeness
        if len(dat) < 0.75*(2011 - 1980):
            print(tg, "--", '75 percent completion not fulfilled')
            continue

        tobs, pobs = computeTrend(dat, 'obs', 'HAC')
        t20cr, p20cr = computeTrend(dat, 'twcr', 'HAC')
        te20c, pe20c = computeTrend(dat, 'era20c', 'HAC')
        teint, peint = computeTrend(dat, 'eraint', 'HAC')
        tmer, pmer = computeTrend(dat, 'merra', 'HAC')
        te5, pe5 = computeTrend(dat, 'era5', 'HAC')
        tens, pens = computeTrend(dat, 'ensMean', 'HAC')
        
        newDf = pd.DataFrame( [tg, lon, lat, tobs, t20cr, te20c, teint, tmer, te5, tens,
                                pobs, p20cr, pe20c, peint, pmer, pe5, pens] ).T
        newDf.columns = ['tg', 'lon', 'lat', 'tobs', 't20cr', 'te20c', 'teint', 'tmer', 'te5',
                                            'tens','pobs', 'p20cr', 'pe20c', 
                                                    'peint', 'pmer', 'pe5', 'pens' ]
        
        df = pd.concat([df, newDf], axis = 0)
    
    # save data 
    os.chdir(dir_out)
    # df.to_csv('allSevenTrends_99th.csv')

    

# execute code
main()