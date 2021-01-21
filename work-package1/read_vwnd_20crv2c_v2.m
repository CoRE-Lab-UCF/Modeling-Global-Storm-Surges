ftpobj = ftp('ftp.cdc.noaa.gov');
cd(ftpobj, 'Datasets/20thC_ReanV2c/gaussian/monolevel');
list = dir(ftpobj);

cd 'C:\Users\mi292519\OneDrive - Knights - University of Central Florida\Daten\Reanalysis\20CR\vwnd_10m_ens_mean'

for ii = 1:length(list)
    if exist(list(ii).name, 'file')
        continue
    elseif length(list(ii).name) < 6
        continue
    elseif strcmp(list(ii).name(1:6), 'vwnd.1') == 1
        mget(ftpobj, list(ii).name);
    end
end