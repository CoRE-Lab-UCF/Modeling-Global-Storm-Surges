#implementation of qunatile reegression
#source - 'http://subramgo.github.io/2017/03/13/Quantile-Regression/'

import os 
import numpy as np
import pandas as pd 
from datetime import datetime
import statsmodels.formula.api as smf
import matplotlib.pyplot as plt

os.chdir("G:\\report\\year-3\\07-Fall-2020\\#3Paper\\data\\changePointTimeSeries"\
        "\\mamun-cpt-approach\\twcr\\08-postCPT")

dat = pd.read_csv("adak,alaska_040a_usa.csv")

time_stamp = lambda x: (datetime.strptime(x, '%Y-%m-%d %H:%M:%S'))
dat['date'] = pd.DataFrame(list(map(time_stamp, dat['date'])))

df = pd.DataFrame(dat['surge_reconsturcted'])
df.reset_index(inplace = True)
df.drop('index', axis = 1, inplace = True)
df.reset_index(inplace = True)
df['index'] = df['index'] + 1
print(df)


mod = smf.quantreg('surge_reconsturcted ~ index', df)
res = mod.fit(q = .5)
print(res.summary())


quantiles = np.arange(.05, .96, .1)
def fit_model(q):
    res = mod.fit(q=q)
    return [q, res.params['Intercept'], res.params['index']] + \
            res.conf_int().loc['index'].tolist()

models = [fit_model(x) for x in quantiles]
models = pd.DataFrame(models, columns=['q', 'a', 'b', 'lb', 'ub'])

ols = smf.ols('surge_reconsturcted ~ index', df).fit()
ols_ci = ols.conf_int().loc['index'].tolist()
ols = dict(a = ols.params['Intercept'],
           b = ols.params['index'],
           lb = ols_ci[0],
           ub = ols_ci[1])

print(models)
print(ols)



x = np.arange(df.index.min(), df.index.max(), 50)
get_y = lambda a, b: a + b * x

fig, ax = plt.subplots(figsize=(8, 6))

for i in range(models.shape[0]):
    y = get_y(models.a[i], models.b[i])
    ax.plot(x, y, linestyle='dotted', color='grey')

y = get_y(ols['a'], ols['b'])

ax.plot(x, y, color='red', label='OLS')
ax.scatter(df.index, df.surge_reconsturcted, alpha=.2)
# ax.set_xlim((240, 3000))
# ax.set_ylim((240, 2000))
legend = ax.legend()
ax.set_xlabel('Index', fontsize=16)
ax.set_ylabel('Surge Height (m)', fontsize=16);
plt.show()



# #plot time series
# plt.figure(figsize=(10,4))
# plt.scatter(dat['date'], dat['surge_reconsturcted'])
# plt.show()

#plot scatterplot
# plt.figure(figsize=(4,6))
# plt.scatter(dat['date'], dat['surge_reconsturcted'])
# plt.show()

# print(dat)


