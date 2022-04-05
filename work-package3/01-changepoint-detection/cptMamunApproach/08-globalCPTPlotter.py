import os
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
#locate the file that basemap needs
os.environ["PROJ_LIB"] = "C:\\Users\\WahlInstall\\"\
    "Anaconda3\\Library\\share\\basemap";
from mpl_toolkits.basemap import Basemap
from mpl_toolkits.axes_grid.inset_locator import inset_axes

home = "G:\\report\\year-3\\07-Fall-2020\\#3Paper\\data\\changePointTimeSeries\\"\
        "mamun-cpt-approach\\era20c\\06-globalCpt"

os.chdir(home)
#change file name here
dat = pd.read_csv('era20cGlobalCPT.csv')
dat.drop('Unnamed: 0', axis = 1, inplace = True)
print(dat)

#increase plot font size
sns.set_context('notebook', font_scale = 1.5)

plt.figure(figsize=(20, 10))
m=Basemap(projection='cyl', lat_ts=20, llcrnrlon=-180, 
          urcrnrlon=180,llcrnrlat=-90,urcrnrlat=90, resolution='c')
x,y = m(dat['lon'].tolist(), dat['lat'].tolist())
m.drawcoastlines()


#get degree signs 
parallels = np.arange(-80,81,20.)
meridians = np.arange(-180.,180.,40.)
#labels = [left,right,top,bottom]
m.drawparallels(parallels,labels=[True,True,False,False], \
                linewidth = 0.5)
m.drawmeridians(meridians,labels=[False,False,False,True], \
                linewidth = 0.5)

m.bluemarble(alpha = .82)


ax = sns.scatterplot(x = x, y = y, s = 70, hue= 'year', palette = 'hot_r',  \
                    data = dat)
# m.colorbar(location = 'bottom')

#add colorbar for years
norm = plt.Normalize(dat['year'].min(), dat['year'].max())
sm = plt.cm.ScalarMappable(cmap = "hot_r", norm = norm)
sm.set_array([])

ax.get_legend().remove()
cbaxes = inset_axes(ax, width="80%", height = "3%", loc = 3)
ax.figure.colorbar(sm, cax = cbaxes, orientation = 'horizontal')


ax.legend(loc = 'lower left', ncol = 3)
# plt.title(title)

# plt.show()

# # save as svg
#change save name here
saveName = 'era20cGlobalCpt.svg'
plt.savefig(saveName, dpi = 400)