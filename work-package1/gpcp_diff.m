cd 'C:\Users\mi292519\OneDrive - Knights - University of Central Florida\Daten\Remote Sensing\GPCP';
list = dir('*.nc'); 
for ii = 1:length(list)
    yr(ii,1) = str2num(list(ii).name(19:22));
    yy = unique(yr);
    dd = diff(yy);
end
