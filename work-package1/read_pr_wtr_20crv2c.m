ftpobj = ftp('ftp.cdc.noaa.gov');
cd(ftpobj, 'Datasets/20thC_ReanV2c/monolevel');
list = dir(ftpobj);

cd 'C:\Users\mi292519\OneDrive - Knights - University of Central Florida\Daten\Reanalysis\20CR\pr_wtr'

for ii = 1:length(list)
    if exist(list(ii).name, 'file')
        continue
    elseif length(list(ii).name) < 19
        continue
    elseif strcmp(list(ii).name(1:6), 'pr_wtr') == 1
        list(ii).name
        mget(ftpobj, list(ii).name);
    end
end