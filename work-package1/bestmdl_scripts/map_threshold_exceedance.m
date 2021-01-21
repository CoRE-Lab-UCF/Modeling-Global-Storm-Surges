% To map error statistics for threshold exceedance % 

fold = 'F:\OneDrive - Knights - University of Central Florida\Daten\MLR\best_model\Threshold_Exceeding_statistics' % source folder
cd(fold)
lst_qunt = dir('*.mat')

% to collect only significant correlations
for ii = 1:length(lst_qunt)
    ii
    load(lst_qunt(ii).name)
    qq(ii, 1:2) = [lon_t lat_t];
    
    n = 2; % the first two columns taken by lon and lat
    for jj = 1:length(qunt)
        if qunt{4,jj} == 1
            rmse = qunt{3,jj}; % taking rmse of siginificantly correlated values
        else
            rmse = NaN;
        end

        qq(ii, jj+n:jj+n+1) = [qunt{5,jj}(:,1) rmse]; % corr and rmse for surge > 70, 80 90 95 99 percentiles
        n = n+1; 
        %columns 3, 5, 7, 9, 11 -> correlations
    end
    
   
end
