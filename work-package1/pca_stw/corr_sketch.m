%% uwnd plot
% in order to plot correlation of surge/skew surge with predctors
usqr = umaxd.*umaxd; 
ucub = umaxd.*umaxd.*umaxd;

for ii = 1:u1
    for jj = 1:u2 
        z = size(umaxd(ii, jj, :));
        u_squz = reshape(umaxd(ii, jj, :), z(2:end))'; % just transform it to a vector for corr
        sg_u_corr(ii,jj) = corr(u_squz, surged(:,2), 'Rows', 'complete');
    end
end
subplot(2, 2, 1);
figure; mymap = pcolor(new_lon, new_lat, sg_u_corr'); 
colormap('jet'); colorbar; caxis([0 1]); 
mymap.EdgeAlpha = 0;
load coast; hold on; plot(long, lat, 'k', 'LineWidth', 2);
hold on; scatter(Lon, Lat, 'k', 'r', 'LineWidth', 8);
plot_name = sprintf('%s uwnd Vs Surge', baseFileName);
title(plot_name);

find(sg_u_corr >= 0.95*max(sg_u_corr(:)));
[ro co] = find(sg_u_corr >= 0.95*max(sg_u_corr(:)));
max_95 = [ro co];

for mm = 1:length(max_95)
    max_95(mm,3) = sg_u_corr(max_95(mm,1), max_95(mm,2));
end

scatter(new_lon(max_95(:,1)), new_lat(max_95(:,2)), 15);

%% vwnd plot
for ii = 1:v1
    for jj = 1:v2 
        z = size(vmaxd(ii, jj, :));
        v_squz = reshape(vmaxd(ii, jj, :), z(2:end))'; % just transform it to a vector for corr
        sg_v_corr(ii,jj) = corr(v_squz, surged(:,2), 'Rows', 'complete');
    end
end

subplot(3, 2, 2); 
figure; mymap = pcolor(new_lon, new_lat, sg_v_corr'); 
colormap('jet'); colorbar; caxis([0 1]);
mymap.EdgeAlpha = 0;
load coast; hold on; plot(long, lat, 'k');
hold on; scatter(Lon, Lat, 'k', 'r', 'LineWidth', 8);
plot_name = sprintf('%s vwnd Vs Surge', baseFileName);
title(plot_name);

find(sg_v_corr >= 0.95*max(sg_v_corr(:)));
[ro co] = find(sg_v_corr >= 0.95*max(sg_v_corr(:)));
max_95 = [ro co];

for mm = 1:length(max_95)
    max_95(mm,3) = sg_v_corr(max_95(mm,1), max_95(mm,2));
end

scatter(new_lon(max_95(:,1)), new_lat(max_95(:,2)), 15);


%% 
for ii = 1:s1
    for jj = 1:s2 
        z = size(sstd(ii, jj, :));
        s_squz = reshape(sstd(ii, jj, :), z(2:end))'; % just transform it to a vector for corr
        sg_s_corr(ii,jj) = corr(s_squz, surged(:,2), 'Rows', 'complete');
    end
end

subplot(3, 2, 3); 
figure; mymap = pcolor(new_lon, new_lat, sg_s_corr'); 
colorbar; caxis([0 1]);
mymap.EdgeAlpha = 0;
load coast; hold on; plot(long, lat, 'k');
hold on; scatter(Lon, Lat, 'k', 'r', 'LineWidth', 8);
plot_name = sprintf('%s SST Vs Surge', baseFileName);
title(plot_name);



%% 
for ii = 1:p1
    for jj = 1:p2 
        z = size(prmsld(ii, jj, :));
        p_squz = reshape(prmsld(ii, jj, :), z(2:end))'; % just transform it to a vector for corr
        sg_p_corr(ii,jj) = corr(p_squz, surged(:,2), 'Rows', 'complete');
    end
end

subplot(3, 2, 4); 
figure; mymap = pcolor(new_lon, new_lat, sg_p_corr'); 
colorbar; caxis([-1 0]); colormap('jet');
oldcmp = colormap; colormap(flipud(oldcmp));
mymap.EdgeAlpha = 0;
load coast; hold on; plot(long, lat, 'k');
hold on; scatter(Lon, Lat, 'k', 'r', 'LineWidth', 8);
plot_name = sprintf('%s SLP Vs Surge', baseFileName);
title(plot_name);

[ro co] = find(abs(sg_p_corr) >= 0.95*max(abs(sg_p_corr(:))));
max_95 = [ro co];

for mm = 1:length(max_95)
    max_95(mm,3) = sg_p_corr(max_95(mm,1), max_95(mm,2));
end

scatter(new_lon(max_95(:,1)), new_lat(max_95(:,2)), 15);


%% 
for ii = 1:g1
    for jj = 1:g2 
        z = size(gpcpd(ii, jj, :));
        g_squz = reshape(gpcpd(ii, jj, :), z(2:end))'; % just transform it to a vector for corr
        sg_g_corr(ii,jj) = corr(g_squz, surged(:,2), 'Rows', 'complete');
    end
end

figure; mymap = pcolor(new_lon, new_lat, sg_g_corr'); 
colorbar; caxis([0 1]); colormap('jet')
mymap.EdgeAlpha = 0;
load coast; hold on; plot(long, lat, 'k');
hold on; scatter(Lon, Lat, 'k', 'r', 'LineWidth', 8);
plot_name = sprintf('%s Precipication Vs Surge', baseFileName);
title(plot_name);