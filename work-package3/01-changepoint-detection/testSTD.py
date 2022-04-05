
import os 
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt 
from datetime import datetime

home = "G:\\report\\year-3\\07-Fall-2020\\#3Paper\\data\\changePointTimeSeries\\"\
        "mamun-cpt-approach\\twcr\\001-additionalTesting\\annualSTD"


os.chdir(home)

def getSTD():

    obs = pd.read_csv("sanfrancisco_usa.csv")

    #get date time series
    getDate = lambda x:x.split(' ')[0]
    time_stamp1 = lambda x: (datetime.strptime(x, '%Y-%m-%d %H:%M:%S'))

    obs['date'] = pd.DataFrame(list(map(time_stamp1, obs['date'])))

    #extract year column
    getYear = lambda x: x.year
    obs['year'] = pd.DataFrame(list(map(getYear, obs['date'])))

    print(obs)

    #get STD    
    dat = obs.copy()

    sd = pd.DataFrame(columns=['year', 'value'])
    years = dat['year'].unique()
    for jj in years:
        currentYear = dat[dat['year'] == jj]
        df = pd.DataFrame([jj, currentYear['surge'].std()]).T
        df.columns = ['year', 'value']
        sd = pd.concat([sd, df], axis = 0)
        # print(sd)


    sd.to_csv("sanfranciscoObsAnnualSTD.csv")


#plot annual STD
obsSTD = pd.read_csv("sanfranciscoObsAnnualSTD.csv")
reconSTD = pd.read_csv("sanfranciscoReconAnnualSTD.csv")

plt.plot(obsSTD['year'], obsSTD['value'], label = "obs", color = "blue")
plt.plot(reconSTD['year'], reconSTD['value'], label = "recon", color = "red")
plt.legend()
plt.show()


# obs = pd.read_csv("sanfranciscoObs.csv")
# recon = pd.read_csv("sanfranciscoRecon.csv")

# #define lambda functions 
# time_stamp = lambda x: (datetime.strptime(x, '%Y-%m-%d %H:%M:%S'))
# time_stamp_surge = lambda x: (datetime.strptime(x, '%Y-%m-%d'))

# obs['date'] = pd.DataFrame(list(map(time_stamp_surge, obs['ymd'])), 
#                                         columns = ['date'])
# recon['date'] = pd.DataFrame(list(map(time_stamp, recon['date'])), 
#                                          columns = ['date'])

# plt.plot(obs['date'], obs['surge'], label = "obs", color = "blue")
# plt.plot(recon['date'], recon['surge_reconsturcted'], label = "recon", color = "red")
# plt.legend()
# plt.show()