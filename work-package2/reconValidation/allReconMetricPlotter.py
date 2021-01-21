# -*- coding: utf-8 -*-
"""
Created on Thu Jul 16 12:34:24 2020

To plot validation metrics for all reconstructions

@author: Michael Tadesse
"""


plt.figure(figsize = (12,8))
plt.plot(twcrCorr['corrn'], twcrCorr['band'], label = '20CR', color = 'green', alpha = 0.4)
plt.plot(era20cCorr['corrn'], era20cCorr['band'], label = 'ERA20C', color = 'magenta', alpha = 0.4)
plt.plot(eraintCorr['corrn'], eraintCorr['band'], label = 'ERA-Int', color = 'black', alpha = 0.4)
plt.plot(merraCorr['corrn'], merraCorr['band'], label = 'MERRA', color = 'red', alpha = 0.4)
plt.legend()

plt.scatter(twcrCorr['corrn'], twcrCorr['band'], label = '20CR', color = 'green')
plt.scatter(era20cCorr['corrn'], era20cCorr['band'], label = 'ERA20C', color = 'magenta')
plt.scatter(eraintCorr['corrn'], eraintCorr['band'], label = 'ERA-Int', color = 'black')
plt.scatter(merraCorr['corrn'], merraCorr['band'], label = 'MERRA', color = 'red')

plt.xlabel("Pearson's Correlation")
plt.ylabel("Latitude")
plt.title("Model Validation for 1980-2010 period")