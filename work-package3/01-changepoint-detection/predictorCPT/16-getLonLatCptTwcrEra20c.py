"""  
this script get the lon/lat for the cpt comparison file
"""

import os 
import pandas as pd 

dirHome = "G:\\report\\year-3\\07-Fall-2020\\#3Paper\\data\\"\
    "changePointTimeSeries\\mamun-cpt-approach\\era20c\\0001-predCPT\\cptSA"
dirLonLat = "G:\\data\\allReconstructions\\06_dmax_surge_georef"

os.chdir(dirHome )

dat = pd.read_csv("era20cVisual_Inspection_GSSRDB.csv")

dat['lon'] = 'nan'
dat['lat'] = 'nan'

for ii in range(len(dat)):
    print(dat['tg'][ii])

    os.chdir(dirLonLat)
    df = pd.read_csv(dat['tg'][ii])
    lon = df['lon'][0]
    lat = df['lat'][0]
    
    dat['lon'][ii] = lon
    dat['lat'][ii] = lat
    
os.chdir(dirHome)
dat.to_csv("era20cVisual_Inspection_GSSRDB_georef.csv")
