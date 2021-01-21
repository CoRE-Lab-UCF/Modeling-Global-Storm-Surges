# -*- coding: utf-8 -*-
"""
Created on Wed Jun 03 11:09:00 2020

MERRA multiple scripts producer

@author: Michael Tadesse
"""
import os

os.chdir('D:\\data\\scripts\\modeling_storm_surge\\wp2\\merra_scripts\\01_netCDF_extraction\\merra40Years')

years = list(range(1980,2020))
yearStr = lambda x: str(x)

#make it a string
yearDat = list(map(yearStr, years))


for ii in range(0, len(yearDat)):
    print(yearDat[ii])

    # save_name_nc = '_'.join(['era', '20c', var_name[var_list[ii]], \
    #                       str(years[jj]), '.nc'])
    save_name_py = '_'.join(['merra', str(yearDat[ii]), '.py'])
    f = open('b_merra_extract_data_original.py', 'r')
    filedata = f.read()
    f.close()
    
    v_year = str(yearDat[ii])
    newdata = filedata.replace("var_year", repr(v_year))
    
    
    f = open(save_name_py, 'w')
    f.write(newdata)
    f.close()
    

        





