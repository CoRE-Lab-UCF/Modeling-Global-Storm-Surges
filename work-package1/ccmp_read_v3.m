%cd 'C:\Users\Admin\OneDrive - Knights - University of Central Florida\Daten\CCMP\January_1988\M01';
basepath = 'C:\Users\mi292519\OneDrive - Knights - University of Central Florida\Daten\Remote Sensing\CCMP';
base_yr = datenum('1987-01-01 00:00:00');
list_yr = dir(basepath);
list_yr(1:2) = []; 
for yy = 13:length(list_yr)
    cd(fullfile(basepath, list_yr(yy).name));
    list_mm = dir(pwd); 
    list_mm(1:2) = [];
    
    
    st = 1; Thour = []; Tumax = []; Tvmax; udmax = []; vdmax = [];
    for mm = 1:length(list_mm)
        cd(fullfile(pwd, list_mm(mm).name));
        list_dd = dir(pwd);
        list_dd(1:2) = [];
        list_dd(end) = [];
        
        %if yy == 1  
        %st = 1;
        %end
        
        for dd = 1:length(list_dd)
            %st
            if st == 1
                d = dd
            else
                d = d + 1
            end
            fname = list_dd(dd).name
            wind_u = ncread(fname, 'uwnd');
            wind_v = ncread(fname, 'vwnd');
            tt = ncread(fname, 'time');
            Lon = ncread(fname, 'longitude'); 
            Lat = ncread(fname, 'latitude');
            [w_umax, ui] = max(wind_u, [],3);
            [w_vmax, vi] = max(wind_v, [], 3);
            %T(dd,1) = tt(4); %take the 4th element of tt to have a daily time step
            Thour = [Thour; datenum(hours(tt(4)) + base_yr)];
            Tumax = cat(3, Tumax, datenum(hours(tt(ui)) + base_yr));
            Tvmax = cat(3, Tmax, datenum(hours(tt(vi)) + base_yr));
            %w_dumax(:,:,d) = w_umax;
            %w_dvmax(:,:,d) = w_vmax;
            udmax = cat(3, udmax, w_umax);
            vdmax = cat(3, vdmax, w_vmax);
            st = 0;
            %st = st + 1;
        end
        cd('..')
        
    end
	save ('DATA.mat', '-v7.3');
    %clearvars -except base_yr basepath list_yr st d;
    if yy == length(list_yr)
        return;
    else
        clearvars wind_u wind_v udmax vdmax;
    end
    cd('..')
    
end


%Time = T/24 + datenum('01-Jan-1987 00:00:00');

