""" 
this script reads grib data for era5
"""
import os 
import cfgrib
import numpy as np
import xarray as xr
from osgeo import gdal
import matplotlib.pyplot as plt

dirHome = "G:\\report\\year-3\\07-Fall-2020\\#3Paper\\data\\"\
    "changePointTimeSeries\\mamun-cpt-approach\\era5\\fremantle-data"

os.chdir(dirHome)


# ds=xr.open_dataset("all_1979_1982.grib",engine='cfgrib')