# -*- coding: utf-8 -*-
"""
Created on Wed Jun 03 11:09:00 2020

MERRA multiple scripts producer

@author: Michael Tadesse
"""
import os

os.chdir('G:\\modeling_storm_surge\\wp2\\kikoAnalysis\\combinedFiles')


for ii in range(0, 109):
    print(ii)

    # save_name_nc = '_'.join(['era', '20c', var_name[var_list[ii]], \
    #                       str(years[jj]), '.nc'])
    save_name_py = ''.join([str(ii), '-tideGauge', '.py'])
    f = open('combined_predictors.py', 'r')
    filedata = f.read()
    f.close()
    
    start = ii
    end = start + 1
    
    newdata1 = filedata.replace("startVal", repr(start))
    newdata2 = newdata1.replace("endVal", repr(end))
    # newdata3 = newdata2.replace("getFolderName", repr('_'.join(['folder', str(ii)])))


    
    #v_year = str(yearDat[ii])
    #newdata = filedata.replace("var_year", repr(v_year))
    
    
    f = open(save_name_py, 'w')
    f.write(newdata2)
    f.close()
    

        





