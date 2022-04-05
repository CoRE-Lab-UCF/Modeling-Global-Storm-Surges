"""
Created on Wed Dec 08 11:23:00 2021

get the interquartile range 

@author: Michael Tadesse

"""

import pandas as pd


def getAnnualIQR(recon):

    recon['date'] = pd.to_datetime(recon['date'])

    #extract year column
    getYear = lambda x: x.year
    recon['year'] = pd.DataFrame(list(map(getYear, recon['date'])))

    # print(recon)


    #get IQR    
    dat = recon.copy()

    iqr = pd.DataFrame(columns=['year', 'value'])
    years = dat['year'].unique()
    for jj in years:
        currentYear = dat[dat['year'] == jj]
        # print(currentYear)

        q3 = currentYear["surge_reconsturcted"].quantile(0.75)
        q1 = currentYear["surge_reconsturcted"].quantile(0.25)


        df = pd.DataFrame([jj, (q3-q1)]).T
        df.columns = ['year', 'value']
        
        iqr = pd.concat([iqr, df], axis = 0)
        # print(sd)
    
    return iqr

