"""  
this script combines all CPTS {pred and recon} of a tide gauge
"""

import os 
import pandas as pd
from functools import reduce

# cpt directories
dirBcpSlp = "G:\\report\\year-3\\07-Fall-2020\\#3Paper\\data\\changePointTimeSeries\\"\
    "mamun-cpt-approach\\era20c\\0001-predCPT\\slp\\originalBCP"
dirBcpUwnd = "G:\\report\\year-3\\07-Fall-2020\\#3Paper\\data\\changePointTimeSeries\\"\
    "mamun-cpt-approach\\era20c\\0001-predCPT\\wnd_u\\originalBCP"
dirBcpVwnd = "G:\\report\\year-3\\07-Fall-2020\\#3Paper\\data\\changePointTimeSeries\\"\
    "mamun-cpt-approach\\era20c\\0001-predCPT\\wnd_v\\originalBCP"
dirBcpRecon = "G:\\report\\year-3\\07-Fall-2020\\#3Paper\\data\\changePointTimeSeries\\"\
    "era20cBCP"
dirOut = "G:\\report\\year-3\\07-Fall-2020\\#3Paper\\data\\changePointTimeSeries\\"\
    "mamun-cpt-approach\\era20c\\0001-predCPT\\combinedBCP"

os.chdir(dirBcpSlp)

tgList = os.listdir()

for tg in tgList:

    os.chdir(dirBcpSlp)

    print(tg)

    slp = pd.read_csv(tg)
    slp = slp[['year', 'prob']]
    slp.columns = ['year', 'p_slp']

    os.chdir(dirBcpUwnd)
    uwnd = pd.read_csv(tg)
    uwnd = uwnd[['year', 'prob']]
    uwnd.columns = ['year', 'p_u']

    os.chdir(dirBcpVwnd)
    vwnd = pd.read_csv(tg)
    vwnd = vwnd[['year', 'prob']]
    vwnd.columns = ['year', 'p_v']

    os.chdir(dirBcpRecon)
    recon = pd.read_csv(tg)
    recon = recon[['year', 'prob']]
    recon.columns = ['year', 'p_recon']

    # merge all of them
    dfCompiled = [slp, uwnd, vwnd, recon]    
    dat = reduce(lambda left, right: \
        pd.merge(left, right, on = ['year'], how="outer"), dfCompiled)

    print(dat)

    os.chdir(dirOut)
    dat.to_csv(tg)



    
