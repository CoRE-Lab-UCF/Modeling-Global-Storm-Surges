# -*- coding: utf-8 -*-
"""
Created on Thu Mar 19 12:20:00 2020
ERA-Interim api request template
@author: Michael Tadesse
"""
import os 
os.chdir('D:\\data\\era_interim\\era_interim_netcdf')

#!/usr/bin/env python
from ecmwfapi import ECMWFDataServer
server = ECMWFDataServer()
server.retrieve({
    "class": "ei",
    "dataset": "interim",
    "date": '2018-01-01/to/2018-12-31',
    "expver": "1",
    "grid": "0.75/0.75",
    "levtype": "sfc",
    "param": '34.128',
    "step": "0",
    "stream": "oper",
    "time": "00:00:00/06:00:00/12:00:00/18:00:00",
    "type": "an",
    "format": "netcdf",
    "target": 'era_interim_sst_2018_.nc',
})