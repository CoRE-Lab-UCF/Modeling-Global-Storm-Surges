#get libraries
import os 
import pandas as pd 

dir_cptFile = "G:\\report\\year-3\\07-Fall-2020\\#3Paper\\data\\changePointTimeSeries\\"\
        "mamun-cpt-approach\\twcr\\0001-predCPT\\cptSA"
dir_home = "G:\\data\\allReconstructions\\01_20cr"
dir_out = "G:\\report\\year-3\\07-Fall-2020\\#3Paper\\data\\changePointTimeSeries\\"\
        "mamun-cpt-approach\\twcr\\0001-predCPT\\postCPT"

def getPostCpt():
    """
    this function filters twcr data after the corresponding
    changepoint year
    """
    os.chdir(dir_cptFile)
    cptFile = pd.read_csv("twcrVisual_Inspection_csv_v3.csv")
    print(cptFile)

    #loop through tide gauges
    for tg in cptFile['tg']:
        cpt = cptFile[cptFile['tg'] == tg]['visual inspection'].values[0]
        print(tg, " - ", cpt)

        #pick up reconstruction file 
        os.chdir(dir_home)
        dat = pd.read_csv(tg)
        print(dat)
        getYear = lambda x: x.split('-')[0]
        dat['year'] = pd.DataFrame(list(map(getYear, dat['date'])))

        #filter based on cpt
        if cpt == "1836":
            datFiltered = \
                dat.copy()[['date', 'surge_reconsturcted', \
                    'pred_int_lower', 'pred_int_upper', 'lon', 'lat']]
            os.chdir(dir_out)
            datFiltered.to_csv(tg)
        elif cpt == "discard ":
            continue
        else:
            datFiltered = dat[dat['year'] > str(cpt)][['date', 'surge_reconsturcted', \
                    'pred_int_lower', 'pred_int_upper', 'lon', 'lat']]
            os.chdir(dir_out)
            datFiltered.to_csv(tg)


#run function 
getPostCpt()