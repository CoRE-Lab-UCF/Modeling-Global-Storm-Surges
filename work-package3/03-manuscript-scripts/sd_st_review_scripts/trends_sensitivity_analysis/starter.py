
"""

Created on Wed Dec 16 12:37:00 2021

brainstoring script for trends sensitivity analysis  

@author: Michael Tadesse

"""

import os 
import pandas as pd
from datetime import datetime


## Data preparation

# go to observed surge repository 
    # for each tide gauge check if `post-cpt` G-20CR and G-E20C exist 
        # prepare G-20CR and G-E20C to match exactly as observed surge 



os.chdir('G:\\report\\year-3\\07-Fall-2020\\#3Paper\\data\\trend-analysis\\data\\allSixTrends\\rawData')


df = pd.DataFrame(columns = ['tg', 'year'])

for tg in os.listdir():
     dat = pd.read_csv(tg)
     start_year = dat['date'][0]
     end_year = dat['date'][len(dat) - 1]
     newdf = pd.DataFrame([tg, start_year, end_year]).T
     newdf.columns = ['tg', 'start_year', 'end_year']
     df = pd.concat([df, newdf], axis = 0)

os.chdir("G:\\report\\year-3\\07-Fall-2020\\#3Paper\\data\\trend-analysis\\data\\test")
df.to_csv('allSixDatasets_years.csv')