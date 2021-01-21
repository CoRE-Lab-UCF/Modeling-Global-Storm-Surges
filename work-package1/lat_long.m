cd 'C:\Users\mi292519\OneDrive - Knights - University of Central Florida\Daten\Tide_data\Skew_surge'
list_mat = dir('*.mat');
Latitude = []; Longitude = [];
for ll = 1:length(list_mat)
    load(list_mat(ll).name)
    Latitude = [Latitude; Lat];
    Longitude = [Longitude; Lon];
end

% Plotting worldmap with tide gauges

worldmap('World')
load coastlines
plotm(coastlat,coastlon)
hold on; plotm(Latitude, Longitude, '.r', 'MarkerSize',25) %'.r', 