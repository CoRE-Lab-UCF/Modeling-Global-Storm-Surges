# -*- coding: utf-8 -*-
"""
Created on Thu Mar 19 12:28:00 2020
ERA-Interim - api request
@author: Michael Tadesse
"""
import os

os.chdir('D:\\data\\era_interim\\era_interm_scripts')

#param: "228.128" == prcp
#param: "34.128" == sst
#param: "151.128" == mean sea level pressure
#date foremat: "1900-01-01/to/1900-01-31"

var_name = {"34.128":'sst'}
years = list(range(1979,2019));

#list of the variable names
var_list = list(var_name.keys())

for ii in range(0, len(var_list)):
    for jj in range(0,len(years)):
        print(var_name[var_list[ii]], years[jj])
        
        save_name_nc = '_'.join(['era', 'interim', var_name[var_list[ii]], \
                              str(years[jj]), '.nc'])
        save_name_py = '_'.join(['era', 'interim', var_name[var_list[ii]], \
                              str(years[jj]), '.py'])
        os.chdir('D:\\data\\era_interim\\era_interm_scripts')
        f = open('api_req_original_sst.py', 'r')
        filedata = f.read()
        f.close()
        
        v_date = ''.join([str(years[jj]),'-01-01/to/',str(years[jj]), '-12-31'])
        newdata = filedata.replace("var_date", repr(v_date))
        newdata = newdata.replace("var_param", repr(var_list[ii]))
        newdata = newdata.replace("var_save_name", repr(save_name_nc))
        
        os.chdir('D:\\data\\era_interim\\era_interm_scripts\\all_apiRequests')
        f = open(save_name_py, 'w')
        f.write(newdata)
        f.close()
        

        





