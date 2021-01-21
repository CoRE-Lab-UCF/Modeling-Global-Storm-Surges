% To count the number of years availabe in the 1998-2014 period

base_dir = 'F:\OneDrive - Knights - University of Central Florida\Daten\MLR\Model_2\Extracted'
cd(base_dir)
dd = dir('*_4d10x10')
yrs = [];
for mt = 1:length(dd)
    cd(fullfile(base_dir, dd(mt).name))
    load('surge_dmax.mat')
    y1 = datevec(surge_sub(:,1));
    y2 = length(unique(y1(:,1)));
    y3 = [lon_t lat_t y2];
    yrs = [yrs; y3]; 
    clearvars -except base_dir dd yrs 
end

 save('numb_yrs_TGs_449TGs.mat')
