%% Choosing Tide gauge
cd 'F:\OneDrive - Knights - University of Central Florida\Daten\MLR\Test_gauges'
list_gauge = dir('*.mat');

for gg = 1:length(list_gauge)
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
    % Predictor - uwnd
    disp('1. Predictor - uwnd')
    cd 'F:\OneDrive - Knights - University of Central Florida\Daten\Remote Sensing\CCMP\CCMP_4Xdaily'
    uwnd_mat = dir('*u4x_daily.mat');
    u4xd10 = []; Tuwnd = [];
    for ii = 1:2%length(uwnd_mat)
        ii
        yname = uwnd_mat(ii).name;
        fprintf('Analyzing %s\n', yname);
        load(yname);

        Tpred = Thour; lat_pred = Lat; lon_pred = Lon; %Thour, Lat and Lon for the predictors
        clearvars -except Tpred lat_pred lon_pred lat_t lon_t ii uwnd_mat u4xdaily u4xd10 Tuwnd gg list_gauge
%%
        % Define the grid
        lat_ind = find(lat_pred >= lat_t - 5 & lat_pred <= lat_t + 5); % find latitude within this range
        if lon_t < 0
            lon_ind = find(lon_pred >= (lon_t+360) - 5 & lon_pred <= (lon_t+360) + 5);
        else
            lon_ind = find(lon_pred >= lon_t - 5 & lon_pred <= lon_t + 5);
        end
        new_lat = lat_pred(lat_ind); new_lon = lon_pred(lon_ind);
        u4xdaily_sub = u4xdaily(lon_ind, lat_ind, :); % subset predictor data
%%
        u4xd10 = cat(3, u4xd10, u4xdaily_sub);
        Tuwnd = cat(1, Tuwnd, Tpred);
    end
    cd 'F:\OneDrive - Knights - University of Central Florida\Daten\MLR\TG_pct_pcd_17yrs_4xdaily_10x10'
    save_as = strsplit(list_gauge(gg).name, '.mat');
    save_nam = strcat(save_as, '_17yrs_4d10x10');
    mkdir(save_nam{1}); cd(save_nam{1});
    clearvars u4xdaily u4xdaily_sub Tpred uwnd_mat ii;
    save('uwnd.mat');

    clearvars -except lat_t lon_t save_nam gg list_gauge

%% Predictor - vwnd
    disp('1. Predictor - vwnd')
    cd 'F:\OneDrive - Knights - University of Central Florida\Daten\Remote Sensing\CCMP\CCMP_4Xdaily'
    vwnd_mat = dir('*v4x_daily.mat');
    v4xd10 = []; Tvwnd = [];
    for ii = 1:2%length(uwnd_mat)
        ii
        yname = vwnd_mat(ii).name;
        fprintf('Analyzing %s\n', yname);
        load(yname);

        Tpred = Thour; lat_pred = Lat; lon_pred = Lon; %Thour, Lat and Lon for the predictors
        clearvars -except Tpred lat_pred lon_pred lat_t lon_t ii vwnd_mat v4xdaily v4xd10 Tvwnd gg list_gauge

        % Define the grid
        lat_ind = find(lat_pred >= lat_t - 5 & lat_pred <= lat_t + 5); % find latitude within this range
        if lon_t < 0
            lon_ind = find(lon_pred >= (lon_t+360) - 5 & lon_pred <= (lon_t+360) + 5);
        else
            lon_ind = find(lon_pred >= lon_t - 5 & lon_pred <= lon_t + 5);
        end
        new_lat = lat_pred(lat_ind); new_lon = lon_pred(lon_ind);
        v4xdaily_sub = v4xdaily(lon_ind, lat_ind, :); % subset predictor data

        v4xd10 = cat(3, v4xd10, v4xdaily_sub);
        Tvwnd = cat(1, Tvwnd, Tpred);
    end
    cd 'F:\OneDrive - Knights - University of Central Florida\Daten\MLR\TG_pct_pcd_17yrs_4xdaily_10x10'
    cd(save_nam{1})
    clearvars v4xdaily v4xdaily_sub Tpred vwnd_mat ii;
    save('vwnd.mat');

    clearvars -except lat_t lon_t save_nam gg list_gauge
    

%% Predictor - Mean Sea-level pressure
    disp('3. Predictor - Sea-level Pressure')
    cd 'F:\OneDrive - Knights - University of Central Florida\Daten\Remote Sensing\SLP\SLP_4Xdaily'
    prmsl_mat = dir('*.mat');
    prmsl_4xd10 = [];  Tprmsl = [];
    for ii = 148:164%length(prmsl_mat)
        yname = prmsl_mat(ii).name;
        fprintf('Analyzing %s\n', yname);
        load(yname);
        clearvars -except slp_4xdaily  Tslp Tprmsl lat_pred lon_pred lat_t lon_t ii prmsl_mat prmsl_4xd10 gg list_gauge save_nam

        % Define the grid
        lat_ind = find(lat_pred >= lat_t - 5 & lat_pred <= lat_t + 5); % find latitude within this range
        if lon_t < 0
            lon_ind = find(lon_pred >= (lon_t+360) - 5 & lon_pred <= (lon_t+360) + 5);
        else
            lon_ind = find(lon_pred >= lon_t - 5 & lon_pred <= lon_t + 5);
        end

        new_lat = lat_pred(lat_ind); new_lon = lon_pred(lon_ind);

        prmsl_sub = slp_4xdaily(lon_ind, lat_ind, :); % subset predictor data
        prmsl_4xd10 = cat(3, prmsl_4xd10, prmsl_sub);
        Tprmsl = cat(1, Tprmsl, Tslp);
    end

    cd 'F:\OneDrive - Knights - University of Central Florida\Daten\MLR\TG_pct_pcd_17yrs_4xdaily_10x10'
    cd(save_nam{1})
    clearvars slp_4xdaily prmsl_sub Tslp ii prmsl_mat;
    save('slp.mat');

    clearvars -except lat_t lon_t gg list_gauge save_nam

    
    %% Predictand
    
    disp('5. Predictand - Surge')
    base_path = fullfile('F:\OneDrive - Knights - University of Central Florida\Daten\MLR\TG_pct_pcd_17yrs_4xdaily_10x10', save_nam{1});
    cd 'F:\OneDrive - Knights - University of Central Florida\Daten\Tide_data\Surge_after_T_Tide'
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
















