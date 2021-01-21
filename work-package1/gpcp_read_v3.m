cd 'C:\Users\mi292519\OneDrive - Knights - University of Central Florida\Daten\Remote Sensing\GPCP';
list_mm = dir('*.nc');
%list_mm(1:2) = [];

year_dat = [];
for yy = 1:length(list_mm)
    fname = list_mm(yy).name;
    year_dat = cat(1, year_dat, str2num(fname(19:22)));
end

yy_u = unique(year_dat);

for jj = 1:length(yy_u)
    ind = find(year_dat == yy_u(jj));
    gpcp = []; T = []; 
    for kk = 1:length(ind)
        fname = list_mm(ind(kk)).name
        base_yr = datetime(str2num(fname(19:22)), 01, 01);
        lon_pred = ncread(fname, 'lon');
        lat_pred = ncread(fname, 'lat');
        gpcp = cat(3, gpcp, ncread(fname, 'precip'));
        tt = ncread(fname, 'time'); %Concatenating along the 3rd dimension
        tt_2 = datenum(days(tt) + base_yr); % converting the time to matlab time
        T = cat(1,T,tt_2); %Concatenating along the column
    end
    matname = sprintf('%d_gpcp.mat', yy_u(jj));
    save(matname);
end


