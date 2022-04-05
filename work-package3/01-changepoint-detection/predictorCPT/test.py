import os
from numpy import nan 
import pandas as pd 
import matplotlib.pyplot as plt

dirHome = "G:\\report\\year-3\\07-Fall-2020\\#3Paper\\data\\"\
        "changePointTimeSeries\\mamun-cpt-approach\\era20c\\0001-predCPT\\cptSA"

os.chdir(dirHome)

dat = pd.read_csv("era20cCptSA_v2.csv")

# count changepoints by year
countDat = dat['visual_inspection'].value_counts()

for ii in range(len(dat)):
    print(dat['tg'][ii])
    
    print(dat['visual_inspection'][ii].isnull())

    # replace nans
#     count = 0;
#     if dat['visual_inspection'][ii] == 'discard':
#         continue
#     if dat['visual_inspection'][ii].isnull():
#         print("found nan")
#         count = count + 1
#         dat['visual_inspection'][ii] = dat['p_30'][ii]

# print(count)










def test3():
        # print(dat['visual inspection'].value_counts())

        countDat = dat['visual inspection'].value_counts()

        countDat.to_csv('twcrCPTCount.csv')

        print(countDat)

# newDat = dat[dat['visual inspection'] != "discard "]
# # print(newDat[newDat['visual inspection'] not in None])
# print(newDat)

# for ii in (range(len(dat))):
#     print(newDat['visual inspection'][ii])
#     if not newDat['visual inspection'][ii]:
#         newDat['visual inspection'][ii] = 'NA'

# print(newDat)

# # print(float(dat['visual inspection']))

# plt.hist(dat['visual inspection'], bins = 10)
# plt.show()

def test2():
        dat = pd.read_csv("twcrCptSA.csv")

        print(dat)

        plt.scatter(dat.index, dat['p_50'])
        plt.axhline(y = 1955, color = "red", ls = "--", lw = 1.0, label = "60 year Mark (1955)")
        plt.title('p = 50%')
        plt.show()

        print(dat[dat['p_50'] <= 1955])

def test1():

    print(dat[dat['avgCPT'] < 1900]['avgCPT'])

    print(len(dat[dat['reconCPT'] >= 1960]))
    print(len(dat[dat['avgCPT'] >= 1960]))

    print("num of tgs with 1900 as cpt {}".format(len(dat[dat['avgCPT'] == 1900])))

    # scatter plot cpt for comparing cpt differences
    plt.figure(figsize=(10, 5))
    # plt.scatter(dat['Unnamed: 0'], dat['reconCPT']-dat['avgCPT'], color = "black", label = "reconCPT-avgCPT")
    # plt.scatter(dat['Unnamed: 0'], dat['reconCPT'], color = "green", label = "reconCPT")
    # plt.scatter(dat['Unnamed: 0'], dat['avgCPT'], color = "magenta", label = "avguCPT")
    # plt.plot(dat['Unnamed: 0'], dat['recon_wndv'], color = "blue", label = "reconCPT vs wndvCPT")
    # plt.scatter(dat['Unnamed: 0'], dat['wnduCPT'], color = "black", label = "wnduCPT")
    # plt.scatter(dat['Unnamed: 0'], dat['wndvCPT'], color = "magenta", label = "wndvCPT")

    # plt.scatter(dat['Unnamed: 0'], dat['reconCPT'], color = "green", label = "reconCPT")
    plt.scatter(dat['Unnamed: 0'], dat['avgCPT'], color = "red", label = "avgCPT")


    plt.legend()
    # plt.show()