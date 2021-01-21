% To compute the correlation between Tide and Surge for 902 TGs %


cd 'F:\OneDrive - Knights - University of Central Florida\Daten\Tide_data\Tide_Surge@dailymax'
lst = dir('*.mat')

for jm = 1:length(lst)
    jm
    cd 'F:\OneDrive - Knights - University of Central Florida\Daten\Tide_data\Tide_Surge@dailymax'
    load(lst(jm).name)
    ind = find(isfinite(ti_sg_daily(:,2))&isfinite(ti_sg_daily(:,3)));
    if isempty(ind)
        continue;
    end
    xx = ti_sg_daily(:,2); yy = ti_sg_daily(:,3);
    cor_val = corr(xx(ind), yy(ind));
    a = strsplit(lst(jm).name, '.mat.mat.mat');
    b = a{1}; c = strcat(b, '.mat.mat');
    cd 'F:\OneDrive - Knights - University of Central Florida\Daten\Tide_data\Surge_after_T_Tide'
    load(c);
    
    ti_sg(jm,1) = Lon;
    ti_sg(jm,2) = Lat;
    ti_sg(jm,3) = cor_val;
    clearvars -except lst jm ti_sg
end
cd 'F:\OneDrive - Knights - University of Central Florida\Daten\MLR\Model_2\Model_2_results'
save('tide_surge_intr.mat', 'ti_sg')