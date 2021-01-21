%% Get list of file names

cd('..\TG_mat_global_unique')

% Get list with file names
list = dir('*');
list(1:2) = [];

% load nameu.mat

%% Run loop for tidal analysis with T_Tide for all sites seperately

for ii = 1:length(list)
    ii
    fname = list(ii).name;
    load(fname)
    
    cd('..\Tidal_analysis_NASA')
    
    % Pass on to Tide_analysis
    [ TCa, TCae, TCp, TCpe, Mt, pred, nameu ] = Tide_analysis(Thour,Whour_detr,Lat);
    Surge = Whour_detr-pred;
    Tide = pred;
    
%     % identify and remove outliers from the fit
%     out = find(Surge_in(:,i)>nanmean(Surge_in(:,i))+5*nanstd(Surge_in(:,i)) | Surge_in(:,i)<nanmean(Surge_in(:,i))-5*nanstd(Surge_in(:,i)));
%     SL1(out,i) = NaN;
%     [ TCa, TCae, TCp, TCpe, Mt, pred(:,i), nameu ] = Tidemaster( SL_t, SL1(:,i), Lat(i,1), 'nameu' );
%     Surge(:,i) = SL(:,i)-pred(:,i);
       
end