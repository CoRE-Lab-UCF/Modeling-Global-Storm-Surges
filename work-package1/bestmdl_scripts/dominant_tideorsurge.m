%This program finds the dominant constituent of total water level; tide or
%surge in percent
%created @ 08/26/2019

%load Model A .mat files
file_path = 'F:\OneDrive - Knights - University of Central Florida\Daten\MLR\best_model\tidesurge_combo'; 
cd (file_path)
dom_lst = dir('*.mat');

for j = 1:length(dom_lst)
    fprintf('%d tide gauges left . . . \n', length(dom_lst) - j);
    load(dom_lst(j).name);
    %percentage of tide/surge in totalwaterlevel
    dominance_tide = mean(abs(total_waterlevel(:,2))*100./...
        (abs(total_waterlevel(:,2)) + abs(total_waterlevel(:,3))));
    dominance_surge = mean(abs(total_waterlevel(:,3))*100./...
        (abs(total_waterlevel(:,2)) + abs(total_waterlevel(:,3))));
    save(strcat(tide_name1{1}, '_tide_surge.mat'));
end
