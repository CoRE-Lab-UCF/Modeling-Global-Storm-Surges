cd 'F:\OneDrive - Knights - University of Central Florida\Daten\MLR\PCA_Stepwise_confg_13'
lst = dir('*.mat');
for ii = 1:length(lst)
    load(lst(ii).name)
    clearvars -except vars y_surge
    aa = randi(length())

    
end