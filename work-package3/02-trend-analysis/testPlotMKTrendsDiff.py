import os
import numpy as np
import pandas as pd
from scipy.ndimage.measurements import label
import seaborn as sns
import matplotlib
import matplotlib.pyplot as plt
#locate the file that basemap needs
os.environ["PROJ_LIB"] = "C:\\Users\\WahlInstall\\"\
    "Anaconda3\\Library\\share\\basemap"
from mpl_toolkits.basemap import Basemap
from mpl_toolkits.axes_grid.inset_locator import inset_axes


os.chdir("G:\\report\\year-3\\07-Fall-2020\\#3Paper\\data\\"\
    "trend-analysis\\data\\allThreeTrends")

dat = pd.read_csv("95thTrendObsTwcrEra20c_30yrs_75perc.csv")

plt.hist(dat['obsTrendReg'] - dat['obsTrendMK'])
plt.show()


# plot 
sns.set_context('paper', font_scale = 1.5)

plt.figure(figsize=(20, 10))
m=Basemap(projection='cyl', lat_ts=20, llcrnrlon=-180, 
            urcrnrlon=180,llcrnrlat=-90,urcrnrlat=90, \
                resolution='c')
x,y = m(dat['lon'].tolist(), dat['lat'].tolist())
m.drawcoastlines()

#draw parallels and meridians 
parallels = np.arange(-80,81,20.)
m.drawparallels(parallels,labels=[True,False,False,False], \
                linewidth = 0)
m.drawmeridians(np.arange(0.,420.,30.),labels=[0,0,0,1], linewidth = 0) # draw meridians

m.bluemarble(alpha = 0.85)


cmap = plt.get_cmap("seismic")

# fix colorbar limits
norm = matplotlib.colors.Normalize(vmin=-1, vmax=1)


ax = sns.scatterplot(x = x, y = y, s = 70, c = cmap(norm(dat['obsTrendReg'] - dat['obsTrendMK'])), \
    palette = "seismic", norm = norm, data = dat, edgecolors='white', linewidth=0.4)

sm = plt.cm.ScalarMappable(cmap = "seismic", norm = norm)
sm.set_array([])
cbaxes = inset_axes(ax, width="40%", height = "3%", loc = 'lower center')
cbar = ax.figure.colorbar(sm, cax = cbaxes, orientation = 'horizontal')

# plt.savefig(fileName + ".svg", dpi = 400)

# # ax.get_legend().remove()
# cbaxes = inset_axes(ax, width="80%", height = "3%", loc = 3)
# ax.figure.colorbar(sm, cax = cbaxes, orientation = 'horizontal')

ax.set_title("Differences in Trend (mm) Linear Reg vs Mann-Kendal")

# plt.legend(loc = 3)

plt.show()