import os
import pandas as pd

dirHome = "G:\\report\\year-3\\07-Fall-2020\\#3Paper\\data\\changePointTimeSeries"\
        "\\mamun-cpt-approach\\era20c\\0001-predCPT\\wnd_v\\rawPred"
dirOut = "G:\\report\\year-3\\07-Fall-2020\\#3Paper\\data\\changePointTimeSeries\\"\
        "mamun-cpt-approach\\era20c\\0001-predCPT\\wnd_v\\meanPred"

os.chdir(dirHome)

predList = os.listdir()

# print(predList)

for pred in predList:

    os.chdir(dirHome)

    print(pred)

    dat = pd.read_csv(pred)

    dat.drop(['Unnamed: 0', 'Unnamed: 0.1'], axis = 1, inplace = True)

    dat['mean'] = dat.iloc[:, 1: dat.shape[1]].mean(axis = 1)

    dat = dat[['date', 'mean']]

    # saveName = pred.split('.csv')[0] + "Mean.csv"

    os.chdir(dirOut)

    dat.to_csv(pred)
