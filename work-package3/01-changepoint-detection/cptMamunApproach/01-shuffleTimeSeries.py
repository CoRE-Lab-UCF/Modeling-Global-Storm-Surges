import os
import pandas as pd


dir_home = "G:\\report\\year-3\\07-Fall-2020\\#3Paper\\data\\changePointTimeSeries"\
        "\\mamun-cpt-approach\\era20c\\0001-predCPT\\wnd_v\\annualSTD"
dir_out = "G:\\report\\year-3\\07-Fall-2020\\#3Paper\\data\\changePointTimeSeries"\
        "\\mamun-cpt-approach\\era20c\\0001-predCPT\\wnd_v\\01-randomizedSTD"

def shuffleTS():
    """
    this function shuffles the rows of the std time series 
    saves csv of the time series 
    """
    os.chdir(dir_home)

    tgList = os.listdir()
    for tg in tgList:
        
        os.chdir(dir_home)
        print(tg)
        dat = pd.read_csv(tg)
        print(dat)

        n = 1000 #number of iterations 
        for ii in range(n):
            datRand = dat.sample(frac = 1) #shuffle the rows of the dataframe
            # datRand.drop(['Unnamed: 0'], axis = 1, inplace = True)
            os.chdir(dir_out)

            # change here to rmse/std/corr
            saveName = 'std' + str(ii) + '.csv'

            try:
                os.makedirs(tg)
                os.chdir(tg)
                datRand.to_csv(saveName)
            except FileExistsError:
                os.chdir(tg)
                datRand.to_csv(saveName)

#run function
shuffleTS()

