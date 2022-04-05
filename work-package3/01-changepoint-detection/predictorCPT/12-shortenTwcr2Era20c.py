"""  
this script shortens the longer 20-CR annual std data
to match that of era20c in length
"""

import os
import pandas as pd

dirDict = {
    "home" : "G:\\report\\year-3\\07-Fall-2020\\#3Paper\\data\\changePointTimeSeries\\"\
            "mamun-cpt-approach\\twcr\\0001-predCPT\\cptSA",
    "slp" : "G:\\report\\year-3\\07-Fall-2020\\#3Paper\\data\\changePointTimeSeries\\"\
            "mamun-cpt-approach\\twcr\\0001-predCPT\\slp\\annualSTD",
    "wnd_u" : "G:\\report\\year-3\\07-Fall-2020\\#3Paper\\data\\changePointTimeSeries\\"\
            "mamun-cpt-approach\\twcr\\0001-predCPT\\wnd_u\\annualSTD",
    "wnd_v" : "G:\\report\\year-3\\07-Fall-2020\\#3Paper\\data\\changePointTimeSeries\\"\
            "mamun-cpt-approach\\twcr\\0001-predCPT\\wnd_v\\annualSTD",
    "recon" : "G:\\report\\year-3\\07-Fall-2020\\#3Paper\\data\\changePointTimeSeries\\"\
            "20crSTD",
    "out" : "G:\\report\\year-3\\07-Fall-2020\\#3Paper\\data\\changePointTimeSeries\\"\
            "mamun-cpt-approach\\shortTwcr"
}


def shortenTwcr():
    """  
    pred: predictor time series
    """
    os.chdir(dirDict["home"])

    # get the list of twcr tgs
    tgList = pd.read_csv("twcrVisual_Inspection_csv_v2.csv")['tg']

    for tg in tgList:

        print(tg)

        # read slp data
        os.chdir(dirDict["slp"])
        dat = pd.read_csv(tg)
        dat = dat[(dat['year'] >= 1900) & (dat['year'] <= 2010)]
        
        # save new csv
        os.chdir(dirDict["out"])
        try:
            os.makedirs("slp")
            os.chdir("slp")
            dat.to_csv(tg)    
        except FileExistsError:
            os.chdir("slp")
            dat.to_csv(tg)
        

        # read wnd_u data
        os.chdir(dirDict["wnd_u"])
        dat = pd.read_csv(tg)
        dat = dat[(dat['year'] >= 1900) & (dat['year'] <= 2010)]
        
        # save new csv
        os.chdir(dirDict["out"])
        try:
            os.makedirs("wnd_u")
            os.chdir("wnd_u")
            dat.to_csv(tg)    
        except FileExistsError:
            os.chdir("wnd_u")
            dat.to_csv(tg)
        
        
        # read wnd_v data
        os.chdir(dirDict["wnd_v"])
        dat = pd.read_csv(tg)
        dat = dat[(dat['year'] >= 1900) & (dat['year'] <= 2010)]
        
        # save new csv
        os.chdir(dirDict["out"])
        try:
            os.makedirs("wnd_v")
            os.chdir("wnd_v")
            dat.to_csv(tg)    
        except FileExistsError:
            os.chdir("wnd_v")
            dat.to_csv(tg)
        

        # read recon data
        os.chdir(dirDict["recon"])
        dat = pd.read_csv(tg)
        dat = dat[(dat['year'] >= 1900) & (dat['year'] <= 2010)]
        
        # save new csv
        os.chdir(dirDict["out"])
        try:
            os.makedirs("recon")
            os.chdir("recon")
            dat.to_csv(tg)    
        except FileExistsError:
            os.chdir("recon")
            dat.to_csv(tg)
        
        
shortenTwcr()