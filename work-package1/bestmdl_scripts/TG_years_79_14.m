% To calculate the number of years used for Model B %

cd 'D:\OneDrive - Knights - University of Central Florida\Daten\Reanalysis\ERA_Interim\Models\bestmdl_b\BestMdl_b'
tg = dir('*.mat')
tg_yrs = NaN(length(tg), 3);
for ii = 1:length(tg)
    ii
    load(tg(ii).name)
    clearvars -except tg ii y_surge lon_t lat_t tg_yrs
    a = datevec(y_surge(:,1));
    b = unique(a(:,1));
    c = length(b);
    tg_yrs(ii,:) = [lon_t lat_t c];
    clear a b c
end
