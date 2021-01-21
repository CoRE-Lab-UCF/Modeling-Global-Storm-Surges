%Plotting the TG with correlation of 0.5 or below

cd 'F:\OneDrive - Knights - University of Central Florida\Daten\MLR\Sonstig'
load('Corr_0.5.mat');


for ii = 1:length(aa)
    load(aa(ii).name)
    figure; ss = scatter(y_surge, y_recsurge, '+', 'k');
    xlabel('Observed Surge(m)'); ylabel('Modelled Surge(m)');
        hline = refline([1, 0]); hline.Color = 'r'; set(hline, 'LineWidth', 2);
    toptitle = sprintf('%s', list_tg(t).name);
    title(toptitle);
    R = corr(y_surge, y_recsurge); R_squared = R^2;
    xx = y_surge; yy = y_recsurge; zz = yy - xx; zsqr = zz.*zz; zmean = mean(zsqr); sg_rmse = sqrt(zmean);
    text(-0.06, 0.30, ['R^2 = ' num2str(R_squared)], 'Color', 'red', 'FontSize', 12);
    text(-0.06, 0.25, ['RMSE = ' num2str(sg_rmse*100) 'cm'], 'Color', 'red', 'FontSize', 12);
    set(gca, 'Box', 'on', 'XMinorTick', 'on', 'YMinorTick', 'on', 'fontname', 'times');
    cd 'F:\OneDrive - Knights - University of Central Florida\Daten\MLR\Sonstig\scatterplots'
    c = strsplit(baseFileName,'_pca_stp.mat');
    d = sprintf('%s.jpeg', char(c(1)));
    saveas(figure(1),d);
    clearvars -except aa; close all;
end

