
%% In order to localize predictors 
% Choosing Tide gauge
cd 'D:\OneDrive - Knights - University of Central Florida\Daten\MLR\Test_gauges'
list_gauge = dir('*.mat');

for gg = 129:length(list_gauge)
    gg
    list_gauge(gg).name
    load(list_gauge(gg).name)
    
    % Check if corresponding skew/surge file is available, otherwise skip
%     cd 'C:\Users\mi292519\OneDrive - Knights - University of Central Florida\Daten\Tide_data\Skew_surge_max_full'
%     id_name = strcat(list_gauge(gg).name, '_sk.mat');
%     
%     if ~exist(id_name)
%         continue;
%     end
    
    
    lat_t = Lat; lon_t = Lon; % Latitude and Longitude for tide gauge
    clearvars -except lat_t lon_t gg list_gauge
    
    % Loading predictor information
    % Predictor Wind
    disp('1. Predictor - Wind')
    cd 'D:\OneDrive - Knights - University of Central Florida\Daten\Remote Sensing\CCMP'
    wind_mat = dir('*.mat');
    umax_daily = []; vmax_daily = []; Twind = [];
    for ii = 1:length(wind_mat)
        yname = wind_mat(ii).name;
        fprintf('Analyzing %s\n', yname);
        load(yname);

        Tpred = Thour; lat_pred = Lat; lon_pred = Lon; %Thour, Lat and Lon for the predictors
        clearvars -except Tpred udmax vdmax lat_pred lon_pred lat_t lon_t ii wind_mat umax_daily vmax_daily Twind gg list_gauge

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
    cd 'D:\OneDrive - Knights - University of Central Florida\Daten\MLR\TG_pct_pcd_17yrs'
    save_as = strsplit(list_gauge(gg).name, '.mat');
    save_nam = strcat(save_as, '_17yrs');
    mkdir(save_nam{1}); cd(save_nam{1});
    clearvars udmax vdmax udmax_sub vdmax_sub Tpred wind_mat ii;
    save('CCMP.mat');

    clearvars -except lat_t lon_t save_nam gg list_gauge

    %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
    
    % Predictor - Precipitation
    disp('2. Predictor - Precipitation')
    cd 'D:\OneDrive - Knights - University of Central Florida\Daten\Remote Sensing\GPCP'
    gpcp_mat = dir('*.mat');

    gpcp_daily = [];  Tgpcp = [];
    for ii = 1:length(gpcp_mat)
        yname = gpcp_mat(ii).name;
        fprintf('Analyzing %s\n', yname);
        load(yname);
        Tpred = T;
        clearvars -except gpcp Tpred Tgpcp lat_pred lon_pred lat_t lon_t ii gpcp_mat gpcp_daily gg list_gauge save_nam

        % Define the grid
        lat_ind = find(lat_pred >= lat_t - 5 & lat_pred <= lat_t + 5); % find latitude within this range
        lon_ind = find(lon_pred >= lon_t - 5 & lon_pred <= lon_t + 5);

        new_lat = lat_pred(lat_ind); new_lon = lon_pred(lon_ind);

        gpcp_sub = gpcp(lon_ind, lat_ind, :); % subset predictor data

        gpcp_daily = cat(3, gpcp_daily, gpcp_sub);
        Tgpcp = cat(1, Tgpcp, Tpred);
    end
    
    cd 'D:\OneDrive - Knights - University of Central Florida\Daten\MLR\TG_pct_pcd_17yrs'
    cd(save_nam{1})
    clearvars gpcp gpcp_sub Tpred ii gpcp_mat;
    save('GPCP.mat');

    clearvars -except lat_t lon_t gg list_gauge save_nam

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
    % Predictor - Mean Sea-level pressure
    disp('3. Predictor - Sea-level Pressure')
    cd 'D:\OneDrive - Knights - University of Central Florida\Daten\Remote Sensing\SLP'
    prmsl_mat = dir('*.mat');

    prmsl_daily = [];  Tprmsl = [];
    for ii = 1:length(prmsl_mat)
        yname = prmsl_mat(ii).name;
        fprintf('Analyzing %s\n', yname);
        load(yname);
        clearvars -except slp_daily Tpred Tprmsl lat_pred lon_pred lat_t lon_t ii prmsl_mat prmsl_daily gg list_gauge save_nam

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

    cd 'D:\OneDrive - Knights - University of Central Florida\Daten\MLR\TG_pct_pcd_17yrs'
    cd(save_nam{1})
    clearvars slp_daily prmsl_sub Tpred ii prmsl_mat;
    save('PRMSL.mat');

    clearvars -except lat_t lon_t gg list_gauge save_nam

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
    % Predictor SST
    disp('4. Predictor - SST')
    cd 'D:\OneDrive - Knights - University of Central Florida\Daten\Remote Sensing\SST'
    sst_mat = dir('*.mat');
    sst_daily = []; Tsst = [];
    for ii = 1:length(sst_mat)
        yname = sst_mat(ii).name;
        fprintf('Analyzing %s\n', yname);
        load(yname);

        Tpred = T; lat_pred = Lat; lon_pred = Lon; %Thour, Lat and Lon for the predictors
        clearvars -except Tpred sst lat_pred lon_pred lat_t lon_t ii sst_mat sst_daily Tsst gg list_gauge save_nam

        % Define the grid
        lat_ind = find(lat_pred >= lat_t - 5 & lat_pred <= lat_t + 5); % find latitude within this range
        lon_ind = find(lon_pred >= lon_t - 5 & lon_pred <= lon_t + 5);

        new_lat = lat_pred(lat_ind); new_lon = lon_pred(lon_ind);
        sst_sub = sst(lon_ind, lat_ind, :); % subset predictor data

        sst_daily = cat(3, sst_daily, sst_sub);
        Tsst = cat(1, Tsst, Tpred);
    end
    cd 'D:\OneDrive - Knights - University of Central Florida\Daten\MLR\TG_pct_pcd_17yrs'
    cd(save_nam{1})    
    clearvars sst sst_sub Tpred sst_mat ii;
    save('SST.mat');

    clearvars -except lat_t lon_t gg list_gauge save_nam
    
    % Predictand
    
    disp('5. Predictand - Surge/Skew surge')
    base_path = fullfile('D:\OneDrive - Knights - University of Central Florida\Daten\MLR\TG_pct_pcd_17yrs', save_nam{1});
    cd 'D:\OneDrive - Knights - University of Central Florida\Daten\Tide_data\Surge_after_T_Tide'
    id_name = strcat(list_gauge(gg).name, '.mat');
    copyfile(id_name, base_path);
    
    %Making daily surge values
    disp('Computing daily maximum surge');
    cd(base_path)
    load(id_name);
    surge_hr = [Thour Surge];
    surge_daily = [];%surge_hr(~isfinite(surge_hr(:,2)),:) = [];
    aa = datevec(surge_hr(:,1)); 
    bb = datetime(aa(:,1:3)); 
    cc = unique(bb); % making a unique list of the days
    for ss = 1:length(cc)
        ind = find(cc(ss) == bb);
        d = surge_hr(ind,2);
        e = max(d); % Picking the daily max surge
        surge_daily = [surge_daily; [datenum(cc(ss)) e]];
    end
    clearvars aa bb cc d e ind basepath folder
    save_name = sprintf('%s_daily.mat', save_nam{1});
    save(save_name);
    cd 'D:\OneDrive - Knights - University of Central Florida\Daten\MLR\Test_gauges'

    
end
















