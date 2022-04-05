import os
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
#locate the file that basemap needs
os.environ["PROJ_LIB"] = "C:\\Users\\WahlInstall\\"\
    "Anaconda3\\Library\\share\\basemap";
from mpl_toolkits.basemap import Basemap
from mpl_toolkits.axes_grid.inset_locator import inset_axes



os.chdir("G:\\report\\year-3\\07-Fall-2020\\#3Paper\\data\\changePointTimeSeries"\
        "\\mamun-cpt-approach\\comparison")
dat = pd.read_csv("twcrEra20cMerged.csv")
print(dat[dat['year_era20c'] <= 1960])
df = dat[dat['year_era20c'] <= 1960]






def reader():
    newDat = df[df['corrn_lr'] >= 0.7]
    newDat.reset_index(inplace = True)
    newDat.drop(['index', 'Unnamed: 0'],  axis = 1, inplace = True)
    # print(newDat)
    # newDat.to_csv("tgCorr0p7plus.csv")

extenstion = ['_glossdm_bodc', '_uhslc', '_jma', '_bodc', '_noaa',\
              '_med_refmar', '_pde', '_meds', '_noc', '_ieo', '_idromare',\
                  '_eseas', 'france_refmar', '_noc', '_smhi', '_bsh',\
                      '_fmi', '_rws', '_dmi', '_statkart', '_coastguard',\
                          '_itt', '_comune_venezia', '_johnhunter', '_university_zagreb']

#replace commas and hyphens
def renameMetaData(newDat):
    dat = newDat.copy() 
    print(dat)

    for ii in range(0, len(dat)):
        oldName = dat['tg'][ii]
        charToRemove = ",-"
        
        for jj in charToRemove:
            newName= oldName.replace(jj, "_")
            print(oldName, " ", newName)
            dat.iloc[ii, 0] = newName
    return dat

#change reanalysis here
def removeExt(newDat, extenstion):

    dat = newDat.copy()  

    for ii in range(0, len(dat)):
        # print(dat['tg'][ii])
        for ext in extenstion:
            if dat['tg'][ii].endswith(ext+".csv"):
                
                print(dat['tg'][ii],"----ENDS WITH---- [", ext, "]")
                                    
                #split it
                new_name = dat['tg'][ii].split(ext+'.csv')[0] + str(".csv")
                print(new_name)
                #rename file
                dat.iloc[ii, 0] = new_name
            
    dat = dat[['tg', 'lon', 'lat', 'corrn_lr']]

    #save metadat as csv
    dat.to_csv('era20cCorr0p7plus.csv')

def plotter(dat):

    #increase plot font size
    sns.set_context('notebook', font_scale = 1.5)

    plt.figure(figsize=(20, 10))
    m=Basemap(projection='cyl', lat_ts=20, llcrnrlon=-180, 
            urcrnrlon=180,llcrnrlat=-90,urcrnrlat=90, resolution='c')
    x,y = m(dat['lon'].tolist(), dat['lat'].tolist())
    m.drawcoastlines()


    #get degree signs 
    parallels = np.arange(-80,81,20.)
    meridians = np.arange(-180.,180.,40.)
    #labels = [left,right,top,bottom]
    m.drawparallels(parallels,labels=[True,True,False,False], \
                    linewidth = 0.5)
    m.drawmeridians(meridians,labels=[False,False,False,True], \
                    linewidth = 0.5)

    m.bluemarble(alpha = .82)

    # color_dict = {'ERA-20C' : 'magenta', '20CR' : 'green'}

    ax = sns.scatterplot(x = x, y = y, s = 70, data = dat, \
        hue = 'year_era20c')
    # m.colorbar(location = 'bottom')
    plt.legend()
    plt.show()


##run function
# newDf = renameMetaData(newDat)
# print(newDf)
# removeExt(newDf, extenstion)
plotter(df)