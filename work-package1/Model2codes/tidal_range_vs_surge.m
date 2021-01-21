% To compute the mean tidal range with the quantiles of surge values

cd 'F:\OneDrive - Knights - University of Central Florida\Daten\Tide_data\Surge_after_T_Tide'
lss = dir('*.mat')

%mean_rng = [];
for jc = 1:length(lss)
    jc
    load(lss(jc).name)
    a1 = Thour;
    a2 = datevec(a1);
    a3 = datenum(a2(:,1:3));
    a4 = unique(a3);
    
    rng = [];
    for jm = 1:length(a4)
        b1 = find(a3 == a4(jm));
        mx = nanmax(Tide(b1)); % daily max tide
        mn = nanmin(Tide(b1)); % daily min tide
        rng1 = mx - mn; %tidal range
        rng = [rng ;rng1];
    end
    mean_rng = nanmean(rng);
    
    tidal_range(jc, 1) = Lon;
    tidal_range(jc,2) = Lat;
    tidal_range(jc,3) = nanmax(Tide);
    tidal_range(jc,4) = nanmin(Tide);
    tidal_range(jc,5) = mean_rng;
end