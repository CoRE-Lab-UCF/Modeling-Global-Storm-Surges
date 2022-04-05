"""

Created on Sun Jan 16 13:16:00 2022
Modified on Fri Jan 21 12:16:00 2022

prepare G-20CR|G-E20C|G-Int|G-Merra|G-E5|G-EnsMean to match Obs time series  
Data is prepared with overlapping period but within 1980-2010
to match all recons and observation - just for Australian tgs

@author: Michael Getachew Tadesse

"""

import os 
import pandas as pd
from datetime import datetime
from functools import reduce


dir_home = "G:\\report\\year-3\\07-Fall-2020\\#3Paper\\data"\
            "\\trend-analysis\\data\\allSixTrends\\rawData\\"\
                    "australia_tgs\\dmax"
dir_twcr = "G:\\report\\year-3\\07-Fall-2020\\#3Paper\\data"\
                "\\trend-analysis\\data\\01-twcr\\01-postCPT"
dir_era20c = "G:\\report\\year-3\\07-Fall-2020\\#3Paper\\data"\
                "\\trend-analysis\\data\\02-era20c\\01-postCPT"
dir_eraint = "G:\\data\\allReconstructions\\03_erainterim"
dir_merra = "G:\\data\\allReconstructions\\04_merra"
dir_era5 = "G:\\data\\allReconstructions\\05_era5"
dir_ens = "G:\\report\\year-3\\07-Fall-2020\\#3Paper\\data\\"\
            "trend-analysis\\data\\ensemble_trends\\ensembleRecon"


dir_out = "G:\\report\\year-3\\07-Fall-2020\\#3Paper\\data"\
            "\\trend-analysis\\data\\allSevenTrends\\rawData\\"\
                    "australia_tgs\\dmax_merged"

def prepareData():
    """  
    
    """
    os.chdir(dir_home)
    tgList = os.listdir()

    count = 0
    for tg in tgList:
        print(tg)
        # check if file exists in post cpt folder and satellite era recons
        if (os.path.exists(dir_twcr + '\\{}'.format(tg))) & \
                (os.path.exists(dir_era20c + '\\{}'.format(tg))) & \
                    (os.path.exists(dir_eraint + '\\{}'.format(tg))) & \
                        (os.path.exists(dir_merra + '\\{}'.format(tg))) & \
                            (os.path.exists(dir_era5 + '\\{}'.format(tg))) & \
                                (os.path.exists(dir_ens + '\\{}'.format(tg))):
            count += 1
    
            # get observed surge
            os.chdir(dir_home)
            obs = pd.read_csv(tg)
            
            time_stamp = lambda x: (datetime.strptime(x, '%Y-%m-%d'))
            obs['date'] = pd.DataFrame(list(map(time_stamp, obs['date'])))
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

            
            # get eraint surge
            os.chdir(dir_eraint)
            eraint = pd.read_csv(tg)
            eraint['date'] = pd.to_datetime(eraint['date'])
            eraint = eraint[['date', 'surge_reconsturcted']]
            eraint.columns = ['date', 'eraint_surge']

            
            # get merra surge
            os.chdir(dir_merra)
            merra = pd.read_csv(tg)
            merra['date'] = pd.to_datetime(merra['date'])
            merra = merra[['date', 'surge_reconsturcted']]
            merra.columns = ['date', 'merra_surge']

            
            # get era5 surge
            os.chdir(dir_era5)
            era5 = pd.read_csv(tg)
            era5['date'] = pd.to_datetime(era5['date'])
            era5 = era5[['date', 'surge_reconsturcted']]
            era5.columns = ['date', 'era5_surge']

            
            # get G-EnsMean 
            os.chdir(dir_ens)
            ens_mean = pd.read_csv(tg)
            ens_mean['date'] = pd.to_datetime(ens_mean['date'])
            ens_mean = ens_mean[['date', 'ensMean']]
            ens_mean.columns = ['date', 'ensMean']


            # merge all three
            dfs = [obs, twcr, era20c, eraint, merra, era5, ens_mean]
            dat_merged = reduce(lambda left, right: pd.merge(left, right, on = 'date'), dfs)

            os.chdir(dir_out)
            dat_merged.to_csv(tg)


prepareData()