% To calculate quantiles of daily max surge % 

go2 = 'F:\OneDrive - Knights - University of Central Florida\Daten\MLR\Model_2\Extracted'
cd(go2);
folds = dir('*10X10');

for jc = 1:length(folds)
    jc
    cd(fullfile(go2, folds(jc).name))
    load('surge_dmax.mat')
    surge_quant(jc,1:2) = [lon_t lat_t];
    surge_quant(jc, 3) = quantile(surge_sub(:,2), 0.9); % 90 percentile
    surge_quant(jc, 4) = quantile(surge_sub(:,2), 0.95); % 95 percentile
    surge_quant(jc, 5) = quantile(surge_sub(:,2), 0.99); % 99 percentile
    surge_quant(jc, 6) = quantile(surge_sub(:,2), 0.995); % 99.5 percentile
    surge_quant(jc, 7) = quantile(surge_sub(:,2), 0.999); % 99.9 percentile
end