% compute the 95%ile of total still water level %
% created 02/24/2020 %

%load Model A .mat files
file_path = 'F:\OneDrive - Knights - University of Central Florida\Daten\MLR\best_model\tidesurge_combo'; 
out_path = 'F:\OneDrive - Knights - University of Central Florida\Daten\MLR\best_model\tidesurge_combo_95ile';
cd (file_path)
my_lst = dir('*.mat');

for xx = 1:length(my_lst)
    xx
    cd(file_path)
    load(my_lst(xx).name);
    clearvars -except y_surge file_path out_path my_lst xx total_waterlevel lat_t lon_t
    tsl95 = quantile(total_waterlevel(:,5), 0.95);
    ind_total = find(total_waterlevel(:,5) >= tsl95);
    total95 = total_waterlevel(ind_total, :);
    
    %tidal dominance
    dominance_tide = mean(abs(total95(:,2))*100./...
        (abs(total95(:,5))));
    
    %statistics
    [rho pval] = corr(total95(:,5), total95(:,6));
    %rmse
    zz = total95(:,5) - total95(:,6); zsqr = zz.*zz; 
    zmean = mean(zsqr); 
    rmse_waterlevel = sqrt(zmean);
    %rel.rmse
    dif = max(y_surge(:,2)) - min(y_surge(:,2));
    rel_rmse = rmse_waterlevel*100/dif;
    
    %nse
    x1 = total95(:,5) - mean(total95(:,5)); x1sqr = x1.*x1;
    nse_waterlevel = 1- (sum(zsqr)/sum(x1sqr));
    cd(out_path)
    save(my_lst(xx).name)
end

