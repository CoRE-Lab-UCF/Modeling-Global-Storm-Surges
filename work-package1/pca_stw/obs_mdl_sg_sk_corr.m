% Correlation of modelled and observed surge
% Calclation of RMSE and relative RMSE
b_p = 'F:\OneDrive - Knights - University of Central Florida\Daten\MLR\PCA_Stepwise_confg_13'
cd(b_p)
lst = dir('*.mat'); %lst(1:2) = []; % making a list for the tg folders
for t_t = 1:length(lst)
    t_t
    load(lst(t_t).name); 
    cor_tbl(t_t,1) = lon_t;
    cor_tbl(t_t,2) = lat_t;
    cor_tbl(t_t,3) = corr(y_surge, y_recsurge);
    %cor_tbl(t_t,4) = corr(y_skew, y_recskew);
    xx = y_surge; yy = y_recsurge; zz = yy - xx; zsqr = zz.*zz; zmean = mean(zsqr); sg_rmse = sqrt(zmean);
    cor_tbl(t_t,5) = sg_rmse;
    cor_tbl(t_t,6) = sg_rmse*100/(max(y_surge) - min(y_surge));
    %xx = y_skew; yy = y_recskew; zz = yy - xx; zsqr = zz.*zz; zmean = mean(zsqr); sk_rmse = sqrt(zmean);
    %cor_tbl(t_t,7) = sk_rmse;
    %cor_tbl(t_t,8) = sk_rmse*100/(max(y_skew) - min(y_skew));
    clearvars -except b_p lst t cor_tbl
end

%% Plotting Surge Correlation 
load coast
geoshow(lat, long, 'DisplayType', 'polygon', 'Facecolor', [0.85 0.85 0.85]);
pt_sz = 80;
hold on; scatter(cor_tbl(:,1), cor_tbl(:,2), pt_sz, cor_tbl(:,3), 'filled')
title('Pearson Correlation Coefficent: observed and reconstructed daily maximum surge','FontSize',17 );
colormap('jet'); colorbar; colorbar('FontSize',12); caxis([0 0.9]); 
get(gca, 'XTick'); %change fontsize of the colorbar ticks
set(gca, 'FontSize', 12);
%% Plotting Skew Surge
load coast
figure; plot(long, lat, 'k')
pt_sz = 30;
hold on; scatter(cor_tbl(:,1), cor_tbl(:,2), pt_sz, cor_tbl(:,4), 'filled')
title('Pearson Correlation Coefficent: observed and reconstructed daily maximum skew surge','FontSize',17 );
colormap('jet'); colorbar; caxis([0 0.9]);
%% Plotting Surge RMSE
load coast
geoshow(lat, long, 'DisplayType', 'polygon', 'Facecolor', [0.85 0.85 0.85]);
pt_sz = 30;
hold on; scatter(cor_tbl(:,1), cor_tbl(:,2), pt_sz, cor_tbl(:,5)*100, 'filled')
title('RMSE (cm): Validation of reconstructed daily maximum surge','FontSize',17 );
colormap('jet'); colorbar; set(gca,'colorscale','log');
c = colorbar('XTickLabel', {'5','10','15','20','25','30','35'}, 'XTick', 5:5:30) %changing the scale to log to better visualize differences
%% Plotting Surge Relative RMSE
load coast
geoshow(lat, long, 'DisplayType', 'polygon', 'Facecolor', [0.85 0.85 0.85]);
pt_sz = 80;
hold on; scatter(cor_tbl(:,1), cor_tbl(:,2), pt_sz, cor_tbl(:,6), 'filled')
title('Relative RMSE (%): Validation of reconstructed daily maximum surge','FontSize',17 );
colormap('jet'); colorbar; set(gca,'colorscale','log');
c = colorbar('XTickLabel', {'5','10','15','20','25','30','35'}, 'XTick', 5:5:30) %changing the scale to log to better visualize differences
get(gca, 'XTick'); %change fontsize of the colorbar ticks
set(gca, 'FontSize', 12);
%% Plotting Skew RMSE
load coast
plot(long, lat, 'k')
pt_sz = 30;
hold on; scatter(cor_tbl(:,1), cor_tbl(:,2), pt_sz, cor_tbl(:,6)*100, 'filled')
title('RMSE (m): Validation of reconstructed daily maximum skew surge','FontSize',17 );
colormap('jet'); colorbar; set(gca,'colorscale','log');
c = colorbar('XTickLabel', {'5','10','15','20','25','30','35'}, 'XTick', 5:5:35); %changing the scale to log to better visualize differences