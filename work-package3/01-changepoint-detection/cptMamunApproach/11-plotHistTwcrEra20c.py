#get libraries
import os 
import pandas as pd 
import matplotlib.pyplot as plt

dir_home = "G:\\report\\year-3\\07-Fall-2020\\#3Paper\\data\\"\
            "changePointTimeSeries\\mamun-cpt-approach\\comparison"

os.chdir(dir_home)

dat = pd.read_csv("twcrEra20cMerged.csv")

print(dat)

plt.figure(figsize=(8,4))
plt.hist(dat['year_twcr'], bins = 50, color = 'green', label="20-CR")
plt.hist(dat['year_era20c'], bins = 50, color = 'magenta', alpha = 0.5, label = "ERA-20C")
plt.xlabel("Changepoint Years")
plt.ylabel("No. Tide Gauges")
plt.legend()
plt.show()