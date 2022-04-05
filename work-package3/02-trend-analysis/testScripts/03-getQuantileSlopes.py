import os
import pandas as pd


dir_home = "G:\\report\\year-3\\07-Fall-2020\\#3Paper\\data\\"\
    "changePointTimeSeries\\mamun-cpt-approach\\twcr\\10-quntReg"

dir_out = "G:\\report\\year-3\\07-Fall-2020\\#3Paper\\data\\"\
    "changePointTimeSeries\\mamun-cpt-approach\\twcr\\11-quantileSlopes"

os.chdir(dir_home)

tgList = os.listdir()

#create an empty dataframe
df = pd.DataFrame(columns = 
    ['tg', 'lon', 'lat', 'tau', 't0p9_mmYear', 
        't0p95_mmYear', 't0p99_mmYear', 't0p999_mmYear'
            , 'pval0p9', 'pval0p95', 'pval0p99', 'pval0p999'])

#loop over tide gauges
for ii in range(len(tgList)):
    tg = tgList[ii]
    print(tg)

    os.chdir(dir_home)

    dat = pd.read_csv(tg)
    # print(dat)

    newDf = pd.DataFrame([tg, dat['lon'][0], dat['lat'][0], dat['tau'][0],\
                dat['value'][0], dat['value'][1], dat['value'][2], 
                    dat['value'][3], dat['pval'][0], 
                        dat['pval'][1], dat['pval'][2], dat['pval'][3]]).T
    newDf.columns = ['tg', 'lon', 'lat', 'tau', 't0p9_mmYear', 
        't0p95_mmYear', 't0p99_mmYear', 't0p999_mmYear'
            , 'pval0p9', 'pval0p95', 'pval0p99', 'pval0p999']
    # print(newDf)

    df = pd.concat([df, newDf], axis = 0)

os.chdir(dir_out)
df.to_csv("twcrQuantileTrends.csv")

