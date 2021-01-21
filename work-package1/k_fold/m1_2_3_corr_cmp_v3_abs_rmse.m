%To compare and plot the correlation of models 1,2 & 3

cd('F:\OneDrive - Knights - University of Central Florida\Daten\MLR\Model_2\Model_2_results')
load('abs_rmse_models_1_2_3_619TGs.mat')

for ii = 1:length(m123)
    ii
    if m123(ii,3) == max(m123(ii, 3:5))
        m123(ii,9) = m123(ii,3);
        m123(ii,10) = NaN;
        m123(ii,11) = NaN;
        m123(ii,12) = m123(ii,6);
        if m123(ii,12) == min(m123(ii,6:8))
            m123(ii, 13) = 1
        end
            
            
    elseif m123(ii,4) == max(m123(ii, 3:5))
        m123(ii,9) = NaN;
        m123(ii,10) = m123(ii,4);
        m123(ii,11) = NaN;
        m123(ii,12) = m123(ii,7);
        if m123(ii,12) == min(m123(ii,6:8))
            m123(ii, 13) = 1
        end
    else
        m123(ii,9) = NaN;
        m123(ii,10) = NaN;
        m123(ii,11) = m123(ii,5);
        m123(ii,12) = m123(ii,8);
        if m123(ii,12) == min(m123(ii,6:8))
            m123(ii, 13) = 1
        end

    end

end
cd('F:\OneDrive - Knights - University of Central Florida\Daten\MLR\Model_2\Model_2_results')
save('model_1_2_3_corr_abs_rmse_readyforplotcmp.mat')

%% plot the comparison
load coast
pt_sz = 80;
a1 = find(isfinite(m123(:,9)));
a2 = find(isfinite(m123(:,10)));
hold on; scatter(m123(a2,1), m123(a2,2), pt_sz, m123(a2,10), 's','filled') % plotting average rsquared
a3 = find(isfinite(m123(:,11)));
hold on; scatter(m123(a3,1), m123(a3,2), pt_sz, m123(a3,11),'filled') % plotting average rsquared

%plot rmse
figure; geoshow(lat, long, 'DisplayType', 'polygon', 'Facecolor', [0.85 0.85 0.85]);
pt_sz = 80;
hold on; scatter(m123(:,1), m123(:,2), pt_sz, m123(:,12)*100,'filled')
colormap('jet'); colorbar; colorbar('FontSize',12); %caxis([0 0.9]); 
colormap(flipud(jet));



















