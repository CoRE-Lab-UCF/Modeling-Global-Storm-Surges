cd 'F:\OneDrive - Knights - University of Central Florida\Daten\Remote Sensing\SLP'
base_yr = datenum('1800-1-1 00:00:00');
list_yr = dir('*.nc');
for yy = 1:length(list_yr) % stopped at yy = 22
    Tpred = [];
    Tslpmn = []; slp_4xdaily = [];
    slpname = list_yr(yy).name;
    lon_pred = ncread(slpname, 'lon');
    lat_pred = ncread(slpname, 'lat');
    tt = ncread(slpname, 'time');
    slprd = ncread(slpname, 'prmsl'); % 6hrly slp date in Kpa
    for hr = 1:4:length(slprd)-3
        tt2 = tt(hr:hr+3);
        [slpmn, Ind] = min(slprd(:,:,hr:hr+3), [],3);
        slp_daily = cat(3, slp_daily, slpmn);
        Tpred = [Tpred; datenum(hours(tt(hr)) + base_yr)]; 
        Tslpmn = cat(3, Tslpmn, datenum(hours(tt2(Ind)) + base_yr));
    end
    % Saving .mat files for every year
    save_name = sprintf('%s.mat', slpname);
    %mat_name = fullfile(basepath, save_name);
    save (save_name, '-v7.3');
    clearvars -except base_yr list_yr y
end

