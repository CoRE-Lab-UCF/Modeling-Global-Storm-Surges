"""  
this script plots cpt sensitivity analysis
"""

import os 
import pandas as pd
from functools import reduce
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import seaborn as sns
from datetime import datetime

dirHome = "G:\\report\\year-3\\07-Fall-2020\\#3Paper\\data\\changePointTimeSeries\\"\
    "mamun-cpt-approach\\era20c\\0001-predCPT\\cptSA"

os.chdir(dirHome)


dat = pd.read_csv("era20cCptSA.csv")

# melt dataframe
datMelt = dat.iloc[:,2:10].melt()
print(datMelt)

plt.figure(figsize = (10,5))
pal = {"p_5":"lightcoral", "p_10":"yellowgreen", 
        "p_15":"deepskyblue", "p_20":"violet", 
            "p_25":"aqua", "p_30":"greenyellow", 
                "p_40":"plum", "p_50":"burlywood"}
sns.boxplot(x = "variable", y = datMelt["value"], width = 0.6,
    data = datMelt, hue= "variable", dodge=False, palette=pal)
plt.axhline(y = 1950, color = "gray", ls = "--", lw = 0.7, label = "60 year Mark (1950)")

plt.ylabel("changepoint years")
plt.xlabel("cutoff probability")
plt.legend(ncol = 5, bbox_to_anchor=(0.1,0.99))
plt.savefig("era20cCPTSA.svg", dpi = 400)
plt.show()

# get data details
print("p_5 has {} tgs with 60+ years {}".format(len(dat[dat['p_5'] <= 1950]), len(dat[dat['p_5'] <= 1950])/320))
print("p_10 has {} tgs with 60+ years {}".format(len(dat[dat['p_10'] <= 1950]), len(dat[dat['p_10'] <= 1950])/320))
print("p_15 has {} tgs with 60+ years {}".format(len(dat[dat['p_15'] <= 1950]), len(dat[dat['p_15'] <= 1950])/320))
print("p_20 has {} tgs with 60+ years {}".format(len(dat[dat['p_20'] <= 1950]), len(dat[dat['p_20'] <= 1950])/320))
print("p_25 has {} tgs with 60+ years {}".format(len(dat[dat['p_25'] <= 1950]), len(dat[dat['p_25'] <= 1950])/320))
print("p_30 has {} tgs with 60+ years {}".format(len(dat[dat['p_30'] <= 1950]), len(dat[dat['p_30'] <= 1950])/320))
print("p_40 has {} tgs with 60+ years {}".format(len(dat[dat['p_40'] <= 1950]), len(dat[dat['p_40'] <= 1950])/320))
print("p_50 has {} tgs with 60+ years {}".format(len(dat[dat['p_50'] <= 1950]), len(dat[dat['p_50'] <= 1950])/320))