%plotting script for figure 4 %

%loading figures
cd 'F:\OneDrive - Knights - University of Central Florida\UCF\Projekt.28\Report\Spring 2019\#1 - Paper\Review\source_files\comment65'
corr = hgload('ModelA_pearson_corr.fig');
rmse = hgload('ModelA_rmse.fig');
rel_rmse = hgload('ModelA_rel_rmse.fig');

figure; h(1)=subplot(3,1,1); 
copyobj(allchild(get(corr,'CurrentAxes')),h(1));

