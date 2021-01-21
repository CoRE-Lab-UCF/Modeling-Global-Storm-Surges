%cd 'C:\Users\Admin\OneDrive - Knights - University of Central Florida\Daten\CCMP\January_1988\M01';
basepath = 'C:\Users\Admin\OneDrive - Knights - University of Central Florida\Daten\CCMP\January_1988';
listdir = dir(basepath);
listdir(1:2) = []; list(end) = [];
for mm = 1:length(listdir)
    cd(fullfile(basepath, listdir(mm).name))
    list2 = dir(pwd); 
    list2(1:2) = [];
    list2(end) = [];
    st = 1;
    for dd = 1:length(list2)
        dd
        fname = list2(dd).name
        Wind_u(:,:,st:st+3) = ncread(fname, 'uwnd');
        Wind_v(:,:,st:st+3) = ncread(fname, 'vwnd');
        T(st:st+3,1) = ncread(fname, 'time');
        st = st + 4;
    end
    Lon = ncread(fname, 'longitude');
    Lat = ncread(fname, 'latitude');
    cd('..')
end


Time = T/24 + datenum('01-Jan-1987 00:00:00');

