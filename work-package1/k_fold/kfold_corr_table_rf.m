% Create a correlation & rmse table for all TGs after Kfold RF
bas_pat = 'F:\OneDrive - Knights - University of Central Florida\Daten\MLR\RF_Kfold_10X10_17_yrs'
cd(bas_pat);
lst = dir(); lst(1:2) = [];%dir('*.mat');
for ii = 1:length(lst)
    ii
    cd(fullfile(bas_pat, lst(ii).name))
    mat_lst = dir('*.mat'); 
    load(mat_lst.name);
    dt(ii, 1) = lon_t;
    dt(ii,2) = lat_t;
    dt(ii,3) = r_avg;
    dt(ii,4) = rsq_avg;
    dt(ii,5) = rmse_avg;
    dt(ii,6) = rmse_avg*100/(max(y_surge) - min(y_surge));
    clearvars -except bas_pat lst ii dt
end
cd('F:\OneDrive - Knights - University of Central Florida\Daten\MLR\Sonstig')
save('RF_kfold_10X10_17yrs.mat', 'dt')
