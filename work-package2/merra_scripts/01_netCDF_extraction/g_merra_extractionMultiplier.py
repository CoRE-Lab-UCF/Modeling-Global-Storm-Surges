# -*- coding: utf-8 -*-
"""
Created on Wed Jun 03 11:09:00 2020

MERRA multiple scripts producer

@author: Michael Tadesse
"""
import os

os.chdir('D:\\data\\scripts\\modeling_storm_surge\\wp2\\merra_scripts\\01_netCDF_extraction\\merra40Years')


for ii in range(0, int(882/25)+1):
    print(ii)

    # save_name_nc = '_'.join(['era', '20c', var_name[var_list[ii]], \
    #                       str(years[jj]), '.nc'])
    save_name_py = '_'.join(['folder', str(ii), '.py'])
    f = open('b_merra_extract_data_original.py', 'r')
    filedata = f.read()
    f.close()
    
    start = ii*25
    if (start + 25 >881):
        end = 881
    else:
        end = start + 26
    
    newdata1 = filedata.replace("startVal", repr(start))
    newdata2 = newdata1.replace("endVal", repr(end))
    newdata3 = newdata2.replace("getFolderName", repr('_'.join(['folder', str(ii)])))


    
    #v_year = str(yearDat[ii])
    #newdata = filedata.replace("var_year", repr(v_year))
    
    
    f = open(save_name_py, 'w')
    f.write(newdata3)
    f.close()
    

        





