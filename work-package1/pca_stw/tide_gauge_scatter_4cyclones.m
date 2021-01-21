% Correlation of modelled and observed surge
b_p = 'F:\OneDrive - Knights - University of Central Florida\Daten\MLR\PCA_Stepwise_confg_13'
cd(b_p)
lst = dir('*.mat'); %lst(1:2) = []; % making a list for the tg folders
for t_t = 1:length(lst)
    t_t
    load(lst(t_t).name); 
    cor_tbl(t_t).name = lst(t_t).name;
    cor_tbl(t_t).longitude = lon_t;
    cor_tbl(t_t).latitude = lat_t;
    %y = datevec(Thour);
    %cor_tbl(t_t,3) = length(unique(y(:,1)));
    clearvars -except b_p lst t cor_tbl
end

%% Plotting Tide Gauges
load coast
geoshow(lat, long, 'DisplayType', 'polygon', 'Facecolor', [0.85 0.85 0.85]);
pt_sz = 30;
hold on; 
for ii = 1:length(lst)
    scatter(cor_tbl(ii).longitude, cor_tbl(ii).latitude, 'filled')
end

%%
tt_tt = datevec(Twind);
tt_ty = find(tt_tt(:,2) >5 & tt_tt(:,2) < 12);
ty_recsurge = y_recsurge(tt_ty);
ty_surge = y_surge(tt_ty);
figure; scatter(ty_surge, ty_recsurge)
hline = refline([1, 0]); hline.Color = 'r'; set(hline, 'LineWidth', 2);
xlabel('Observed Surge'); ylabel('Modelled Surge'); title('Correlation during the Typhoon season - 5 Years')


nty_surge = y_surge;
nty_surge(tt_ty, :) = [];
nty_recsurge = y_recsurge;
nty_recsurge(tt_ty, :) = [];
figure; scatter(nty_surge, nty_recsurge)
hline = refline([1, 0]); hline.Color = 'r'; set(hline, 'LineWidth', 2);
xlabel('Observed Surge'); ylabel('Modelled Surge'); title('Correlation during the Non-Typhoon season - 5 Years')

%%

scatter(cor_tbl(:,1), cor_tbl(:,2), cor_tbl(:,3), 'b','filled') %hold on; scatter(cor_tbl(:,1), cor_tbl(:,2), pt_sz, cor_tbl(:,3), 'filled')
title('Location of available GESLA-2 tide gauge records in years','FontSize',17 );
colormap('jet'); colorbar; set(gca,'colorscale','log');
c = colorbar('XTickLabel', {'20','40','60','80','100','120','140', '160', '180'}, 'XTick', 20:20:180)

%% Plotting according to size
load coast
figure; geoshow(lat, long, 'DisplayType', 'polygon', 'Facecolor', [0.85 0.85 0.85]);
hold on; scatter(cor_tbl(:,1), cor_tbl(:,2), cor_tbl(:,3), cor_tbl(:,3), 'filled')
%title('Location of available GESLA-2 tide gauge records in years','FontSize',17 );
colormap('jet'); set(gca,'colorscale','log'); colorbar;
c = colorbar('XTickLabel', {'20','60','100','140', '180'}, 'XTick', 20:40:180)
title('Location of available GESLA-2 tide gauge records in years','FontSize',17 );


