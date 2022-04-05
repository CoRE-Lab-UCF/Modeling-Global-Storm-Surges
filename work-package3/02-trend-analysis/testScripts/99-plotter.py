import os
import numpy as np
import pandas as pd
from datetime import datetime
import matplotlib.pyplot as plt
from numpy.random import seed
from numpy.random import randn
from scipy import stats
from scipy.stats import normaltest
from scipy.stats import anderson
import statsmodels.api as sm 
from scipy import stats
from sklearn.linear_model import LinearRegression
from statsmodels.graphics.gofplots import qqplot


dirHome = "G:\\report\\year-3\\07-Fall-2020\\#3Paper\\data\\trend-analysis\\data\\test"

os.chdir(dirHome)

datTwcr = pd.read_csv("cuxhavenTwcr99Percentile.csv")
datEra20c = pd.read_csv("cuxhavenEra20c99Percentile.csv")

datEra20cMartha = datEra20c[datEra20c['year'] >= 1960]


# print(datTwcr)
# print(datEra20c)

def plotTimeSeries():
    plt.figure(figsize=(15,4))
    plt.plot(datTwcr['year'], datTwcr['value'], label = "99th twcr surge", color = "green")
    plt.plot(datEra20c['year'], datEra20c['value'], label = "99th era20c surge", color = "magenta")
    plt.legend()
    plt.ylabel("Surge Height (m)")
    plt.grid(b=None, which='major', axis= 'both', linestyle='-')
    plt.minorticks_on()
    plt.grid(b=None, which='minor', linestyle='--', axis="both", alpha=0.4)
    plt.show()

def plotHist(x,y):
    plt.hist(x['value'], color = "green")
    plt.hist(y['value'], color = "magenta", alpha=0.4)
    plt.show()

def plotQuant(x):
    qqplot(x, line = 's')
    plt.show()

def checkNormality(x):
    """ checks normality of the time series """
    shapiro_test = stats.shapiro(x) # shapiro test
    stat, p = normaltest(x) # D'Agostino test

    print("shapiro pvalue = {}".format(shapiro_test.pvalue))
    print("D'Agostino pvalue = {} \n".format(p))
    print()

def simpleReg(dat):
    """ implements simple linear regression """
    x = dat['year']
    y = dat['value']

    x2 = sm.add_constant(x)
    est = sm.OLS(y, x2)
    est2 = est.fit()

    print("pvalue = {}".format(est2.pvalues[1]))
    print(est2.summary())



# plotHist(datTwcr, datEra20c)
# plotQuant(datTwcr['value'])
# plotQuant(datEra20c['value'])

# checkNormality(datTwcr['value'])
# checkNormality(datEra20c['value'])

simpleReg(datEra20c)
simpleReg(datEra20cMartha)