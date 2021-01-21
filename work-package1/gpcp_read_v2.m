cd 'C:\Users\mi292519\OneDrive - Knights - University of Central Florida\Daten\Remote Sensing\GPCP';
list_mm = dir('*.nc');
%list_mm(1:2) = [];


mm = 1; T = []; year_dat = [];

for yy = 1:length(list_mm)
    fname = list_mm(yy).name;
    year_dat = cat(1, year_dat, str2num(fname(19:22)));
end

yy_u = unique(year_dat);

for mm = 1:length(list_mm)
    fname = list_mm(mm).name;
    if   


while mm <= length(list_mm)%112
    mm
    fname = list_mm(mm).name

    yr = str2num(fname(19:22));
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
save ('gpcp_data.mat', '-v7.3');



   
