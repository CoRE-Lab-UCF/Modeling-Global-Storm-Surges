% To compute the lambda metric %

cd 'D:\OneDrive - Knights - University of Central Florida\Daten\Reanalysis\ERA_Interim\Models\bestmdl_b\BestMdl_b'
lst_mb = dir('*.mat')
mdlb_metric = NaN(length(lst_mb), 4);
for ii = 1:length(lst_mb)
    ii
    load(lst_mb(ii).name)
    clearvars -except lat_t lon_t y_surge y_rec rho ii lst_mb mdlb_metric
    a = y_rec(:,2) - y_surge(:,2);
    aa = a.*a; 
    b = y_surge(:,2) - mean(y_surge(:,2)); 
    bb = b.*b; 
    c = y_rec(:,2) - mean(y_rec(:,2));
    cc = c.*c;
    d = length(y_surge(:,2))*(mean(y_surge(:,2)) - mean(y_rec(:,2)))^2;
    lambda = 1- (sum(aa)/(sum(bb) + sum(cc) + d));
    mdlb_metric(ii,:) = [lon_t lat_t rho lambda];
end