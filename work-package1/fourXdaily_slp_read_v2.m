cd 'F:\OneDrive - Knights - University of Central Florida\Daten\Remote Sensing\SLP'
base_yr = datenum('1800-1-1 00:00:00');
list_yr = dir('*.nc');

for yy = 1:length(list_yr) % stopped at yy = 22
    yy
    slpname = list_yr(yy).name;
    lon_pred = ncread(slpname, 'lon');
    lat_pred = ncread(slpname, 'lat');
    Tslp = ncread(slpname, 'time');
    slp_4xdaily = ncread(slpname, 'prmsl'); % 6hrly slp date in Kpa

    % Saving .mat files for every year
    save_name = sprintf('%s_4x_daily.mat', slpname);
    %mat_name = fullfile(basepath, save_name);
    cd 'F:\OneDrive - Knights - University of Central Florida\Daten\Remote Sensing\SLP\SLP_4Xdaily'
    save (save_name, '-v7.3');
    clearvars -except base_yr list_yr yy
    cd 'F:\OneDrive - Knights - University of Central Florida\Daten\Remote Sensing\SLP'
end

