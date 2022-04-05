"""  
this script compares the reconSTD of the centennial
reconstructions with that of era5
"""
import os  
import pandas as pd 
import matplotlib.pyplot as plt

dirE5 = "G:\\report\\year-3\\07-Fall-2020\\#3Paper\\data\\"\
    "changePointTimeSeries\\mamun-cpt-approach\\era5\\annualSTD"
dirT = "G:\\report\\year-3\\07-Fall-2020\\#3Paper\\data\\changePointTimeSeries\\"\
    "20crSTD"
dirE2 = "G:\\report\\year-3\\07-Fall-2020\\#3Paper\\data\\changePointTimeSeries\\"\
    "era20cSTD"
dirO = "G:\\report\\year-3\\07-Fall-2020\\#3Paper\\data\\"\
        "changePointTimeSeries\\mamun-cpt-approach\\obsSurge\\01-annualSTD"

tg = "fremantle_012_australia.csv"

# era5
os.chdir(dirE5)
e5Recon = pd.read_csv(tg)

# era20c
os.chdir(dirE2)
e2Recon = pd.read_csv(tg)

# twcr
os.chdir(dirT)
tRecon = pd.read_csv(tg)

# obs
os.chdir(dirO)
oRecon = pd.read_csv(tg)



print(e5Recon)
print(e2Recon)
print(tRecon)
print(oRecon)

plt.figure(figsize = (10, 4))
plt.plot(e5Recon['year'], e5Recon['value'], label = "era5STD", lw = 2, color = "black")
plt.plot(e2Recon['year'], e2Recon['value'], label = "era20cSTD", lw = 2, color = "magenta")
plt.plot(tRecon['year'], tRecon['value'], label = "twcrSTD", lw = 2, color = "green")
plt.scatter(oRecon['year'], oRecon['value'], label = "obsSTD", lw = 1, color = "blue")
plt.ylabel("annual variability in m")
plt.grid(b=None, which='major', axis= 'both', linestyle='-')
plt.minorticks_on()
plt.grid(b=None, which='minor', linestyle='--', axis="both", alpha=0.4)
plt.legend()
plt.show()