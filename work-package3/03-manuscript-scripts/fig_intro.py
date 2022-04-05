"""

Created on Thu Feb 27 15:30:00 2022

plot G-20CR and G-E20C along with their annual 99th values 
also include observed surges

@author: Michael Getachew Tadesse

"""

import os 
import pandas as pd
import seaborn as sns
from datetime import datetime
import matplotlib.pyplot as plt


g20cr = "G:\\data\\allReconstructions\\01_20cr"
g20cr99 = "G:\\report\\year-3\\07-Fall-2020\\#3Paper\\"\
            "p28ThirdManuscript\\manuscript\\data\\percentiles\\g20cr\\99"
ge20c = "G:\\data\\allReconstructions\\02_era20c"
ge20c99 = "G:\\report\\year-3\\07-Fall-2020\\#3Paper\\"\
            "p28ThirdManuscript\\manuscript\\data\\percentiles\\ge20c\\99"


################################
# choose tide gauge
tg = "astoria,or_572a_usa.csv"
################################


# organize data

# G-20CR
os.chdir(g20cr)
dat_g20cr = pd.read_csv(tg)
dat_g20cr['date'] = pd.to_datetime(dat_g20cr['date'])
print(dat_g20cr)

# G-20CR 99th
os.chdir(g20cr99)
dat_g20cr99 = pd.read_csv(tg)
dat_g20cr99['year'] = pd.to_datetime(dat_g20cr99['year'], format = "%Y")
print(dat_g20cr99)

# G-E20C
os.chdir(ge20c)
dat_ge20c = pd.read_csv(tg)
dat_ge20c['date'] = pd.to_datetime(dat_ge20c['date'])
print(dat_ge20c)

# G-E20C 99th
os.chdir(ge20c99)
dat_ge20c99 = pd.read_csv(tg)
dat_ge20c99['year'] = pd.to_datetime(dat_ge20c99['year'], format = "%Y")
print(dat_ge20c99)



# plot 

sns.set_context('paper', font_scale = 1.5)

plt.figure(figsize=(16, 8))

# G-20CR
plt.plot(dat_g20cr['date'], dat_g20cr['surge_reconsturcted'], 
    label = "G-20CR [Daily Max]", lw = 1.0, color = "lightgreen")

# G-E20C
plt.plot(dat_ge20c['date'], dat_ge20c['surge_reconsturcted'], 
    label = "G-E20C [Daily Max]", lw = 1.0, color = "lightpink")

# percentiles
plt.plot(dat_g20cr99['year'], dat_g20cr99['value'], 
    label = "G-20CR [Annual 99th Percentile]", lw = 1.5, color = "darkgreen", 
            linestyle='--', marker='o', markersize = 5)

plt.plot(dat_ge20c99['year'], dat_ge20c99['value'], 
    label = "G-E20C [Annual 99th Percentile]", lw = 1.5, color = "magenta", 
            linestyle='--', marker='o', markersize = 5)



plt.ylabel("Storm Surge Height (m)")

plt.legend()


os.chdir("G:\\googleDrive\\p28\\dissertation\\defense")
plt.savefig("fig1_intro.svg", dpi = 300)
plt.show()



