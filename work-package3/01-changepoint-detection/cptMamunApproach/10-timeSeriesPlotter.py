#get libraries
import os 
import pandas as pd 
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from datetime import datetime

#define lambda functions 
time_stamp = lambda x: (datetime.strptime(x, '%Y-%m-%d %H:%M:%S'))
time_stamp_surge = lambda x: (datetime.strptime(x, '%Y-%m-%d'))

#change directory
os.chdir("G:\\report\\year-3\\07-Fall-2020\\#3Paper\\data\\"\
        "changePointTimeSeries\\mamun-cpt-approach\\obsSurge\\09-reconSurge\\01-astoria")


#load obs surge
obs = pd.read_csv("DailyMax.csv")
twcr = pd.read_csv("Twcr.csv")
era20c = pd.read_csv("Era20c.csv")

#change date format for plotting
obs['date'] = pd.DataFrame(list(map(time_stamp_surge, obs['days'])), 
                                        columns = ['date'])
twcr['date'] = pd.DataFrame(list(map(time_stamp, twcr['date'])), 
                                         columns = ['date'])
era20c['date'] = pd.DataFrame(list(map(time_stamp, era20c['date'])), 
                                         columns = ['date'])

#plot
plt.figure(figsize=(10, 4))
plt.plot(obs['date'], obs['surge'], color = "blue", 
                   label = "observation", lw = 2)
plt.plot(twcr['date'], twcr['surge_reconsturcted'], color = "green", 
                   label = "20-CR", lw = 2)
plt.plot(era20c['date'], era20c['surge_reconsturcted'], color = "magenta", 
                   label = "ERA-20C", lw = 2)
plt.legend()
plt.show()