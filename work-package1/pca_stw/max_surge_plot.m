% Plotting Max Surge for TGs
b_p = 'F:\OneDrive - Knights - University of Central Florida\Daten\Tide_data\Surge_after_T_Tide'
cd(b_p)
lst = dir('*.mat');
for t_t = 1:length(lst)
    t_t
    load(lst(t_t).name);
    sg(t_t, 1) = Lon;
    sg(t_t, 2) = Lat;
    sg(t_t,3) = max(Surge);
    sg(t_t,4) = nanmean(Surge);
    sg(t_t,5) = nanmin(Surge);
end
clearvars -except sg;
a = [19 100 398 614 691];
sg_2 = sg; sg_2(a, :) = [];
%% Plotting Surge
load coast
figure; geoshow(lat, long, 'DisplayType', 'polygon', 'Facecolor', [0.85 0.85 0.85]);
pt_sz = 30;
hold on; scatter(sg_2(:,1), sg_2(:,2), sg_2(:,3)*20, 'filled')
title('Pearson Correlation Coefficent: observed and reconstructed daily maximum surge','FontSize',17 );
colormap('jet'); colorbar; colorbar('FontSize',12); caxis([0 0.9]); 
get(gca, 'XTick'); %change fontsize of the colorbar ticks
set(gca, 'FontSize', 12);