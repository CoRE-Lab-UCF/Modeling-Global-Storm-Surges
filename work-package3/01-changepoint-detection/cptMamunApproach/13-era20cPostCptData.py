#get libraries
import os 
import pandas as pd 

dir_cptFile = "G:\\report\\year-3\\07-Fall-2020\\#3Paper\\data\\changePointTimeSeries\\"\
        "mamun-cpt-approach\\era20c\\0001-predCPT\\cptSA"
dir_home = "G:\\data\\allReconstructions\\02_era20c"
dir_out = "G:\\report\\year-3\\07-Fall-2020\\#3Paper\\data\\changePointTimeSeries\\"\
        "mamun-cpt-approach\\era20c\\0001-predCPT\\postCPT"

def getPostCpt():
    """
    this function filters twcr data after the corresponding
    changepoint year
    """
    os.chdir(dir_cptFile)
    cptFile = pd.read_csv("era20cVisual_Inspection_csv.csv")
    print(cptFile)

    #loop through tide gauges
    for tg in cptFile['tg']:
        cpt = cptFile[cptFile['tg'] == tg]['visual_inspection'].values[0]
        print(tg, " - ", cpt)

        #pick up reconstruction file 
        os.chdir(dir_home)
        dat = pd.read_csv(tg)
        print(dat)
        getYear = lambda x: x.split('-')[0]
        dat['year'] = pd.DataFrame(list(map(getYear, dat['date'])))

        #filter based on cpt
        if cpt == "1900":
            datFiltered = \
                dat.copy()[['date', 'surge_reconsturcted', \
                    'pred_int_lower', 'pred_int_upper', 'lon', 'lat']]
            os.chdir(dir_out)
            datFiltered.to_csv(tg)
        elif cpt == "discard":
            continue
        else:
            datFiltered = dat[dat['year'] > str(cpt)][['date', 'surge_reconsturcted', \
                    'pred_int_lower', 'pred_int_upper', 'lon', 'lat']]
            os.chdir(dir_out)
            datFiltered.to_csv(tg)


#run function 
getPostCpt()