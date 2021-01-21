# -*- coding: utf-8 -*-
"""
Created on Wed Apr 29 16:15:39 2020

Implementation of KFOLD

@author: Michael Tadesse
"""
import numpy as np
from sklearn import metrics
from scipy import stats
from sklearn.linear_model import LinearRegression
from sklearn.decomposition import PCA
from sklearn.model_selection import KFold
from sklearn.preprocessing import StandardScaler


#add squared and cubed wind terms
pickTerms = lambda x: x.startswith('wnd')
wndTerms = pred.columns[list(map(pickTerms, pred.columns))]
wnd_sqr = pred[wndTerms]**2
wnd_cbd = pred[wndTerms]**3
pred = pd.concat([pred, wnd_sqr, wnd_cbd], axis = 1)


#prepare data for reconstruction
pred_for_recon = pred[~pred.isna().any(axis = 1)]

#standardize matrix


#find size of X_pca to use also for X_recon
pca = PCA(86)
pca.fit(X_recon)
X_pca_recon = pca.transform(X_recon)

X_pca_recon = sm.add_constant(X_pca_recon)
predictions = est.get_prediction(X_pca_recon).summary_frame(alpha = 0.05)



#standardize predictor data



#apply pca on predictor matrix 
X = pred_surge.iloc[:,1:-1]
y = pd.DataFrame(pred_surge['surge'])
y = y.reset_index()
y.drop(['index'], axis = 1, inplace = True)

pca = PCA(.95)
pca.fit(X)
X_pca = pca.transform(X)



#apply 10 fold cross validation
kf = KFold(n_splits=10, random_state=29)

metric_corr = []; metric_rmse = []; combo = pd.DataFrame(columns = ['pred', 'obs'])
for train_index, test_index in kf.split(X):
    X_train, X_test = X_pca[train_index], X_pca[test_index]
    y_train, y_test = y['surge'][train_index], y['surge'][test_index]
    
    #train regression model
    lm = LinearRegression()
    lm.fit(X_train, y_train)
    
    #predictions
    predictions = lm.predict(X_test)
    pred_obs = pd.concat([pd.DataFrame(np.array(predictions)), pd.DataFrame(np.array(y_test))], \
                         axis = 1)
    pred_obs.columns = ['pred', 'obs']
    combo = pd.concat([combo, pred_obs], axis = 0)    
    
    #evaluation matrix - check p value
    if stats.pearsonr(y_test, predictions)[1] >= 0.05:
        print("insignificant correlation!")
        continue
    else:
        print(stats.pearsonr(y_test, predictions))
        metric_corr.append(stats.pearsonr(y_test, predictions)[0])
        print(np.sqrt(metrics.mean_squared_error(y_test, predictions)))
        metric_rmse.append(np.sqrt(metrics.mean_squared_error(y_test, predictions)))
        
print('avg_corr = ',np.mean(metric_corr), 'avg_rmse (m) = ', \
      np.mean(metric_rmse), '\n')
    
#regression using statsmodel
import statsmodels.api as sm
X_pca = sm.add_constant(X_pca)
est = sm.OLS(y['surge'], X_pca).fit()
est.summary()

X_pca_recon = sm.add_constant(X_pca_recon)

predictions = est.get_prediction(X_pca_recon).summary_frame(alpha = 0.05)
y_prd = predictions['mean'];
y_prd_ci_lower = predictions['obs_ci_lower'];
y_prd_ci_upper = predictions['obs_ci_upper'];

#plot 
time_stamp = lambda x: (datetime.strptime(x, '%Y-%m-%d %H:%M:%S'))

sns.set_context('notebook', font_scale = 2)
plt.figure()
plt.plot(surge_recon['date'], surge_recon['mean'], color = 'green')
plt.scatter(surge['date'], surge['surge'], color = 'blue')
plt.plot(surge_recon['date'], surge_recon['obs_ci_lower'], color = 'red',  linestyle = "--", lw = 0.8)
plt.plot(surge_recon['date'], surge_recon['obs_ci_upper'], color = 'red',  linestyle = "--", lw = 0.8)



#use complete time series to train model


##use extra time series (without surge data) to reconstruct
#remove nans from pred
pred[pred.isna().any(axis = 1)]

    
#comparing plot
plt.figure()
plt.scatter(surge['date'], surge['surge'], color = 'blue', s= 2)
plt.plot(surge_recon['date'], surge_recon['surge'], color = 'darkgreen')
plt.title('Zanzibar Reconstructed Surge (m) - Observation (blue)')
Out[335]: Text(0.5, 1.0, 'Zanzibar Reconstructed Surge (m) - Observation (blue)')
