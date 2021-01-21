%To compare and plot the correlation of models 1,2 & 3

cd('F:\OneDrive - Knights - University of Central Florida\Daten\MLR\Model_2\Model_2_results')
load('pre_model_1_2_3_corr_cmp.mat')

for ii = 1:length(cc)
    ii
    if cc(ii,3) == max(cc(ii, 3:5))
        cc(ii,6) = cc(ii,3);
        cc(ii,7) = NaN;
        cc(ii,8) = NaN;
    elseif cc(ii,4) == max(cc(ii, 3:5))
        cc(ii,6) = NaN;
        cc(ii,7) = cc(ii,4);
        cc(ii,8) = NaN;
    else
        cc(ii,6) = NaN;
        cc(ii,7) = NaN;
        cc(ii,8) = cc(ii,5);

    end

end
cd('F:\OneDrive - Knights - University of Central Florida\Daten\MLR\Model_2\Model_2_results')
save('model_1_2_3_corr_cmp.mat', 'cc')

%% plot the comparison
load coast
figure; geoshow(lat, long, 'DisplayType', 'polygon', 'Facecolor', [0.85 0.85 0.85]);
pt_sz = 80;
a1 = find(isfinite(cc(:,6)));
hold on; scatter(cc(a1,1), cc(a1,2), pt_sz, cc(a1,6), 'd', 'filled') % plotting average rsquared
colormap('jet'); colorbar; colorbar('FontSize',12); caxis([0 0.9]); 
a2 = find(isfinite(cc(:,7)));
hold on; scatter(cc(a2,1), cc(a2,2), pt_sz, cc(a2,7), 's','filled') % plotting average rsquared
a3 = find(isfinite(cc(:,8)));
hold on; scatter(cc(a3,1), cc(a3,2), pt_sz, cc(a3,8),'filled') % plotting average rsquared




















