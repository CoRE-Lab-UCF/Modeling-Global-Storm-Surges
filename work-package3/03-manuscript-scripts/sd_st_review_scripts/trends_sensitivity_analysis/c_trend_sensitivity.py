"""
Created on Sun Dec 19 12:34:00 2021
Modified on Mon Dec 20 07:39:00 2021

perform trend analysis sensitivity analysis  

@author: Michael Tadesse

"""

import os 
import pandas as pd
from datetime import datetime
import statsmodels.stats.stattools as stools
import statsmodels.api as sm



dir_home = "G:\\report\\year-3\\07-Fall-2020\\#3Paper\\data"\
            "\\trend-analysis\\data\\chosen_tgs_sensitivity\\percentiles\\99"
dir_out = "G:\\report\\year-3\\07-Fall-2020\\#3Paper\\data"\
            "\\trend-analysis\\data\\chosen_tgs_sensitivity\\trends"



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




def main(tg, min_window, data):
    """  
    tg: name of tide gauge
    min_window: minimum number of years for trend calucation 
    data: { obs, twcr, era20c }
    """
    
    os.chdir(dir_home)
    dat = pd.read_csv(tg)
    print(dat)

    # years run between start date : end_date - window 
    # these are the years you will be working with 
    years = list(range(int(dat['year'][0]), int(dat['year'][len(dat)-1] + 1 - min_window)))

    # create an empty dataframe 
    df = pd.DataFrame(columns = ['year', 'window', 'trend', 'pval'])

    for yr in years:
        
        # define max_window size for each year
        max_window = int(dat['year'][len(dat)-1] - yr + 1 )

        for wind in list(range(min_window, max_window + 1)):
            print(yr, wind)

            nowData = dat[(dat['year'] >= yr) & (dat['year'] < (yr + wind + 1))]

            # check 75% completeness
            if len(nowData) < 0.75*wind:
                trend = ''
                pval = ''
            else:
                trend, pval = computeTrend(nowData, data, 'HAC')

            newDf = pd.DataFrame([yr, wind, trend, pval]).T
            newDf.columns = ['year', 'window', 'trend', 'pval']

            df = pd.concat([df, newDf], axis = 0)


    os.chdir(dir_out)
    df.to_csv(tg.split('.csv')[0] + data + '.csv')


# run code
os.chdir(dir_home)
for tg in os.listdir():
    for data in [ 'obs', 'twcr', 'era20c' ]:
        print(tg, data)
        main(tg, 30, data)