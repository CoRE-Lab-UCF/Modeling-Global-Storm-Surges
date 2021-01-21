%% Choosing Tide gauge
cd 'C:\Users\mi292519\OneDrive - Knights - University of Central Florida\Daten\Tide_data\TG_mat_global_unique'
load('astoria,or-572a-usa-uhslc');
lat_t = Lat; lon_t = Lon; % Latitude and Longitude for tide gauge
clearvars -except lat_t lon_t


%% Loading predictor information
% Predictor Wind
disp('1. Predictor - Wind')
cd 'C:\Users\mi292519\OneDrive - Knights - University of Central Florida\Daten\Remote Sensing\CCMP'
wind_mat = dir('*.mat');
umax_daily = []; vmax_daily = []; Twind = [];
for ii = 1:length(wind_mat)
    yname = wind_mat(ii).name;
    fprintf('Analyzing %s\n', yname);
    load(yname);
    
    Tpred = Thour; lat_pred = Lat; lon_pred = Lon; %Thour, Lat and Lon for the predictors
    clearvars -except Tpred udmax vdmax lat_pred lon_pred lat_t lon_t ii wind_mat umax_daily vmax_daily Twind

    % Define the grid
    lat_ind = find(lat_pred >= lat_t - 5 & lat_pred <= lat_t + 5); % find latitude within this range
    if lon_t < 0
        lon_ind = find(lon_pred >= (lon_t+360) - 5 & lon_pred <= (lon_t+360) + 5);
    else
        lon_ind = find(lon_pred >= lon_t - 5 & lon_pred <= lon_t + 5);
    end
    new_lat = lat_pred(lat_ind); new_lon = lon_pred(lon_ind);
    udmax_sub = udmax(lon_ind, lat_ind, :); % subset predictor data
    vdmax_sub = vdmax(lon_ind, lat_ind, :);
    
    umax_daily = cat(3, umax_daily, udmax_sub);
    vmax_daily = cat(3, vmax_daily, vdmax_sub);
    Twind = cat(1, Twind, Tpred);
end
cd 'C:\Users\mi292519\OneDrive - Knights - University of Central Florida\Daten\MLR'
clearvars udmax vdmax udmax_sub vdmax_sub Tpred wind_mat ii;
save('CCMP.mat');
    
clearvars -except lat_t lon_t

%% Predictor - Precipitation
disp('2. Predictor - Precipitation')
cd 'C:\Users\mi292519\OneDrive - Knights - University of Central Florida\Daten\Remote Sensing\GPCP\GPCP_test'
gpcp_mat = dir('*.mat');

gpcp_daily = [];  Tgpcp = [];
for ii = 1:length(gpcp_mat)
    yname = gpcp_mat(ii).name;
    fprintf('Analyzing %s\n', yname);
    load(yname);
    Tpred = T;
    clearvars -except gpcp Tpred Tgpcp lat_pred lon_pred lat_t lon_t ii gpcp_mat gpcp_daily

    % Define the grid
    lat_ind = find(lat_pred >= lat_t - 5 & lat_pred <= lat_t + 5); % find latitude within this range
    lon_ind = find(lon_pred >= lon_t - 5 & lon_pred <= lon_t + 5);

    new_lat = lat_pred(lat_ind); new_lon = lon_pred(lon_ind);

    gpcp_sub = gpcp(lon_ind, lat_ind, :); % subset predictor data
    
    gpcp_daily = cat(3, gpcp_daily, gpcp_sub);
    Tgpcp = cat(1, Tgpcp, Tpred);
end

cd 'C:\Users\mi292519\OneDrive - Knights - University of Central Florida\Daten\MLR'
clearvars gpcp gpcp_sub Tpred ii gpcp_mat;
save('GPCP.mat');
    
clearvars -except lat_t lon_t


%% Predictor - Mean Sea-level pressure
disp('3. Predictor - Sea-level Pressure')
cd 'C:\Users\mi292519\OneDrive - Knights - University of Central Florida\Daten\Remote Sensing\SLP\SLP_test'
prmsl_mat = dir('*.mat');

prmsl_daily = [];  Tprmsl = [];
for ii = 1:length(prmsl_mat)
    yname = prmsl_mat(ii).name;
    fprintf('Analyzing %s\n', yname);
    load(yname);
    clearvars -except slp_daily Tpred Tprmsl lat_pred lon_pred lat_t lon_t ii prmsl_mat prmsl_daily
    
    % Define the grid
    lat_ind = find(lat_pred >= lat_t - 5 & lat_pred <= lat_t + 5); % find latitude within this range
    if lon_t < 0
        lon_ind = find(lon_pred >= (lon_t+360) - 5 & lon_pred <= (lon_t+360) + 5);
    else
        lon_ind = find(lon_pred >= lon_t - 5 & lon_pred <= lon_t + 5);
    end

    new_lat = lat_pred(lat_ind); new_lon = lon_pred(lon_ind);

    prmsl_sub = slp_daily(lon_ind, lat_ind, :); % subset predictor data
    prmsl_daily = cat(3, prmsl_daily, prmsl_sub);
    Tprmsl = cat(1, Tprmsl, Tpred);
end

cd 'C:\Users\mi292519\OneDrive - Knights - University of Central Florida\Daten\MLR'
clearvars slp_daily prmsl_sub Tpred ii prmsl_mat;
save('PRMSL.mat');
    
clearvars -except lat_t lon_t

%% Predictor SST
disp('4. Predictor - SST')
cd 'C:\Users\mi292519\OneDrive - Knights - University of Central Florida\Daten\Remote Sensing\SST\SST_test'
sst_mat = dir('*.mat');
sst_daily = []; Tsst = [];
for ii = 1:length(sst_mat)
    yname = sst_mat(ii).name;
    fprintf('Analyzing %s\n', yname);
    load(yname);
    
    Tpred = T; lat_pred = Lat; lon_pred = Lon; %Thour, Lat and Lon for the predictors
    clearvars -except Tpred sst lat_pred lon_pred lat_t lon_t ii sst_mat sst_daily Tsst

    % Define the grid
    lat_ind = find(lat_pred >= lat_t - 5 & lat_pred <= lat_t + 5); % find latitude within this range
    lon_ind = find(lon_pred >= lon_t - 5 & lon_pred <= lon_t + 5);
 
    new_lat = lat_pred(lat_ind); new_lon = lon_pred(lon_ind);
    sst_sub = sst(lon_ind, lat_ind, :); % subset predictor data
   
    sst_daily = cat(3, sst_daily, sst_sub);
    Tsst = cat(1, Tsst, Tpred);
end
cd 'C:\Users\mi292519\OneDrive - Knights - University of Central Florida\Daten\MLR'
clearvars sst sst_sub Tpred sst_mat ii;
save('SST.mat');
    
clearvars -except lat_t lon_t


%% Predictand + Predictor

% Load surge/skew surge data

cd 'C:\Users\mi292519\OneDrive - Knights - University of Central Florida\Daten\Tide_data\Skew_surge'
load('astoria,or-572a-usa-uhslc.mat_mean_sk.mat')
clearvars -except sk_daily surge_daily

% Refine CCMP data to match surge time series

cd 'C:\Users\mi292519\OneDrive - Knights - University of Central Florida\Daten\MLR'
load('CCMP.mat')
clearvars -except vmax_daily umax_daily Twind surge_daily sk_daily

ymd_pred = datevec(Twind); %predictor year, month, date format
ymd_mat = datenum(ymd_pred(:,1:3)); % taking only the ymd format to extract daily values of predictors

pp_ind = []; % index of surge_daily where surge and predictor have common dates

if length(surge_daily) > length(ymd_mat)
    for pp = 1:length(Twind)
        pp_ind = [pp_ind; find(ymd_mat(pp) == surge_daily(:,1))];
    end
    
    surge_new = surge_daily(pp_ind,:); %surge values matching predictor date
    umax_new = umax_daily(:,:,find(isfinite(pp_ind))); % choosing only predictors without nans
    vmax_new = vmax_daily(:,:, find(isfinite(pp_ind)));

else
    for pp = 1:length(Twind)
        pp_ind = [pp_ind; find(surge_daily(:,1) == ymd_mat(pp))];
    end 
    
    umax_new = umax_daily(:,:,pp_ind); 
    vmax_new = vmax_daily(:,:,pp_ind);
    surge_new = surge_daily(find(isfinite(pp_ind)),:);
end


