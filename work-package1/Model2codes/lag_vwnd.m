% In order to time-shift vwnd 
base_dir = 'F:\OneDrive - Knights - University of Central Florida\Daten\MLR\Model_2\4Xdaily_10X10_217_TGs';
cd (base_dir)
tg_lst = dir(base_dir);
tg_lst(1:2) = []; 
cd 'F:\OneDrive - Knights - University of Central Florida\Daten\MLR\Model_2\Extracted'
%fid = fopen('no_surge_vwnd.txt', 'a');

for ii = 60:length(tg_lst)
    ii
    cd(fullfile(base_dir, tg_lst(ii).name))
    
    %Load daily max surge
    a = dir('*_new.mat'); load(a.name);
    clearvars -except base_dir tg_lst ii surge_daily lat_t lon_t nan_tgs fid
    
    %Load vwnd data
    load('vwnd.mat')
    if isempty(surge_daily)
        cd 'F:\OneDrive - Knights - University of Central Florida\Daten\MLR\Model_2\Extracted'
        fprintf(fid, 'ii = %d; Tide_Gauge = %s \n', ii, tg_lst(ii).name);
        continue %if surge and wind values don't compute
    end
    clearvars -except base_dir tg_lst ii surge_daily lat_t lon_t new_lat new_lon Tvwnd v4xd10 nan_tgs fid
    b = datevec(surge_daily(:,1)); bb = datetime(b(:,1:3));
    c = datevec(Tvwnd); cc = datetime(c(:,1:3));
    cc_uq = unique(cc);
    %d = find(bb == cc(1)); % find date where the wind data begins
    
    
    ind_bb = []; %to find the overlap between predictor and predictand
    for kk = 1:length(cc_uq)
        ind = find(bb == cc_uq(kk));
        if isempty(ind)
            ind = NaN;
        end
        ind_bb = [ind_bb;ind];
    end
 
    if isempty(ind_bb)
        cd 'F:\OneDrive - Knights - University of Central Florida\Daten\MLR\Model_2\Extracted'
        fprintf(fid, 'ii = %d; Tide_Gauge = %s \n', ii, tg_lst(ii).name);
        continue %if surge and wind values don't compute
    end
    
    
    e = min(bb(end), cc(end));
    f = find(bb == e); %find date when to stop
    
    disp('1. Extracting 30hr lagged vwnd')
    hh = []; count = 0;
    for jj = d:f
        %Time-shifting Uwnd
        
        t30 = datenum(surge_daily(jj, 1) - hours(30));
        g = datenum(t30 - hours(6)); 
        h = find(Tvwnd > g & Tvwnd <= t30);
        if isempty(h)
            count = count +1;
        end
        hh = [hh;h]; %the index for the 30hr lagged wind 
    end
    vt30_lag = Tvwnd(hh);
    v30 = v4xd10(:,:, hh); %the 30hr lagged uwnd
    clearvars h hh g jj
    
  
    disp('2. Extracting 24hr lagged vwnd')
    hh = [];
    for jj = d + count:f 
        
        t24 = datenum(surge_daily(jj, 1) - hours(24));
        g = datenum(t24 - hours(6));
        h = find(Tvwnd > g & Tvwnd <= t24);
        hh = [hh;h];
    end
    vt24_lag = Tvwnd(hh);
    v24 = v4xd10(:,:, hh); %the 30hr lagged uwnd
    clearvars h hh g jj
    

    disp('3. Extracting 18hr lagged vwnd')
    hh = [];
    for jj = d + count:f 
        
        t18 = datenum(surge_daily(jj, 1) - hours(18));
        g = datenum(t18 - hours(6));
        h = find(Tvwnd > g & Tvwnd <= t18);
        hh = [hh;h];
    end
    vt18_lag = Tvwnd(hh);
    v18 = v4xd10(:,:, hh); %the 30hr lagged uwnd
    clearvars h hh g jj

    
    disp('4. Extracting 12hr lagged vwnd')
    hh = [];
    for jj = d + count:f 
        
        t12 = datenum(surge_daily(jj, 1) - hours(12));
        g = datenum(t12 - hours(6));
        h = find(Tvwnd > g & Tvwnd <= t12);
        hh = [hh;h];
    end
    vt12_lag = Tvwnd(hh);
    v12 = v4xd10(:,:, hh); %the 30hr lagged uwnd
    clearvars h hh g jj
    
    
    disp('5. Extracting 6hr lagged vwnd')
    hh = [];
    for jj = d + count:f 
        
        t6 = datenum(surge_daily(jj, 1) - hours(6));
        g = datenum(t6 - hours(6));
        h = find(Tvwnd > g & Tvwnd <= t6);
        hh = [hh;h];
    end
    vt6_lag = Tvwnd(hh);
    v6 = v4xd10(:,:, hh); %the 30hr lagged uwnd
    clearvars h hh g jj
    

    disp('6. Extracting 0hr lagged uwnd')
    hh = [];
    for jj = d + count:f 
        
        t0 = surge_daily(jj, 1);
        g = datenum(t0 - hours(6));
        h = find(Tvwnd > g & Tvwnd <= t0);
        hh = [hh;h];
    end
    vt0_lag = Tvwnd(hh);
    v0 = v4xd10(:,:, hh); %the 0hr lagged uwnd
    
    disp('Saving .mat file')
    cd 'F:\OneDrive - Knights - University of Central Florida\Daten\MLR\Model_2\Extracted'
    cd(fullfile('F:\OneDrive - Knights - University of Central Florida\Daten\MLR\Model_2\Extracted', tg_lst(ii).name))
    clearvars -except  v0 vt0_lag v6 vt6_lag v12 vt12_lag v18 vt18_lag v24 vt24_lag v30 vt30_lag ii tg_lst base_dir nan_tgs fid
    save('vwnd_lagged.mat')
    clearvars -except base_dir ii tg_lst nan_tgs fid
end
fclose(fid);     
     
























