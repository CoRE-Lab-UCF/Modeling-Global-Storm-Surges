cd 'F:\OneDrive - Knights - University of Central Florida\Daten\MLR\Sonstig'
load('RF_kfold_10X10_17yrs.mat')
load coast
figure; geoshow(lat, long, 'DisplayType', 'polygon', 'Facecolor', [0.85 0.85 0.85]);
pt_sz = 50;
hold on; scatter(dt(:,1), dt(:,2), pt_sz, dt(:,3), 'filled') % plotting average rsquared
title('Random Forest (17 years) - Pearson Correlation Coefficent: observed and reconstructed daily maximum surge','FontSize',17 );
colormap('jet'); colorbar; colorbar('FontSize',12); %caxis([0 0.9]); 
get(gca, 'XTick'); %change fontsize of the colorbar ticks
set(gca, 'FontSize', 12);


figure; geoshow(lat, long, 'DisplayType', 'polygon', 'Facecolor', [0.85 0.85 0.85]);
pt_sz = 50;
hold on; scatter(dt(:,1), dt(:,2), pt_sz, dt(:,6), 'filled') % plotting average rsquared
title('Relative RMSE (10X10 - 17 years) - RF: observed and reconstructed daily maximum surge','FontSize',17 );
colormap('jet'); colorbar; colorbar('FontSize',12); %caxis([0 0.9]); 
get(gca, 'XTick'); %change fontsize of the colorbar ticks
set(gca, 'FontSize', 12);