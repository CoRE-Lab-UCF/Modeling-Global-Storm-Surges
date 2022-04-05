#get libraries
import os 
import pandas as pd 
from datetime import datetime
from statsmodels.tsa.seasonal import seasonal_decompose
import matplotlib.pyplot as plt

os.chdir("G:\\report\\year-3\\07-Fall-2020\\#3Paper\\data\\changePointTimeSeries"\
        "\\mamun-cpt-approach\\twcr\\08-postCPT")


time_stamp = lambda x: (datetime.strptime(x, '%Y-%m-%d %H:%M:%S'))

dat = pd.read_csv('adak,alaska_040a_usa.csv')
dat['date'] = pd.DataFrame(list(map(time_stamp, dat['date'])))

# print(dat)
# series = pd.DataFrame({'data': dat['surge_reconsturcted']}, index = dat['date'])

series = dat[['date', 'surge_reconsturcted']]
series.set_index('date', inplace = True)

print(series)

seasonal_decompose(series, model='additive', period = 365).plot()
plt.show()

# print(result.trend)
# print(result.seasonal)
# print(result.resid)
# print(result.observed)