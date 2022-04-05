"""  
this script finds common tgs for short twcr and era20c
"""

import os 
import pandas as pd

dirTwcr = "G:\\report\\year-3\\07-Fall-2020\\#3Paper\\data\\changePointTimeSeries"\
    "\\mamun-cpt-approach\\shortTwcr\\03-cptSA"
dirEra20c = "G:\\report\\year-3\\07-Fall-2020\\#3Paper\\data\\changePointTimeSeries"\
    "\\mamun-cpt-approach\\era20c\\0001-predCPT\\cptSA"
dirOut = "G:\\report\\year-3\\07-Fall-2020\\#3Paper\\data\\changePointTimeSeries\\"\
    "mamun-cpt-approach\\twcr_era20c_1900_2010"

os.chdir(dirTwcr)
twcr = pd.read_csv("twcrShortenedCptSA.csv")
twcr.columns = ['tg', 'p_5T', 'p_10T', 'p_15T', 'p_20T', 'p_25T', 'p_30T', 'p_40T', 'p_50T']


os.chdir(dirEra20c)
era20c = pd.read_csv("era20cCptSA.csv")
era20c.columns = ['tg', 'p_5E', 'p_10E', 'p_15E', 'p_20E', 'p_25E', 'p_30E', 'p_40E', 'p_50E', 'vi']

# merge dfs
dfMerged = pd.merge(twcr, era20c, on="tg", how = "inner")

os.chdir(dirOut)
dfMerged.to_csv("cptSAComparison.csv")