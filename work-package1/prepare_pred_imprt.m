% this script prepares the vars|y_rec|indx|lon|lat variables in a single %
% csv file %

cd 'F:\OneDrive - Knights - University of Central Florida\Daten\MLR\Model_2\04_01_2019\M2_Kfold_randomized_v2'
tg_lst = dir('*.mat');


for ii = 1:1%length(tg_lst)
    load(tg_lst(ii).name);
    clearvars -except tg_lst ii lon_t lat_t vars y_rec y_surge indx
    dat = [y_surge(:,1) vars y_surge(:,2) y_rec(:,2)];
    dat_size = size(dat);
    dat(:,dat_size(2) + 1) = lon_t;
    dat(:,dat_size(2) + 2) = lon_t;
    dat = [dat indx];

end                                                                      
