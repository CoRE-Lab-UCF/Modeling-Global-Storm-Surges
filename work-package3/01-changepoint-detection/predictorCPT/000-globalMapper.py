import os
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
#locate the file that basemap needs
os.environ["PROJ_LIB"] = "C:\\Users\\WahlInstall\\"\
    "Anaconda3\\Library\\share\\basemap"
from mpl_toolkits.basemap import Basemap

# image saving dir
dirOut = "G:\\report\\year-3\\07-Fall-2020\\#3Paper\\p28ThirdManuscript\\manuscript\\figures"


df = {
      'tg': ['astoria', 'fremantle', 'base_prat', 'ny_alesund', 'kerguelen'],
      'lon': [-123.77, 115.75, -59.633, 11.95, 70.22],
      'lat': [46.208, -32.053, -62.483, 78.933, -49.345]  
      }

dat = pd.DataFrame(data = df)

print(dat)


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

m.bluemarble(alpha = 0.5)
sns.scatterplot(x = x, y = y, s = 900, color = 'red',  
        data = dat, edgecolor='black', linewidth=0.4)

# plt.title("Length of ERA-20C Surge Reconstruction (Years) After Changepoint Analysis")

# plt.legend(loc = 3)

os.chdir(dirOut)
plt.savefig("outlierTideGaugesLocation.svg", dpi = 400)

# plt.show()