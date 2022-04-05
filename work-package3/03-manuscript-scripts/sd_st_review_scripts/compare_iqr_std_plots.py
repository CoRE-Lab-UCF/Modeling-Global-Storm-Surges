"""
Created on Mon Dec 13 10:46:00 2021

compare IQR and STD-DEV BCP plots

@author: Michael Tadesse

"""
import os 
import pandas as pd
import matplotlib.pyplot as plt

dir_std = "G:\\report\\year-3\\07-Fall-2020\\#3Paper\\data\\"\
            "changePointTimeSeries\\20crBCP"
dir_iqr = "G:\\report\\year-3\\07-Fall-2020\\#3Paper\\data\\"\
            "changePointTimeSeries\\additionalTest\\iqrBCP"


tg = "wellington_071a_new_zealand.csv"

os.chdir(dir_std)
stdBcp = pd.read_csv(tg)

os.chdir(dir_iqr)
iqrBcp = pd.read_csv(tg)

print(stdBcp)
print(iqrBcp)

plt.figure(figsize = (14,4))
plt.plot(stdBcp['year'], stdBcp['prob'], c = 'blue', label = "std-dev")
plt.plot(iqrBcp['year'], iqrBcp['prob'], c = 'red', label = "iqr")
plt.legend()
plt.grid()
plt.title(tg.split('.csv')[0])
plt.show()