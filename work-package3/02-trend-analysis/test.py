"""  
to test trends in cuxhaven tide gauge
"""
import os 
import pandas as pd 
import pymannkendall as mk
import statsmodels.api as sm
import statsmodels.stats.stattools as stools
import matplotlib.pyplot as plt

dirObs = "G:\\report\\year-3\\07-Fall-2020\\#3Paper\\"\
    "data\\trend-analysis\\data\\03-obsSurge\\percentiles\\99"
dirERA5 = "G:\\report\\year-3\\07-Fall-2020\\#3Paper\\data"\
    "\\trend-analysis\\data\\06-era5\\02-percentiles\\99"
dirTwcr = "G:\\report\\year-3\\07-Fall-2020\\#3Paper\\data\\"\
    "trend-analysis\\data\\01-twcr\\02-percentiles\\99"
dirEra20c = "G:\\report\\year-3\\07-Fall-2020\\#3Paper\\data\\"\
    "trend-analysis\\data\\02-era20c\\02-percentiles\\99"

os.chdir(dirEra20c)


# using modified Mann-Kendall Trend Test
def mannKendal(dat, mnkd):
    if mnkd == "orignMK":
        return mk.original_test(dat['value']).slope*1000, \
            mk.original_test(dat['value']).p
    elif mnkd == "modifiedMK":
        return mk.hamed_rao_modification_test(dat['value']).slope*1000, \
                mk.hamed_rao_modification_test(dat['value']).p


def simpleReg(dat, ar):
    """ implements simple linear regression """
    x = dat['index']
    y = dat['value']

    x2 = sm.add_constant(x)
    est = sm.OLS(y, x2)
    if ar == "HAC":
        lag = int(4*(len(dat)*0.01)**(2/9))
        print("lag = ", lag)
        est2 = est.fit(cov_type = 'HAC', cov_kwds={'maxlags':lag}) # adding heteroscedasticity-consistent standard errors
        stderr = est2.bse[1] # stderr for trend coefficient
    else:
        est2 = est.fit() # default - without heteroscedasticity checking
        stderr = est2.bse[1] # stderr for trend coefficient
    
    print(est2.summary())

    # get fitted values
    predVal = est2.fittedvalues.copy()
    residual = y - predVal

    durbinStat = stools.durbin_watson(residual)
    print(durbinStat)
    return est2.params[1]*1000, est2.pvalues[1]


def sampleCode():
    dat = pd.read_csv("cuxhaven_germany.csv")
    # reset index to check if using year/ordered number plays part
    dat.reset_index(inplace = True)

    # dat = dat[dat['year'] >= 1918]
    print(dat)

    trend, pval = simpleReg(dat, "HAC")

    mkTrend, mkPval = mannKendal(dat, "modifiedMK")

    print("\n")

    print("-------------------------------------")
    print(trend, pval, "\n")
    print(mkTrend, mkPval)
    print("-------------------------------------")


os.chdir("G:\\report\\year-3\\07-Fall-2020\\#3Paper\\data"\
        "\\trend-analysis\\data\\allThreeTrends\\95_post1930_30yrs_75perc")

tgList = os.listdir()

# print(tgList)

df = pd.DataFrame(columns = ['tg', 'start', 'end'])
for tg in tgList:
    dat = pd.read_csv(tg)
    # print(int(dat['year'][0]), int(dat['year'][len(dat) - 1]), 
    #         int(dat['year'][len(dat) - 1]) - int(dat['year'][0]))

    newDf = pd.DataFrame([tg, int(dat['year'][0]), int(dat['year'][len(dat) - 1])]).T
    newDf.columns = ['tg', 'start', 'end']

    df = pd.concat([df, newDf])

print(df)

os.chdir("G:\\report\\year-3\\07-Fall-2020\\#3Paper\\data"\
        "\\trend-analysis\\data\\allThreeTrends")

df.to_csv("trendDiff_tgs_years.csv")