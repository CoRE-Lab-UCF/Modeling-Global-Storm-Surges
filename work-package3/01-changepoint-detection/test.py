import os 
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt 
from datetime import datetime


dir_home = "G:\\report\\year-3\\07-Fall-2020\\#3Paper\\data\\"\
        "changePointTimeSeries\\mamun-cpt-approach\\twcr\\"\
                "001-tgsAnnualCorr\\merged"

os.chdir(dir_home)

dat = pd.read_csv("brest_Merged.csv")
time_stamp1 = lambda x: (datetime.strptime(x, '%Y-%m-%d'))
dat['date'] = pd.DataFrame(list(map(time_stamp1, dat['date'])))

print(dat)

plt.figure(figsize=(10, 4))
plt.plot(dat['date'], dat['surge'], label = 'obs', color = "blue")
plt.plot(dat['date'], dat['surge_reconsturcted'], label = 'recon', color = "red")
plt.legend()
plt.show()
