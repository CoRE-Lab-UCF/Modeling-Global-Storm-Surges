ftpobj = ftp('ftp.cdc.noaa.gov');
cd(ftpobj, 'Datasets/noaa.oisst.v2.highres');
list = dir(ftpobj);

cd 'C:\Users\mi292519\OneDrive - Knights - University of Central Florida\Daten\Reanalysis\20CR\SST\sst.day.mean'

for ii = 1:length(list)
    if exist(list(ii).name, 'file')
        continue
    elseif length(list(ii).name) < 23
        continue
    elseif strcmp(list(ii).name(1:12), 'sst.day.mean') == 1
        list(ii).name
        mget(ftpobj, list(ii).name);
    end
end