%To compare and plot the correlation of models 1,2 & 3

cd('F:\OneDrive - Knights - University of Central Florida\Daten\MLR\Model_2\Model_2_results')
load('model_1_2_3_corr_abs_rmse_readyforplotcmp.mat')

for ii = 1:length(m123_732)
    ii
    if m123_732(ii,3) == max(m123_732(ii, 3:5))
        m123_732(ii,12) = m123_732(ii,3);
        m123_732(ii,13) = NaN;
        m123_732(ii,14) = NaN;
        m123_732(ii,15) = m123_732(ii,6); %abs rmse
        m123_732(ii,16) = m123_732(ii,9); %rel rmse
    elseif m123_732(ii,4) == max(m123_732(ii, 3:5))
        m123_732(ii,12) = NaN;
        m123_732(ii,13) = m123_732(ii,4);
        m123_732(ii,14) = NaN;
        m123_732(ii,15) = m123_732(ii,7);
        m123_732(ii,16) = m123_732(ii,10);
    else
        m123_732(ii,12) = NaN;
        m123_732(ii,13) = NaN;
        m123_732(ii,14) = m123_732(ii,5);
        m123_732(ii,15) = m123_732(ii,8);
        m123_732(ii,16) = m123_732(ii,11);

    end

end
cd('F:\OneDrive - Knights - University of Central Florida\Daten\MLR\Model_2\Model_2_results')
save('m123_corr_rmse_ready4plot_732TGs.mat')

%% plot the comparison
load coast
pt_sz = 80;
a1 = find(isfinite(m123_732(:,12)));
a2 = find(isfinite(m123_732(:,13)));
figure; geoshow(lat, long, 'DisplayType', 'polygon', 'Facecolor', [0.85 0.85 0.85]);
hold on; scatter(m123_732(a1,1), m123_732(a1,2), pt_sz, m123_732(a1,12), 'd','filled')
colormap('jet'); colorbar; colorbar('FontSize',12); caxis([0 0.9]); 
hold on; scatter(m123_732(a2,1), m123_732(a2,2), pt_sz, m123_732(a2,13), 's','filled') 
a3 = find(isfinite(m123_732(:,14)));
hold on; scatter(m123_732(a3,1), m123_732(a3,2), pt_sz, m123_732(a3,14),'filled') 


figure; geoshow(lat, long, 'DisplayType', 'polygon', 'Facecolor', [0.85 0.85 0.85]);
pt_sz = 80;
hold on; scatter(m123_732(:,1), m123_732(:,2), pt_sz, m123_732(:,12),'filled')
colormap('jet'); colorbar; colorbar('FontSize',12); %caxis([0 0.9]); 
colormap(flipud(hot));



















