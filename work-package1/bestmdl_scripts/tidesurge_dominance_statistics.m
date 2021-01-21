%This script spits back the tide/surge dominance statistics for all tide
%gauges 

%load Model A .mat files
file_path = 'F:\OneDrive - Knights - University of Central Florida\Daten\MLR\best_model\tidesurge_combo'; 
out_path = 'F:\OneDrive - Knights - University of Central Florida\Daten\MLR\best_model\tidesurge_combo_figures'
cd (file_path)
stats_lst = dir('*.mat');

dom_stat = NaN(length(stats_lst), 4);
for m = 1:length(stats_lst)
    fprintf('%d tide gauges left . . . \n', length(stats_lst) - m);
    load(stats_lst(m).name);
    %concatenate |lon| lat | dominance_tide | dominance_surge   
    dom_stat(m,:) = [lon_t, lat_t, dominance_tide, dominance_surge];
    clearvars -except file_path out_path stats_lst dom_stat m
end
cd (out_path);
save('tidesurgedominance_stat.mat');