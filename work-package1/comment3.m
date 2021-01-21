% plot the correlation and rmse for extreme (>95%) surge %

cd 'F:\OneDrive - Knights - University of Central Florida\Daten\MLR\best_model\Threshold_Exceeding_statistics'

tg_lst = dir('*.mat');
cor_rms95 = NaN(length(tg_lst), 4);


for ii = 1:length(tg_lst)
    ii
    load(tg_lst(ii).name);
    clearvars -except tg_lst ii cor_rms95 lon_t lat_t qunt
    
    %correlation
    a = corr(qunt{1,4}(:,1), qunt{1,4}(:,2));
    %rmse
    b = rmse(qunt{1,4}(:,1), qunt{1,4}(:,2));
    
    cor_rms95(ii,:) = [lon_t lat_t a b];
    clear a b qunt lon_t lat_t 
    
end


