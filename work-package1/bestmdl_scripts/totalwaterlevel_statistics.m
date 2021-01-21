%The following script extracts totalwaterlevel statistics from all tide
%gauges and stores them to a separate .mat file

%load Model A .mat files
file_path = 'F:\OneDrive - Knights - University of Central Florida\Daten\MLR\best_model\tidesurge_combo'; 
out_path = 'F:\OneDrive - Knights - University of Central Florida\Daten\MLR\best_model\tidesurge_combo_figures\_matfiles'
cd (file_path)
stat_lst = dir('*.mat');

stat = NaN(length(stat_lst), 5);
for k = 1:length(stat_lst)
    fprintf('%d tide gauges left . . . \n', length(stat_lst) - k);
    load(stat_lst(k).name);
    %concatenate |lon| lat | correlation | rmse | nse |   
    stat(k,:) = [lon_t, lat_t, corr_waterlevel, rmse_waterlevel, nse_waterlevel];
    clearvars -except file_path out_path stat_lst stat k
end
cd (out_path);
save('totalwaterlevel_stat.mat');