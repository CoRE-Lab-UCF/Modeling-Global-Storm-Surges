% In order to time-shift predictors 
base_dir = 'F:\OneDrive - Knights - University of Central Florida\Daten\MLR\Model_2\4Xdaily_10X10_217_TGs';
cd (base_dir)
tg_lst = dir(base_dir);
tg_lst(1:2) = []; 
cd 'F:\OneDrive - Knights - University of Central Florida\Daten\MLR\Model_2\Extracted'
fid = fopen('no_surge.txt', 'a');

for ii = 1:length(tg_lst)
    ii
    cd(fullfile(base_dir, tg_lst(ii).name))
    
    %Load daily max surge
    a = dir('*_new.mat'); load(a.name);
    clearvars -except base_dir tg_lst ii surge_daily lat_t lon_t nan_tgs fid
    
    %Load wind data
    load('uwnd.mat')
    if isempty(surge_daily)
        cd 'F:\OneDrive - Knights - University of Central Florida\Daten\MLR\Model_2\Extracted'
        fprintf(fid, 'ii = %d; Tide_Gauge = %s \n', ii, tg_lst(ii).name);
        continue %if surge and wind values don't compute
    end
    clearvars -except base_dir tg_lst ii surge_daily lat_t lon_t new_lat new_lon Tuwnd u4xd10 nan_tgs fid
    b = datevec(surge_daily(:,1)); bb = datetime(b(:,1:3));
    c = datevec(Tuwnd); cc = datetime(c(:,1:3));
    d = find(bb == cc(1)); % find date where the wind data begins
    
    if isempty(d)
        cd 'F:\OneDrive - Knights - University of Central Florida\Daten\MLR\Model_2\Extracted'
        fprintf(fid, 'ii = %d; Tide_Gauge = %s \n', ii, tg_lst(ii).name);
        continue %if surge and wind values don't compute
    end
    
    
    e = min(bb(end), cc(end));
    f = find(bb == e); %find date when to stop
    
    disp('1. Extracting 30hr lagged uwnd')
    hh = []; count = 0;
    for jj = d:f
        %Time-shifting Uwnd
        
        t30 = datenum(surge_daily(jj, 1) - hours(30));
        g = datenum(t30 - hours(6)); 
        h = find(Tuwnd > g & Tuwnd <= t30);
        if isempty(h)
            count = count +1;
        end
        hh = [hh;h]; %the index for the 30hr lagged wind 
    end
    ut30_lag = Tuwnd(hh);
    u30 = u4xd10(:,:, hh); %the 30hr lagged uwnd
    clearvars h hh g jj
    
  
    disp('2. Extracting 24hr lagged uwnd')
    hh = [];
    for jj = d + count:f % to make all matrices equal 
        
        t24 = datenum(surge_daily(jj, 1) - hours(24));
        g = datenum(t24 - hours(6));
        h = find(Tuwnd > g & Tuwnd <= t24);
        hh = [hh;h];
    end
    ut24_lag = Tuwnd(hh);
    u24 = u4xd10(:,:, hh); %the 30hr lagged uwnd
    clearvars h hh g jj
    

    disp('3. Extracting 18hr lagged uwnd')
    hh = [];
    for jj = d + count:f 
        
        t18 = datenum(surge_daily(jj, 1) - hours(18));
        g = datenum(t18 - hours(6));
        h = find(Tuwnd > g & Tuwnd <= t18);
        hh = [hh;h];
    end
    ut18_lag = Tuwnd(hh);
    u18 = u4xd10(:,:, hh); %the 30hr lagged uwnd
    clearvars h hh g jj

    
    disp('4. Extracting 12hr lagged uwnd')
    hh = [];
    for jj = d + count:f 
        
        t12 = datenum(surge_daily(jj, 1) - hours(12));
        g = datenum(t12 - hours(6));
        h = find(Tuwnd > g & Tuwnd <= t12);
        hh = [hh;h];
    end
    ut12_lag = Tuwnd(hh);
    u12 = u4xd10(:,:, hh); %the 30hr lagged uwnd
    clearvars h hh g jj
    
    
    disp('5. Extracting 6hr lagged uwnd')
    hh = [];
    for jj = d + count:f 
        
        t6 = datenum(surge_daily(jj, 1) - hours(6));
        g = datenum(t6 - hours(6));
        h = find(Tuwnd > g & Tuwnd <= t6);
        hh = [hh;h];
    end
    ut6_lag = Tuwnd(hh);
    u6 = u4xd10(:,:, hh); %the 30hr lagged uwnd
    clearvars h hh g jj
    

    disp('6. Extracting 0hr lagged uwnd')
    hh = [];
    for jj = d + count:f 
        
        t0 = surge_daily(jj, 1);
        g = datenum(t0 - hours(6));
        h = find(Tuwnd > g & Tuwnd <= t0);
        hh = [hh;h];
    end
    ut0_lag = Tuwnd(hh);
    u0 = u4xd10(:,:, hh); %the 0hr lagged uwnd
    
    %Subsetting surge
    surge_sub = surge_daily(d+count:f, :);
    
    disp('Saving .mat file')
    cd 'F:\OneDrive - Knights - University of Central Florida\Daten\MLR\Model_2\Extracted'
    mkdir(tg_lst(ii).name); cd(tg_lst(ii).name);
    clearvars -except  u0 ut0_lag u6 ut6_lag u12 ut12_lag u18 ut18_lag u24 ut24_lag u30 ut30_lag ii tg_lst base_dir nan_tgs fid surge_sub
    save('uwnd_lagged.mat')
    clearvars -except base_dir ii tg_lst nan_tgs fid surge_sub
end
fclose(fid);     
























