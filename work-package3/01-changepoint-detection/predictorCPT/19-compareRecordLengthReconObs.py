"""  
this script compares the record length for twcr/era20c with
observed daily max obs record length
"""

import os
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
#locate the file that basemap needs
os.environ["PROJ_LIB"] = "C:\\Users\\WahlInstall\\"\
    "Anaconda3\\Library\\share\\basemap"
from mpl_toolkits.basemap import Basemap


# get data 
dirDict = {
    "twcr":"G:\\report\\year-3\\07-Fall-2020\\#3Paper\\data\\"\
            "changePointTimeSeries\\mamun-cpt-approach\\twcr\\0001-predCPT\\cptSA",
    "era20c":"G:\\report\\year-3\\07-Fall-2020\\#3Paper\\data\\"\
            "changePointTimeSeries\\mamun-cpt-approach\\era20c\\0001-predCPT\\cptSA"
}

dirObs = "G:\\data\\allReconstructions\\06_dmax_surge_georef"

def compareRecord(recon):
    """  
    this function compares the reconstruction length 
    with observed surge length

    recon = {"twcr", "era20c"}

    """
    os.chdir(dirDict[recon])

    dat = pd.read_csv(recon + "SurgeLength.csv")

    dat['obsRecordLength'] = "nan"
    dat['numYearsGained'] = "nan"

    for ii in range(len(dat['tg'])):
        os.chdir(dirDict[recon])

        print(dat['tg'][ii])

        # get observed obs record length
        os.chdir(dirObs)

        obs = pd.read_csv(dat['tg'][ii])

        # print(len(obs))

        #remove duplicated obs rows
        obs.drop(obs[obs['ymd'].duplicated()].index, axis = 0, inplace = True)
        obs.reset_index(inplace = True)
        obs.drop('index', axis = 1, inplace = True)

        dat['obsRecordLength'][ii] = np.ceil(len(obs)/365)

        # calculate diff
        dat['numYearsGained'][ii] = dat['recordLength'][ii] - dat['obsRecordLength'][ii]

        print(dat['recordLength'][ii], "-", dat['obsRecordLength'][ii])

    # save it 
    os.chdir(dirDict[recon])
    dat.to_csv(recon+"RecordLengthComparison.csv")

compareRecord("era20c")

