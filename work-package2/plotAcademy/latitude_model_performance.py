# -*- coding: utf-8 -*-
"""
Created on Tue Feb 25 11:44:31 2020
Spatial distribution of average rmse (%) for Model-RS
Group latitudinal values of Model-RS and plot them on barplot
@author: Michael Tadesse
"""
import pandas as pd


#%% All three models in Model-RS

mdlrs_all = pd.read_csv('modelrs_all.csv', header=None) 
mdlrs_all.columns = ['lon', 'lat', 'corr', \
                   'pval', 'rmse', 'Relative RMSE', 'nse', 'model']

mdlrs_all['model'].replace(1, 'lrrs', inplace = True)
mdlrs_all['model'].replace(2, 'lrrslag', inplace = True)
mdlrs_all['model'].replace(3, 'rfrslag', inplace = True)


lrrs = mdlrs_all.loc[mdlrs_all['model'] == 'lrrs']
lrrslag = mdlrs_all.loc[mdlrs_all['model'] == 'lrrslag']
rfrslag = mdlrs_all.loc[mdlrs_all['model'] == 'rfrslag']

############
#Relative RMSE
############

#plotting horizontal barplots 
step = 20;
to_bin = lambda x: np.floor(x/step)*step
lrrs['latbin'] = lrrs.lat.map(to_bin);
lrrslag['latbin'] = lrrslag.lat.map(to_bin);
rfrslag['latbin'] = rfrslag.lat.map(to_bin);

g_lrrs = lrrs.groupby("latbin").median()
g_lrrs['model'] = "lrrs"
g_lrrslag = lrrslag.groupby("latbin").median()
g_lrrslag['model'] = "lrrslag"
g_rfrslag = rfrslag.groupby("latbin").median()
g_rfrslag['model'] = "rfrslag"



g_lrrs.reset_index(inplace = True)
g_lrrslag.reset_index(inplace = True)
g_rfrslag.reset_index(inplace = True)

g_lrrs.sort_values(by = ['latbin'], inplace = True, ascending=False)
g_lrrslag.sort_values(by = ['latbin'], inplace = True, ascending=False)
g_rfrslag.sort_values(by = ['latbin'], inplace = True, ascending=False)


model_rs = pd.concat([g_lrrs, g_lrrslag, g_rfrslag], axis = 0)
model_rs.reset_index(inplace = True)
model_rs.sort_values(by = ['latbin'], inplace = True, ascending=False)


#plotting
plt.figure(figsize = (12,8));
sns.barplot(x = 'Relative RMSE', y = 'latbin', \
            palette = "muted", data = model_rs, \
                hue = 'model', orient='h')
plt.ylabel('Latitude')
plt.xlabel('Relative RMSE (%)')
plt.title('Spatial Distribution of Average Relative RMSE (%)')
plt.xlim([0, 12])
#invert y axis
plt.gca().invert_yaxis() 
plt.savefig('lr_lrlag_rflag_relRMSE.svg', dpi = 400) # save as SVG


############
#correlation
############
mdlrs_all = pd.read_csv('modelrs_all.csv', header=None) 
mdlrs_all.columns = ['lon', 'lat', 'corr', \
                   'pval', 'rmse', 'Relative RMSE', 'nse', 'model']

mdlrs_all['model'].replace(1, 'lrrs', inplace = True)
mdlrs_all['model'].replace(2, 'lrrslag', inplace = True)
mdlrs_all['model'].replace(3, 'rfrslag', inplace = True)


lrrs = mdlrs_all.loc[mdlrs_all['model'] == 'lrrs']
lrrslag = mdlrs_all.loc[mdlrs_all['model'] == 'lrrslag']
rfrslag = mdlrs_all.loc[mdlrs_all['model'] == 'rfrslag']



#plotting horizontal barplots 
step = 20;
to_bin = lambda x: np.floor(x/step)*step
lrrs['latbin'] = lrrs.lat.map(to_bin);
lrrslag['latbin'] = lrrslag.lat.map(to_bin);
rfrslag['latbin'] = rfrslag.lat.map(to_bin);


g_lrrs = lrrs.groupby("latbin").median()
g_lrrs['model'] = "lrrs"
g_lrrslag = lrrslag.groupby("latbin").median()
g_lrrslag['model'] = "lrrslag"
g_rfrslag = rfrslag.groupby("latbin").median()
g_rfrslag['model'] = "rfrslag"


g_lrrs.reset_index(inplace = True)
g_lrrslag.reset_index(inplace = True)
g_rfrslag.reset_index(inplace = True)


mdlrs = pd.concat([g_lrrs, g_lrrslag, g_rfrslag], axis = 0)

#plotting
plt.figure(figsize = (12,8));
sns.barplot(x = 'corr', y = 'latbin', \
            palette = "muted", data = mdlrs, \
                hue = 'model', orient='h')
plt.ylabel('Latitude')
plt.xlabel('Correlation')
plt.title('Spatial Distribution of Average Correlation')
plt.xlim([0, 1])
#invert y axis
plt.gca().invert_yaxis() 
plt.savefig('lr_lrlag_rflag_corr.svg', dpi = 400) # save as SVG


#%% For best model - Model-RS
best_rs = pd.read_csv('modelrs.csv', header=None) 
best_rs.columns = ['lon', 'lat', 'model', 'corr', \
                   'pval', 'rmse', 'Relative RMSE', 'nse']
best_rs['model'].replace(1, 'lrrs', inplace = True)
best_rs['model'].replace(2, 'lrrslag', inplace = True)
best_rs['model'].replace(3, 'rfrslag', inplace = True)


#plotting horizontal barplots 
step = 20;
to_bin = lambda x: np.floor(x/step)*step
best_rs['latbin'] = best_rs.lat.map(to_bin);

g_bestrs = best_rs.groupby("latbin").median()


g_bestrs.reset_index(inplace = True)


#adding number of tide gauges in each band

bestrs_num = best_rs.groupby("latbin")
tg_num = bestrs_num.count()['nse']
tg_num = pd.DataFrame(tg_num)
# tg_num.sort_values(by = 'latbin', ascending=False, inplace = True)
tg_num.reset_index(inplace = True)
g_bestrs['tg_num'] = tg_num['nse']


step = 50;
to_bin = lambda x: np.floor(x/step)*step
g_bestrs['tg'] = g_bestrs.tg_num.map(to_bin);


#######################
#plotting relative rmse
#######################
plt.figure(figsize = (12,8));
sns.barplot(x = 'Relative RMSE', y = 'latbin', \
            palette = "muted", data = g_bestrs, \
                hue = 'tg_num', orient='h')
plt.ylabel('Latitude')
plt.xlabel('Relative RMSE (%)')
plt.title('Model-RS: Spatial Distribution of Average Relative RMSE (%)')
plt.xlim([0, 12])
#invert y axis
plt.gca().invert_yaxis()
plt.savefig('model_rs_relRMSE_v2.svg') # save as SVG


#######################
#plotting correlation
#######################
plt.figure(figsize = (12,8));
sns.barplot(x = 'corr', y = 'latbin', \
            palette = "muted", data = g_bestrs, \
                hue = 'tg_num', orient='h')
plt.ylabel('Latitude')
plt.xlabel('Correlation')
plt.title('Model-RS: Spatial Distribution of Average Correlation')
plt.xlim([0, 1])
#invert y axis
plt.gca().invert_yaxis()
plt.savefig('model_rs_corr.svg') # save as SVG



#%% For total still water levels - extremes - >95th percentile

tsw_rs = pd.read_csv('tsw_extreme_modelrs.csv', header=None) 
tsw_rs.columns = ['lon', 'lat', 'tid_dom', 'corr', \
                   'pval', 'rmse', 'Relative RMSE', 'nse']

#plotting horizontal barplots 
step = 20;
to_bin = lambda x: np.floor(x/step)*step
tsw_rs['latbin'] = tsw_rs.lat.map(to_bin);

g_tswrs = tsw_rs.groupby("latbin").median()


g_tswrs.reset_index(inplace = True)



#adding number of tide gauges in each band

tswrs_num = tsw_rs.groupby("latbin")
tg_num = tswrs_num.count()['nse']
tg_num = pd.DataFrame(tg_num)
# tg_num.sort_values(by = 'latbin', ascending=False, inplace = True)
tg_num.reset_index(inplace = True)
g_tswrs['tg_num'] = tg_num['nse']


step = 50;
to_bin = lambda x: np.floor(x/step)*step
g_tswrs['tg'] = g_tswrs.tg_num.map(to_bin);

#######################
#plotting relative rmse
#######################
plt.figure(figsize = (12,8));
sns.barplot(x = 'Relative RMSE', y = 'latbin', \
            palette = "muted", data = g_tswrs, \
                hue = 'tg_num', orient='h')
plt.ylabel('Latitude')
plt.xlabel('Relative RMSE (%)')
plt.title('Model-RS: Spatial Distribution of Average Relative RMSE for Extreme Total Still Water Levels (%)')
plt.xlim([0, 12])
#invert y axis
plt.gca().invert_yaxis()
plt.savefig('tsl_modelrs_relRMSE_v2.svg') # save as SVG


#######################
#plotting correltaion
#######################
plt.figure(figsize = (12,8));
sns.barplot(x = 'corr', y = 'latbin', \
            palette = "muted", data = g_tswrs, \
                hue = 'tg_num', orient='h')
plt.ylabel('Latitude')
plt.xlabel('Correlation')
plt.title('Model-RS: Spatial Distribution of Average Correlation for Extreme Total Still Water Levels (%)')
plt.xlim([0, 1])
#invert y axis
plt.gca().invert_yaxis()
plt.savefig('tsl_modelrs_corr.svg') # save as SVG

























