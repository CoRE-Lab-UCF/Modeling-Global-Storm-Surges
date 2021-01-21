%To make a matrix of correlation of all the TGs from the model results

bas_pat = 'F:\OneDrive - Knights - University of Central Florida\Daten\MLR\Model_1\RF_Kfold_10X10_17_yrs'
cd(bas_pat);
lst_new = dir(); lst_new(1:2) = [];%dir('*.mat');
for ii = 1:length(lst_new)
    ii
    cd(fullfile(bas_pat, lst_new(ii).name))
    mat_lst = dir('*.mat'); 
    load(mat_lst.name);
    dat(ii, 1) = lon_t;
    dat(ii,2) = lat_t;
    dat(ii,3) = r_avg;
    dat(ii,4) = rsq_avg;
    dat(ii,5) = rmse_avg;
    dat(ii,6) = rmse_avg*100/(max(y_surge) - min(y_surge));
    clearvars -except bas_pat lst_new ii dat
end
cd('F:\OneDrive - Knights - University of Central Florida\Daten\MLR\Model_2\Model_2_results')
save('RF_4Xdaily_kfold_mdl_1p0_732TGs.mat', 'dat')
