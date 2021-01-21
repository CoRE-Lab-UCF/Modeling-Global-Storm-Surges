%% Plotting predictors associated with a specific surge
cd 'F:\OneDrive - Knights - University of Central Florida\Daten\MLR\PCA_Stepwise_confg_13'

%% Load the pca+stepwise regression result file for the tide gauge
figure; 
obs_mdl = [Twind y_surge y_recsurge];
ss = scatter(obs_mdl(:,2), obs_mdl(:,3), '+', 'k');
xlabel('Observed Surge(m)'); ylabel('Modelled Surge(m)');
hline = refline([1, 0]); hline.Color = 'r'; set(hline, 'LineWidth', 2);
toptitle = sprintf('%s', list_tg(t).name);
title(toptitle); 
R = corr(y_surge, y_recsurge); R_squared = R^2;
xx = y_surge; yy = y_recsurge; zz = yy - xx; zsqr = zz.*zz; zmean = mean(zsqr); sg_rmse = sqrt(zmean);
text(-0.06, 0.18, ['R^2 = ' num2str(R_squared)], 'Color', 'red', 'FontSize', 12);
text(-0.06, 0.15, ['RMSE = ' num2str(sg_rmse*100) 'cm'], 'Color', 'red', 'FontSize', 12);
set(gca, 'Box', 'on', 'XMinorTick', 'on', 'YMinorTick', 'on', 'fontname', 'times');

%% Add the cursor_info at this point
a_a = find(obs_mdl(:,2) == cursor_info.Position(1,1) & obs_mdl(:,3) == cursor_info.Position(1,2))
a_tt = datevec(Twind(a_a));
clearvars -except obs_mdl a_a a_tt lon_t lat_t baseFileName

%% Load Wind Data
cd 'F:\OneDrive - Knights - University of Central Florida\Daten\Remote Sensing\CCMP'
bb = sprintf('%s%d.mat', 'Y',a_tt(1));
load(bb);
d_tt = datevec(Thour);
c_c = find(d_tt(:,1) == a_tt(1)& d_tt(:,2) == a_tt(2)& d_tt(:,3) == a_tt(3)); % to find the time when the cursor_info lies 

%% plot udmax - Zonal Wind Speed
load coast; figure;
map2 = pcolor(Lon, Lat, (udmax(:,:,c_c))')
map2.EdgeAlpha = 0; hold on;
plot(long, lat, 'k'); plot(long+360, lat, 'k');
colormap('jet'); colorbar;
scatter(lon_t+360, lat_t, 100, 'o', 'k', 'filled');
c = strsplit(baseFileName, '-');
toptitle = sprintf('%s - Zonal Wind Speed  @ %s', char(c(1)), datetime(a_tt));
title(toptitle);

%% plot vdmax - Meridional Wind Speed
load coast; figure;
map2 = pcolor(Lon, Lat, (vdmax(:,:,c_c))')
map2.EdgeAlpha = 0; hold on;
plot(long+360, lat, 'k'); plot(long+360, lat, 'k');
colormap('jet'); colorbar;
scatter(lon_t, lat_t, 100, 'o', 'k', 'filled');
toptitle = sprintf('%s - Meridional Wind Speed @ %s', char(c(1)), datetime(a_tt));
title(toptitle);

%% Plot resultant wind speed
wnd_res = sqrt(udmax(:,:,c_c).*udmax(:,:,c_c) + vdmax(:,:,c_c).*vdmax(:,:,c_c));
figure;
map2 = pcolor(Lon, Lat, wnd_res');
map2.EdgeAlpha = 0; hold on;
plot(long, lat, 'w'); plot(long+360, lat, 'w');
colormap('jet'); colorbar;
scatter(lon_t+360, lat_t, 100, 'o', 'w', 'filled');
toptitle = sprintf('%s - Resultant Wind Speed @ %s', char(c(1)), datetime(a_tt));
title(toptitle)
clearvars -except obs_mdl a_a a_tt lon_t lat_t baseFileName
%% Load Sea level pressure Data
cd 'F:\OneDrive - Knights - University of Central Florida\Daten\Remote Sensing\SLP\SLP_test'
bb = sprintf('%s%d%s.mat', 'prmsl.',a_tt(1),'.nc');
load(bb);
d_tt = datevec(Tpred);
c_c = find(d_tt(:,1) == a_tt(1)& d_tt(:,2) == a_tt(2)& d_tt(:,3) == a_tt(3)); % to find the time when the cursor_info lies 
%% plot prmsl
load coast; figure;
map2 = pcolor(lon_pred, lat_pred, (slp_daily(:,:,c_c))')
map2.EdgeAlpha = 0; hold on;
plot(long, lat, 'k'); plot(long+360, lat, 'k');
colormap('jet'); colorbar;
oldcmp = colormap; colormap(flipud(oldcmp));
scatter(lon_t+360, lat_t, 100, 'o', 'k', 'filled');
c = strsplit(baseFileName, '-');
toptitle = sprintf('%s - Sea level pressure  @ %s', char(c(1)), datetime(a_tt));
title(toptitle);









































