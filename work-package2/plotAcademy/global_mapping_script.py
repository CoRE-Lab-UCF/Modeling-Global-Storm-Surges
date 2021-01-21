# -*- coding: utf-8 -*-
"""
Created on Tue Apr 14 09:49:38 2020


Global Mapping (correlation/RMSE) script

@author: Michael Tadesse
"""
import os
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
#locate the file that basemap needs
os.environ["PROJ_LIB"] = "C:\\Users\\WahlInstall\\Anaconda3\\Library\\share\\basemap";
from mpl_toolkits.basemap import Basemap



#load file to be plotted
dat = pd.read_csv('eraint_lrreg_validation_pca.csv')
dat_new = dat.drop(dat.loc[dat['tg'] == 'roscoff-france-refmar.csv'].index)
dat_new.reset_index(inplace = True)
dat_new.drop(['index'], axis =1, inplace = True)
dat_new.drop(['Unnamed: 0'], axis =1, inplace = True)


sns.set_context('notebook', font_scale = 2)

#%%plotting netCDF
#use 'cyl' projection for wider figure (not square)
#also use the lon.min, lon.max in order not to plot half of the map
fig=plt.figure(figsize=(12, 8) )
m=Basemap(projection='cyl',lat_ts=10,llcrnrlon=lon.min(), \
  urcrnrlon=lon.max(),llcrnrlat=lat.min(),urcrnrlat=lat.max(), \
  resolution='c')
x, y = m(*np.meshgrid(lon,lat))
m.contourf(x,y,pred[0,:,:],cmap='jet')
m.colorbar(location='bottom')
m.drawcoastlines()
m.drawmapboundary()
#m.drawparallels(np.arange(-90.,90.,30.),labels=[1,0,0,0])
#m.drawmeridians(np.arange(-180.,180.,60.),labels=[0,0,0,1])
#plt.title('VWND 09/8/11990


#%%plotting rmse
fig=plt.figure(figsize=(16, 12) )
m=Basemap(projection='mill', lat_ts=10, llcrnrlon=-180, \
  urcrnrlon=180,llcrnrlat=-80,urcrnrlat=80, \
  resolution='c')
x,y = m(dat_new['lon'].tolist(), dat_new['lat'].tolist())
m.drawcoastlines()
m.fillcontinents(color='coral',lake_color='aqua')
plt.scatter(x, y, 70, marker = 'o', edgecolors = 'black', c = dat_new['rmse'], cmap = 'hot_r')
cbar = m.colorbar(location = 'bottom')
plt.clim(0, 0.3)
plt.title('Base_case - RMSE(m)')

#save figure
plt.savefig("base_case_corr.png", dpi = 400)


#plotting correlation
fig=plt.figure(figsize=(16, 12) )
m=Basemap(projection='mill', lat_ts=10, llcrnrlon=-180, \
  urcrnrlon=180,llcrnrlat=-80,urcrnrlat=80, \
  resolution='c')
x,y = m(dat_new['lon'].tolist(), dat_new['lat'].tolist())
m.drawcoastlines()
plt.scatter(x, y, 70, marker = 'o', edgecolors = 'black',\
            c = dat_new['corr_data'], cmap = 'hot_r')
cbar = m.colorbar(location = 'bottom')
plt.clim(0, 1)
plt.title('Base_case  - Correlation')


#plotting rmse with bluemarble basemap
fig=plt.figure(figsize=(16, 12) )
m=Basemap(projection='mill', lat_ts=10, llcrnrlon=-180, \
  urcrnrlon=180,llcrnrlat=-80,urcrnrlat=80, \
  resolution='c')
x,y = m(grid_rmse['lon'].tolist(), grid_rmse['lat'].tolist())
m.drawcoastlines()
m.bluemarble(alpha = 0.8) #basemap , alpha = transparency
plt.scatter(x, y, 70, marker = 'o', edgecolors = 'black', c = grid_rmse['rmse_g1'], cmap = 'hot_r')
cbar = m.colorbar(location = 'bottom')
#plt.clim(0, 0.3)
#plt.title('Base_case - RMSE(m)')



#extract correlation data from dat_new
gridcorr_data = pd.DataFrame(list(map(get_corr, dat_new['corrn'])), columns = ['corrn'])
dat_new['corr_data'] = corr_data


#get histogram plot - add edge colors to the histogram
plt.figure(figsize=(8,6))
sns.distplot(combo_rmse_clean['rmse95d5'], hist = True, kde = False, bins=100, hist_kws=dict(edgecolor="k", linewidth=1))
plt.xlim(0, 0.8)
plt.ylabel('No. Tide Gauges')
plt.title('10 x 10')
plt.xlabel('RMSE(m)')

#plot scatterplot with seaborn - hue and style
plt.figure(figsize = (10, 8))
sns.scatterplot(x = 'time', y = 'delta_rmse', hue = 'Grid Sizes', style='Grid Sizes', data = comp, s=200)
plt.legend(ncol = 2)
plt.grid(alpha = 0.4)
plt.ylabel('Average increase in RMSE (cm)')
plt.xlabel('Run Time (hrs.)')


#to place legend outside the plotting box
plt.figure(figsize=(18, 12))
sns.boxplot(x = 'variable', y = mdf_rmse['value']*100, hue = 'variable', data = mdf_rmse, palette = 'Accent')
plt.legend(ncol = 8)
plt.legend(bbox_to_anchor=(0,1.02,1,0.2), loc="lower left",
                mode="expand", borderaxespad=0, ncol=7)
plt.ylabel('Absolute Rmse (cm)')
plt.xlabel('Grid Sizes')


#plot scatterplot with errorbars
plt.figure(figsize=(10, 8))
sns.scatterplot(x = 'time', y = 'avg_rmse', hue = 'grid_size', style='grid_size', data = comp, s=200)
plt.errorbar(comp['time'], comp['avg_rmse'], yerr=comp['rmse_std'], ecolor= 'gray', alpha = 0.6, capsize = 20)
plt.legend(bbox_to_anchor=(0,1.02,1,0.2), loc="lower left",
                mode="expand", borderaxespad=0, ncol=8)
plt.ylabel('Absolute Rmse (cm)')
plt.xlabel('Grid Sizes')
plt.grid()
plt.ylim(0, 40)



#to plot prediction intervals
time_stamp = lambda x: (datetime.strptime(x, '%Y-%m-%d %H:%M:%S'))
final_dat['date'] = pd.DataFrame(list(map(time_stamp, final_dat['date'])), columns = ['date'])
surge['date'] = pd.DataFrame(list(map(time_stamp, surge['date'])), columns = ['date'])
sns.set_context('notebook', font_scale = 2)
plt.figure()
plt.plot(final_dat['date'], final_dat['mean'], color = 'green')
plt.scatter(surge['date'], surge['surge'], color = 'blue')
# prediction intervals
plt.plot(final_dat['date'], final_dat['obs_ci_lower'], color = 'red',  linestyle = "--", lw = 0.8)
plt.plot(final_dat['date'], final_dat['obs_ci_upper'], color = 'red',  linestyle = "--", lw = 0.8)
# confidence intervals
plt.plot(final_dat['date'], final_dat['mean_ci_upper'], color = 'black',  linestyle = "--", lw = 0.8)
plt.plot(final_dat['date'], final_dat['mean_ci_lower'], color = 'black',  linestyle = "--", lw = 0.8)


plt.figure()
plt.plot(cux_mlr['date'], cux_mlr['surge_reconsturcted'], color = 'blue', label = 'mlr_recon')
plt.plot(cux_rf['date'], cux_rf['surge_reconsturcted'], color = 'green', label = 'rf_recon')
#mlr pred intervals
plt.plot(cux_mlr['date'], cux_mlr['pred_int_lower'], lw = 0.5 ,ls = '--', color = 'blue', label = 'pred_lower interval')
plt.plot(cux_mlr['date'], cux_mlr['pred_int_upper'], lw = 0.5, ls = '--', color = 'blue', label = 'pred_upper interval')
#rf pred intervals
plt.plot(cux_rf['date'], cux_rf['pred_int_lower'], lw = 0.5 ,ls = '--', color = 'green', label = 'pred_lower interval')
plt.plot(cux_rf['date'], cux_rf['pred_int_upper'], lw = 0.5, ls = '--', color = 'green', label = 'pred_upper interval')
plt.legend()



#to overlay maps
#%%plotting netCDF
#use 'cyl' projection for wider figure (not square)
#also use the lon.min, lon.max in order not to plot half of the map
fig=plt.figure(figsize=(12, 8) )
m=Basemap(projection='cyl',lat_ts=10,llcrnrlon=lon.min(), \
  urcrnrlon=lon.max(),llcrnrlat=lat.min(),urcrnrlat=lat.max(), \
  resolution='c')
x, y = m(*np.meshgrid(lon_sub,lat_sub))
m.contourf(x,y,pred_sub[0,:,:],cmap='jet')
m.scatter(tg_cord.Longitude, tg_cord.Latitude)
m.colorbar(location='bottom')
#m.drawcoastlines()
m.bluemarble(alpha = 0.8) #basemap , alpha = transparency
m.drawmapboundary()
#m.drawstates()
#m.drawparallels(np.arange(-90.,90.,30.),labels=[1,0,0,0])
#m.drawmeridians(np.arange(-180.,180.,60.),labels=[0,0,0,1])
#plt.title('VWND 09/8/11990


#plot only a subset of a map
fig=plt.figure(figsize=(12, 8) )
m=Basemap(projection='cyl',lat_ts=10,llcrnrlon=260, \
  urcrnrlon=280,llcrnrlat=10,urcrnrlat=40, \
  resolution='c')
x, y = m(*np.meshgrid(lon_sub,lat_sub))
m.pcolor(x,y,pred_sub,cmap='jet')
#m.scatter(tg_cord.Longitude, tg_cord.Latitude)
m.colorbar()
m.drawcoastlines()
m.bluemarble(alpha = 0.8) #basemap , alpha = transparency
m.drawmapboundary()
plt.clim(98750, 100750)
plt.title('Hurricane Katrina - SLP - ERA5 - 08/29/2005 06:00:00')