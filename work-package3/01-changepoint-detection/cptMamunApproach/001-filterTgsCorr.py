import shutil
import os
import pandas as pd
from os.path import exists

dir_home = "G:\\report\\year-3\\07-Fall-2020\\#3Paper\\data\\changePointTimeSeries\\era20cSTD"
dir_tg = "G:\\report\\year-3\\07-Fall-2020\\#3Paper\\data\\changePointTimeSeries\\reconValidation"
dir_out = "G:\\report\\year-3\\07-Fall-2020\\#3Paper\\data\\changePointTimeSeries\\era20cSTD_filtered"


def selectTgs():
    """
    this function chooses the probRange tgs
    based on the selected tgs (on validation)
    """
    os.chdir(dir_tg)
    df = pd.read_csv("era20cCorr0p7plus.csv")

    for tg in df['tg']:
        print(tg, "\n")
        
        os.chdir(dir_home)

        if not exists(tg):
            print("not found")
        else:
            source = os.path.join(os.path.abspath(os.getcwd()), tg)
            print(source)
            destination = os.path.join(dir_out, tg)
            print(destination)

            try:
                shutil.copyfile(source, destination)
            except shutil.SameFileError:
                print("source and destination represent the same file")
            except:
                print("error occured while copying file")

#run function
selectTgs()