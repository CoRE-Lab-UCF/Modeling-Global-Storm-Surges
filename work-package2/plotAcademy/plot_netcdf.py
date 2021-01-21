# -*- coding: utf-8 -*-
"""
Created on Fri Mar 20 15:30:46 2020
Plotting NetCDF files 
@author: Michael Tadesse
"""

#tweak to load basemap
#find the location of the epsg file
import os
os.environ["PROJ_LIB"] = "C:\\Users\\WahlInstall\\Anaconda3\\Library\\share\\basemap";
from mpl_toolkits.basemap import Basemap


#load netcdf file
prs = Dataset('era_interim_slp_1987_1990.nc')
slp = prs.variables['msl'][:]

#subset a portiong of the array to plot it
slp_test = slp[4385,:,:]

#flip it to correctly plot
#slp_test_flip = slp[::-1]

#plot
fig=plt.figure(figsize=(12, 8) )
m=Basemap(projection='mill',lat_ts=10,llcrnrlon=lons.min(), \
  urcrnrlon=lons.max(),llcrnrlat=lats.min(),urcrnrlat=lats.max(), \
  resolution='c')
x, y = m(*np.meshgrid(lons,lats))
m.pcolormesh(x,y,vwnd_test,shading='flat',cmap='jet')
m.colorbar(location='right')
m.drawcoastlines()
m.drawmapboundary()
m.drawparallels(np.arange(-90.,90.,30.),labels=[1,0,0,0])
m.drawmeridians(np.arange(-180.,180.,60.),labels=[0,0,0,1])
plt.title('VWND 09/8/11990')

