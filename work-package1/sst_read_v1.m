%cd 'C:\Users\Admin\OneDrive - Knights - University of Central Florida\Daten\CCMP\January_1988\M01';
basepath = 'C:\Users\mi292519\OneDrive - Knights - University of Central Florida\Daten\Remote Sensing\SST';
base_yr = datenum('1981-1-1 00:00:00');
list_yr = dir(basepath);
list_yr(1:2) = [];
for yy = 1:5%length(list_yr)
    cd(fullfile(basepath, list_yr(yy).name));
    list_dd = dir('*.nc');
    %list_dd(1:2) = [];
    %list_dd(end) = [];
    
    sst = [];
    for dd = 1:length(list_dd)
            %st
            dd
            fname = list_dd(dd).name
            sst = cat(3, sst, ncread(fname, 'analysed_sst'));
            tt = ncread(fname, 'time');
            T(dd,1) = datenum(seconds(tt) + base_yr);
            Lon = ncread(fname, 'lon'); 
            Lat = ncread(fname, 'lat');
            %st = st + 1;
    end
    cd (basepath);
    save_name = sprintf('%s.mat', list_yr(yy).name);
    save (save_name, '-v7.3');
    clearvars -except base_yr basepath list_yr yy 
end


   
