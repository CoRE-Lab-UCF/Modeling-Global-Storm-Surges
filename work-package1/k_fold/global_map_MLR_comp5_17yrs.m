cd 'F:\OneDrive - Knights - University of Central Florida\Daten\MLR\Sonstig'
load('MLR_comp_m2p1_m1_449TGs.mat')
load coast
figure; geoshow(lat, long, 'DisplayType', 'polygon', 'Facecolor', [0.85 0.85 0.85]);
pt_sz = 50;
dff = (DAT(:,3) - DAT(:,4))*100./DAT(:,3);
hold on; scatter(DAT(:,1), DAT(:,2), pt_sz, dff, 'filled') % plotting average rsquared
title('MLR (10X10) - Improvement of correlation after using longer time series (%)','FontSize',17 );
colormap('jet'); colorbar; colorbar('FontSize',12); %caxis([-60 20]); 
get(gca, 'XTick'); %change fontsize of the colorbar ticks
%set(gca, 'FontSize', 12);

figure; geoshow(lat, long, 'DisplayType', 'polygon', 'Facecolor', [0.85 0.85 0.85]);
pt_sz = 50;
dff_rmse = (DAT(:,5) - DAT(:,6))*100./DAT(:,5);
hold on; scatter(DAT(:,1), DAT(:,2), pt_sz, dff_rmse, 'filled') % plotting average rsquared
title('MLR: Improvement of relative rmse after using longer time series (%)','FontSize',17 );
colormap('jet'); colorbar; colorbar('FontSize',12); %caxis([-10 40]); 
get(gca, 'XTick'); %change fontsize of the colorbar ticks
set(gca, 'FontSize', 12);