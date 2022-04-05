"""

Created on Thu Dec 16 12:47:00 2021

prepare G-20CR G-E20C to match Obs time series  

@author: Michael Tadesse

"""

import os 
import pandas as pd
from datetime import datetime
from functools import reduce


dir_home = "G:\\report\\year-3\\07-Fall-2020\\#3Paper\\data"\
                "\\trend-analysis\\data\\03-obsSurge\\data"
dir_twcr = "G:\\report\\year-3\\07-Fall-2020\\#3Paper\\data"\
                "\\trend-analysis\\data\\01-twcr\\01-postCPT"
dir_era20c = "G:\\report\\year-3\\07-Fall-2020\\#3Paper\\data"\
                "\\trend-analysis\\data\\02-era20c\\01-postCPT"
dir_out = "G:\\report\\year-3\\07-Fall-2020\\#3Paper\\data\\"\
                "trend-analysis\\data\\sensitivity_analysis"

def prepareData():
    """  
    
    """
    os.chdir(dir_home)
    tgList = os.listdir()

    count = 0
    for tg in tgList:
        print(tg)
        # check if file exists in post cpt folder
        if (os.path.exists(dir_twcr + '\\{}'.format(tg))) & \
                (os.path.exists(dir_era20c + '\\{}'.format(tg))):
            count += 1
    
            # get observed surge
            os.chdir(dir_home)
            obs = pd.read_csv(tg)
            
            time_stamp = lambda x: (datetime.strptime(x, '%Y-%m-%d'))
            obs['date'] = pd.DataFrame(list(map(time_stamp, obs['ymd'])))
            obs = obs[['date', 'lon',  'lat','surge']]


            # get twcr surge
            os.chdir(dir_twcr)
            twcr = pd.read_csv(tg)
            twcr['date'] = pd.to_datetime(twcr['date'])
            twcr = twcr[['date', 'surge_reconsturcted']]
            twcr.columns = ['date', 'twcr_surge']

            
            # get era20c surge
            os.chdir(dir_era20c)
            era20c = pd.read_csv(tg)
            era20c['date'] = pd.to_datetime(era20c['date'])
            era20c = era20c[['date', 'surge_reconsturcted']]
            era20c.columns = ['date', 'era20c_surge']


            # merge all three
            dfs = [obs, twcr, era20c]
            dat_merged = reduce(lambda left, right: pd.merge(left, right, on = 'date'), dfs)

            os.chdir(dir_out)
            dat_merged.to_csv(tg)


prepareData()