# -*- coding: utf-8 -*-
"""
Created on Mon Aug 24 14:25:27 2020

to get differences in annual max

@author: Michael Tadesse 
"""

#merge reconstruction and obs surge first



#reading files and preparing them for trend analysis

atlTwcr = pd.read_csv('atlantic_city-264a-usa-uhslc_twcrTrained19502011_Recon.csv')
#add surge
atlTwcr['date'] = pd.DataFrame(list(map(time_stamp, atlTwcr['date'])))
atlTwcrMerged = pd.merge(atlTwcr, atlSurge, on='date', how='left')

#find rows that have nans and remove them
row_nan = atlTwcrMerged[atlTwcrMerged.isna().any(axis =1)]
atlTwcrMerged.drop(row_nan.index, axis = 0, inplace = True)
atlTwcrMerged.reset_index(inplace = True)
atlTwcrMerged.drop('index', axis = 1, inplace = True)

#get the year
getYear = lambda x: x.split('-')[0]
getYear = lambda x: x.year
vicMergedEra20c['year'] = pd.DataFrame(list(map(getYear, vicMergedEra20c['date'])))




#get yearly metric values
dat = atlEra20cMerged.copy()
years = dat.year.unique().tolist()

metric = pd.DataFrame(columns = ['year', 'delta'])

for year in years:
    blockYear = dat[dat['year'] == year];
    blockMax = blockYear[blockYear['surge'] == blockYear['surge'].max()]
    print(blockMax, '\n')
    metricDelta = float(blockMax['surge_reconsturcted']) - float(blockMax['surge'])
    
    
    currentMetric = [year, metricDelta**2]
    print(year, " - ", metricDelta)
    
    metric.loc[len(metric)] = currentMetric
    
    
plt.figure()
plt.plot(brestMetric['year'], brestMetric['deltaEra20c'], label = 'Era-20C', color = 'magenta')
plt.plot(brestMetric['year'], brestMetric['deltaTwcr'], label = '20CR', color = 'green')
plt.title('Brest - 20CR vs Era-20C')
plt.ylabel('Square of Differences [m^2]')

#to get moving average 
twcrBrest['ma10Corr'] = twcrBrest['corr'].rolling(10).mean()





#to plot correlation/rmse moving average comparisons
#first get the files - from plotFiles folder
atlDat = pd.read_csv('atlanticCityCorrRMSENSE_Twcr.csv')

#plot
plt.figure(figsize = (14,8))
plt.plot(atlDat['year'], atlDat['corrTen'], label = 'Atlantic City', color = 'maroon')
plt.plot(vicDat['year'], vicDat['corrTen'], label = 'Victoria', color = 'darkcyan')
plt.plot(freDat['year'], freDat['corrTen'], label = 'Fremantle', color = 'navy')
plt.plot(brestDat['year'], brestDat['corrTen'], label = 'Brest', color = 'darkgreen')
plt.plot(hornbaekDat['year'], hornbaekDat['corrTen'], label = 'Hornbaek', color = 'orange')
plt.title('20CR - 10 year moving average - Correlation Coefficient')
plt.ylabel('Correlation')
