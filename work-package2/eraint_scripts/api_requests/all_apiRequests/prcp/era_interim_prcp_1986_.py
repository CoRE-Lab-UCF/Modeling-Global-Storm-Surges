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
    "date": '1986-01-01/to/1986-12-31',
    "expver": "1",
    "grid": "0.75/0.75",
    "levtype": "sfc",
    "param": '228.128',
    "step": "3/6/9/12",
    "stream": "oper",
    "time": "00:00:00/12:00:00",
    "type": "fc",
    "format": "netcdf",
    "target": 'era_interim_prcp_1986_.nc',
})