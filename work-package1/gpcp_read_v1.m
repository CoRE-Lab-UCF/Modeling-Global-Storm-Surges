%% First part 1996-2005

cd 'C:\Users\mi292519\OneDrive - Knights - University of Central Florida\Daten\Remote Sensing\GPCP';
list_mm = dir('*.nc');
%list_mm(1:2) = [];


mm = 1; T = [];
while mm < 112
    mm
    fname = list_mm(mm).name
    base_yr = datetime(str2num(fname(19:22)), 01, 01);
    if mm == 1
        gpcp = ncread(fname, 'precip');
    else
        gpcp = cat(3, gpcp, ncread(fname, 'precip')); %Concatenating along the 3rd dimension
    end
    
    tt = ncread(fname, 'time');
    tt_2 = datenum(days(tt) + base_yr); % converting the time to matlab time
    T = cat(1,T,tt_2); %Concatenating along the column
    Lon = ncread(fname, 'lon');
    Lat = ncread(fname, 'lat');
    mm = mm + 1;
end
save gpcp_1996_2005.mat;
clear('gpcp', 'tt', 'T');
%% Second part 2006-2015

T = [];
while mm > 111 & mm <= length(list_mm)
    mm
    fname = list_mm(mm).name
    base_yr = datetime(str2num(fname(19:22)), 01, 01);
    if mm == 112
        gpcp = ncread(fname, 'precip');
    else
        gpcp = cat(3, gpcp, ncread(fname, 'precip')); %Concatenating along the 3rd dimension
    end
    tt = ncread(fname, 'time');
    tt_2 = datenum(days(tt) + base_yr);
    T = cat(1,T,tt_2); %Concatenating along the column
    Lon = ncread(fname, 'lon');
    Lat = ncread(fname, 'lat');
    mm = mm + 1;
end
save gpcp_2006_2015.mat;


   
