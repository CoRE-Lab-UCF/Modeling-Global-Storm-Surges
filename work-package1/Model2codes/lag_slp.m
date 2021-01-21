% In order to time-shift vwnd 
base_dir = 'F:\OneDrive - Knights - University of Central Florida\Daten\MLR\Model_2\4Xdaily_10X10_217_TGs';
cd (base_dir)
tg_lst = dir(base_dir);
tg_lst(1:2) = []; 
cd 'F:\OneDrive - Knights - University of Central Florida\Daten\MLR\Model_2\Extracted'
fid = fopen('no_surge_slp.txt', 'a');

for ii = 1:length(tg_lst)
    ii
    cd(fullfile(base_dir, tg_lst(ii).name))
    
    %Load daily max surge
    a = dir('*_new.mat'); load(a.name);
    clearvars -except base_dir tg_lst ii surge_daily lat_t lon_t nan_tgs fid
    
    if isempty(surge_daily)
        cd 'F:\OneDrive - Knights - University of Central Florida\Daten\MLR\Model_2\Extracted'
        fprintf(fid, 'ii = %d; Tide_Gauge = %s \n', ii, tg_lst(ii).name);
        continue %if surge and wind values don't compute
    end
    
    %Load slp data
    load('slp.mat')
    clearvars -except base_dir tg_lst ii surge_daily lat_t lon_t new_lat new_lon Tprmsl prmsl_4xd10 nan_tgs fid
    tslp = datenum(datenum('1800-1-1 00:00:00') + hours(Tprmsl));
    b = datevec(surge_daily(:,1)); bb = datetime(b(:,1:3));
    c = datevec(tslp); cc = datetime(c(:,1:3));
    d = find(bb == cc(1)); % find date where the wind data begins
    
    if isempty(d)
        cd 'F:\OneDrive - Knights - University of Central Florida\Daten\MLR\Model_2\Extracted'
        fprintf(fid, 'ii = %d; Tide_Gauge = %s \n', ii, tg_lst(ii).name);
        continue %if surge and wind values don't compute
    end
    
    
    e = min(bb(end), cc(end));
    f = find(bb == e); %find date when to stop
    
    disp('1. Extracting 30hr lagged slp')
    hh = []; count = 0;
    for jj = d:f
        %Time-shifting Uwnd
        
        t30 = datenum(surge_daily(jj, 1) - hours(30));
        g = datenum(t30 - hours(6)); 
        h = find(tslp > g & tslp <= t30);
        if isempty(h)
            count = count +1;
        end
        hh = [hh;h]; %the index for the 30hr lagged wind 
    end
    st30_lag = tslp(hh);
    s30 = prmsl_4xd10(:,:, hh); %the 30hr lagged uwnd
    clearvars h hh g jj
    
  
    disp('2. Extracting 24hr lagged slp')
    hh = [];
    for jj = d + count:f 
        
        t24 = datenum(surge_daily(jj, 1) - hours(24));
        g = datenum(t24 - hours(6));
        h = find(tslp > g & tslp <= t24);
        hh = [hh;h];
    end
    st24_lag = tslp(hh);
    s24 = prmsl_4xd10(:,:, hh); %the 30hr lagged uwnd
    clearvars h hh g jj
    

    disp('3. Extracting 18hr lagged slp')
    hh = [];
    for jj = d + count:f 
        
        t18 = datenum(surge_daily(jj, 1) - hours(18));
        g = datenum(t18 - hours(6));
        h = find(tslp > g & tslp <= t18);
        hh = [hh;h];
    end
    st18_lag = tslp(hh);
    s18 = prmsl_4xd10(:,:, hh); %the 30hr lagged uwnd
    clearvars h hh g jj

    
    disp('4. Extracting 12hr lagged slp')
    hh = [];
    for jj = d + count:f 
        
        t12 = datenum(surge_daily(jj, 1) - hours(12));
        g = datenum(t12 - hours(6));
        h = find(tslp > g & tslp <= t12);
        hh = [hh;h];
    end
    st12_lag = tslp(hh);
    s12 = prmsl_4xd10(:,:, hh); %the 30hr lagged uwnd
    clearvars h hh g jj
    
    
    disp('5. Extracting 6hr lagged slp')
    hh = [];
    for jj = d + count:f 
        
        t6 = datenum(surge_daily(jj, 1) - hours(6));
        g = datenum(t6 - hours(6));
        h = find(tslp > g & tslp <= t6);
        hh = [hh;h];
    end
    st6_lag = tslp(hh);
    s6 = prmsl_4xd10(:,:, hh); %the 30hr lagged uwnd
    clearvars h hh g jj
    

    disp('6. Extracting 0hr lagged slp')
    hh = [];
    for jj = d + count:f 
        
        t0 = surge_daily(jj, 1);
        g = datenum(t0 - hours(6));
        h = find(tslp > g & tslp <= t0);
        hh = [hh;h];
    end
    st0_lag = tslp(hh);
    s0 = prmsl_4xd10(:,:, hh); %the 0hr lagged uwnd
    
    disp('Saving .mat file')
    cd 'F:\OneDrive - Knights - University of Central Florida\Daten\MLR\Model_2\Extracted'
    cd(fullfile('F:\OneDrive - Knights - University of Central Florida\Daten\MLR\Model_2\Extracted', tg_lst(ii).name))
    clearvars -except  s0 st0_lag v6 st6_lag s12 st12_lag s18 st18_lag s24 st24_lag s30 st30_lag ii tg_lst base_dir nan_tgs fid
    save('slp_lagged.mat')
    clearvars -except base_dir ii tg_lst nan_tgs fid
end
fclose(fid);     
     
























