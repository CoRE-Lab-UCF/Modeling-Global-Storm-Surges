%cd 'C:\Users\Admin\OneDrive - Knights - University of Central Florida\Daten\CCMP\January_1988\M01';
basepath = 'C:\Users\mi292519\OneDrive - Knights - University of Central Florida\Daten\Remote Sensing\CCMP';
list_yr = dir(basepath);
list_yr(1:2) = [];
for yy = 1:length(list_yr)
    cd(fullfile(basepath, list_yr(yy).name));
    list_mm = dir(pwd); 
    list_mm(1:2) = [];
    
    for mm = 1:length(list_mm)
        cd(fullfile(pwd, list_mm(mm).name));
        list_dd = dir(pwd);
        list_dd(1:2) = [];
        list_dd(end) = [];
        
        if yy == 1  
        st = 1;
        end
        
        for dd = 1:length(list_dd)
        st
        dd
        fname = list_dd(dd).name
        wind_u = ncread(fname, 'uwnd');
        wind_v = ncread(fname, 'vwnd');
		tt = ncread(fname, 'time');
		Lon = ncread(fname, 'longitude'); 
		Lat = ncread(fname, 'latitude');
        w_umax = max(wind_u, [],3);
        w_vmax = max(wind_v, [], 3);
        T(st,1) = tt(4); %take the 4th element of tt to have a daily time step
        w_dumax(:,:,st) = w_umax;
        w_dvmax(:,:,st) = w_vmax;
        st = st + 1;
        end
        cd('..')
    end
	
    cd('..')
end


%Time = T/24 + datenum('01-Jan-1987 00:00:00');

