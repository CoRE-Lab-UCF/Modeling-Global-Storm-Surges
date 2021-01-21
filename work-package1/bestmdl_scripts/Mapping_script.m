% To map out correlation and rmse results from MLR model

cd 'F:\OneDrive - Knights - University of Central Florida\Daten\MLR\Model_2'
load('MLR_4Xdaily_kfold_mdl2p2_449TGs.mat')

load coast
figure; geoshow(lat, long, 'DisplayType', 'polygon', 'Facecolor', [0.85 0.85 0.85]);
pt_sz = 70;
hold on; scatter(dat(:,1), dat(:,2), pt_sz, dat(:,3), 'filled') % plotting average rsquared
title('MLR (4Xdaily - 10X10) - Pearson Correlation Coefficent: observed and reconstructed daily maximum surge','FontSize',17 );
colormap('jet'); colorbar; colorbar('FontSize',12); %caxis([0 0.9]); 
get(gca, 'XTick'); %change fontsize of the colorbar ticks
set(gca, 'FontSize', 12);

figure; geoshow(lat, long, 'DisplayType', 'polygon', 'Facecolor', [0.85 0.85 0.85]);
pt_sz = 80;
hold on; scatter(dat(:,1), dat(:,2), pt_sz, dat(:,5)*100, 'filled') % plotting average rsquared
title('Relative RMSE - MLR: observed and reconstructed daily maximum surge','FontSize',17 );
colormap('jet'); colorbar; colorbar('FontSize',12); %caxis([0 0.9]); 
get(gca, 'XTick'); %change fontsize of the colorbar ticks
set(gca, 'FontSize', 12);
