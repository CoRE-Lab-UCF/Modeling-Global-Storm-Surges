"""  
script to merge visual inspection results for
twcr and era20c
"""

import os
import pandas as pd

dirTwcr = "G:\\report\\year-3\\07-Fall-2020\\#3Paper\\data\\changePointTimeSeries\\"\
    "mamun-cpt-approach\\twcr\\0001-predCPT\\cptSA"
dirEra20c = "G:\\report\\year-3\\07-Fall-2020\\#3Paper\\data\\changePointTimeSeries\\"\
    "mamun-cpt-approach\\era20c\\0001-predCPT\\cptSA"
dirTwcrEra20c = "G:\\report\\year-3\\07-Fall-2020\\#3Paper\\data\\changePointTimeSeries"\
    "\\mamun-cpt-approach\\twcr_era20c_1900_2010"


os.chdir(dirEra20c)
dat = pd.read_csv("era20cVisual_Inspection_csv.csv")
print(dat['visual_inspection'])
print(dat['visual_inspection'].value_counts())

era20cCount = dat['visual_inspection'].value_counts()
era20cCount.to_csv("era20cCount.csv")


# os.chdir(dirEra20c)
# dat = pd.read_csv("era20cRecordLengthComparison.csv")




def cptComparison():

    dat = pd.read_csv("twcrEra20c_cptComparison.csv")

    print("p5E has {} tgs".format(len(dat[dat['p5E'] == True])))
    print("p10E has {} tgs".format(len(dat[dat['p10E'] == True])))
    print("p15E has {} tgs".format(len(dat[dat['p15E'] == True])))
    print("p20E has {} tgs".format(len(dat[dat['p20E'] == True])))
    print("p25E has {} tgs".format(len(dat[dat['p25E'] == True])))
    print("p30E has {} tgs".format(len(dat[dat['p30E'] == True])))
    print("p40E has {} tgs".format(len(dat[dat['p40E'] == True])))
    print("p50E has {} tgs".format(len(dat[dat['p50E'] == True])))

    print()
    print()

    print("p5T has {} tgs".format(len(dat[dat['p5E'] == False])))
    print("p10T has {} tgs".format(len(dat[dat['p10E'] == False])))
    print("p15T has {} tgs".format(len(dat[dat['p15E'] == False])))
    print("p20T has {} tgs".format(len(dat[dat['p20E'] == False])))
    print("p25T has {} tgs".format(len(dat[dat['p25E'] == False])))
    print("p30T has {} tgs".format(len(dat[dat['p30E'] == False])))
    print("p40T has {} tgs".format(len(dat[dat['p40E'] == False])))
    print("p50T has {} tgs".format(len(dat[dat['p50E'] == False])))


def twcr_era20c_merger():
    os.chdir(dirTwcr)
    twcr = pd.read_csv("twcrVisual_Inspection_GSSRDB.csv")
    twcr.columns = ['tg', 'p_5', 'p_10', 'p_15', 'p_20', 'p_25', 'p_30', 'p_40', 'p_50',
        'viTwcr']

    print(twcr)

    os.chdir(dirEra20c)
    era20c = pd.read_csv("era20cVisual_Inspection_GSSRDB.csv")
    era20c.columns = ['tg', 'p_5', 'p_10', 'p_15', 'p_20', 'p_25', 'p_30', 'p_40', 'p_50',
        'viEra20c']
    print(era20c)

    # merge 
    dfMerged = pd.merge(twcr, era20c, on='tg', how='inner')
    dfNotDiscard = dfMerged[(dfMerged['viTwcr'] != 'discard ') & (dfMerged['viEra20c'] != 'discard')]
    print(dfNotDiscard[['tg', 'viTwcr', 'viEra20c']])
    # print(dfMerged[dfMerged['viEra20c'] == 'discard'][['tg', 'viTwcr', 'viEra20c']])

    # save as csv
    os.chdir("G:\\report\\year-3\\07-Fall-2020\\#3Paper\\data\\"\
        "changePointTimeSeries\\mamun-cpt-approach\\twcr_Era20c_merged_visual_inspection")
    dfNotDiscard[['tg', 'viTwcr', 'viEra20c']].to_csv("twcrEra20cMergedVI.csv")