
cd 'C:\Users\mi292519\OneDrive - Knights - University of Central Florida\Daten\Remote Sensing\GPCP';
list_mm = dir('*.nc'); %index only netcdf files
%list_mm(1:2) = [];


mm = 1; T = [];
for mm = 1:length(list_mm)
    mm
    fname = list_mm(mm).name
    if mm == 1
        gpcp = ncread(fname, 'precip');
    else
        gpcp = cat(3, gpcp, ncread(fname, 'precip')); %Concatenating along the 3rd dimension
    end
    tt = ncread(fname, 'time');
    T = cat(1,T,tt); %Concatenating along the column
    Lon = ncread(fname, 'lon');
    Lat = ncread(fname, 'lat');
end