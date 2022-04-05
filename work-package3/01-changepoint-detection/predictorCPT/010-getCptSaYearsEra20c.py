"""  
this script picks the year for each probability value - era20c
"""

import os 
import pandas as pd

dirHome = "G:\\report\\year-3\\07-Fall-2020\\#3Paper\\data\\changePointTimeSeries\\"\
    "mamun-cpt-approach\\era20c\\0001-predCPT\\cptProbs"

dirOut = "G:\\report\\year-3\\07-Fall-2020\\#3Paper\\data\\changePointTimeSeries\\"\
    "mamun-cpt-approach\\era20c\\0001-predCPT\\cptSA"

os.chdir(dirHome)
tgList = os.listdir()

# create an empty dataframe
cpt = pd.DataFrame(
        columns = ['tg', 'p_5', 'p_10', 'p_15', 'p_20', 'p_25', 'p_30', 'p_40', 'p_50'])

for tg in tgList:
    print(tg)
    dat = pd.read_csv(tg)

    y_5 = dat[dat['p_5'] == True].year.tolist()
    y_10 = dat[dat['p_10'] == True].year.tolist()
    y_15 = dat[dat['p_15'] == True].year.tolist()
    y_20 = dat[dat['p_20'] == True].year.tolist()
    y_25 = dat[dat['p_25'] == True].year.tolist()
    y_30 = dat[dat['p_30'] == True].year.tolist()
    y_40 = dat[dat['p_40'] == True].year.tolist()
    y_50 = dat[dat['p_50'] == True].year.tolist()
    
    # selecting the most recent cpt
    if y_5:
        y_5 = y_5[len(y_5)-1]
    else: 
        y_5 = '1900'

    if y_10:
        y_10 = y_10[len(y_10)-1]
    else: 
        y_10 = '1900'

    if y_15:
        y_15 = y_15[len(y_15)-1]
    else: 
        y_15 = '1900'

    if y_20:
        y_20 = y_20[len(y_20)-1]
    else: 
        y_20 = '1900'

    if y_25:
        y_25 = y_25[len(y_25)-1]
    else: 
        y_25 = '1900'

    if y_30:
        y_30 = y_30[len(y_30)-1]
    else: 
        y_30 = '1900'

    if y_40:
        y_40 = y_40[len(y_40)-1]
    else: 
        y_40 = '1900'

    if y_50:
        y_50 = y_50[len(y_50)-1]
    else: 
        y_50 = '1900'


    newDf = pd.DataFrame([tg, y_5, y_10, y_15, y_20, y_25, y_30, y_40, y_50]).T
    newDf.columns = ['tg', 'p_5', 'p_10', 'p_15', 'p_20', 'p_25', 'p_30', 'p_40', 'p_50']

    # concat to original dataframe
    cpt = pd.concat([cpt, newDf], axis = 0)

os.chdir(dirOut)
cpt.to_csv("era20cCptSA.csv")
    