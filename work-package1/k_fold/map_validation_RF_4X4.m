bas_pat = 'D:\OneDrive - Knights - University of Central Florida\Daten\MLR\RF_K_Fold4x4'
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
cd('D:\OneDrive - Knights - University of Central Florida\Daten\MLR\Sonstig')
save('RF_kfold_4X4.mat', 'dt')
