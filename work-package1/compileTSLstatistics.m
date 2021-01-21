% extract tide surge combination statistics for global mapping %
%load Model A .mat files
input = 'F:\OneDrive - Knights - University of Central Florida\Daten\MLR\best_model\tidesurge_combo_95ile'; 
output = 'F:\OneDrive - Knights - University of Central Florida\UCF\Projekt.28\Report\Spring 2019\#1 - Paper\Review\source_files\comment2';
cd (input)
c_lst = dir('*.mat');

tideSurge_stat = NaN(length(c_lst), 8);
for cc = 1:length(c_lst)
    cc
    cd(input)
    load(c_lst(cc).name);
    tideSurge_stat(cc,:) = [lon_t, lat_t, dominance_tide, rho, pval, rmse_waterlevel, rel_rmse, nse_waterlevel];
    clearvars -except input output c_lst cc tideSurge_stat
end



