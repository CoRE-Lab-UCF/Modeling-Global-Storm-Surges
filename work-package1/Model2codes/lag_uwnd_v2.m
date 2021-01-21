% In order to time-shift uwnd 
base_dir = 'F:\OneDrive - Knights - University of Central Florida\Daten\MLR\Model_2\4Xdaily_10X10_217_TGs';
cd (base_dir)
tg_lst = dir(base_dir);
tg_lst(1:2) = []; 
cd 'F:\OneDrive - Knights - University of Central Florida\Daten\MLR\Model_2\Extracted'
fid = fopen('Skipped TGs.txt', 'wt');

for ii = 764:length(tg_lst)
    ii
    cd(fullfile(base_dir, tg_lst(ii).name))
    
    %Load daily max surge
    a = dir('*_new.mat'); load(a.name);
    if isempty(surge_daily)
        cd 'F:\OneDrive - Knights - University of Central Florida\Daten\MLR\Model_2\Extracted'
        fprintf(fid, 'ii = %d; Tide_Gauge = %s \n', ii, tg_lst(ii).name);
        continue %if surge and wind values don't compute
    end
    clearvars -except base_dir tg_lst ii surge_daily lat_t lon_t nan_tgs fid
    
    %Load wind data
    load('uwnd.mat')
    load('vwnd.mat')
    load('slp.mat')
    tslp = datenum(datenum('1800-1-1 00:00:00') + hours(Tprmsl));
    clearvars -except base_dir tg_lst ii surge_daily lat_t lon_t ... 
         Tuwnd u4xd10 fid Tvwnd v4xd10 tslp prmsl_4xd10
    b = datevec(surge_daily(:,1)); bb = datetime(b(:,1:3));
    x = datevec(Tuwnd); xx = datetime(x(:,1:3));
    y = datevec(Tvwnd); yy = datetime(y(:,1:3));
    z = datevec(tslp); zz = datetime(z(:,1:3));
    
    % Check if predictors have the same time period
    if (length(xx) == length(yy)) & (length(xx) == length(zz))
        peter = find((xx == yy) == 0 | (xx == zz) == 0); %making sure the time for
            %all predictors is the same
        if isfinite(peter)
            cd 'F:\OneDrive - Knights - University of Central Florida\Daten\MLR\Model_2\Extracted'
            fprintf(fid, 'CHECK IT! - ii = %d; Tide_Gauge = %s \n', ii, tg_lst(ii).name);
            continue
        end
    else
        cd 'F:\OneDrive - Knights - University of Central Florida\Daten\MLR\Model_2\Extracted'
        fprintf(fid, 'CHECK IT! - ii = %d; Tide_Gauge = %s \n', ii, tg_lst(ii).name);
        continue 
    end
    
    xyz = [xx;yy;zz]; cc_uq = unique(xyz); %to find the surge values that
    %can be modelled by all predictors
    clear x y z xyz 
    
    %% Subset dataset 
    ind_bb = []; %to find the overlap between predictor and predictand
    for kk = 1:length(cc_uq)
        ind = find(bb == cc_uq(kk));
        if isempty(ind)
            ind = NaN;
        end
        ind_bb = [ind_bb;ind];
    end
 
    ind_sg = ind_bb(find(isfinite(ind_bb))); %filter surge that has predictors
    
    if isempty(ind_sg)
        cd 'F:\OneDrive - Knights - University of Central Florida\Daten\MLR\Model_2\Extracted'
        fprintf(fid, 'ii = %d; Tide_Gauge = %s \n', ii, tg_lst(ii).name);
        continue %if surge and wind values don't compute
    else 
        surge_sub = surge_daily(ind_sg,:);
    end
	
	
	
	
 %% Time-shift predictors
    disp('1. Extracting 30hr lagged uwnd')
    hh = []; count = 0;
    for jj = 1:length(surge_sub)
        
        t30 = datenum(surge_sub(jj, 1) - hours(30));
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
    for jj = 1 + count:length(surge_sub)
        
        t24 = datenum(surge_sub(jj, 1) - hours(24));
        g = datenum(t24 - hours(6));
        h = find(Tuwnd > g & Tuwnd <= t24);
        hh = [hh;h];
    end
    ut24_lag = Tuwnd(hh);
    u24 = u4xd10(:,:, hh); %the 30hr lagged uwnd
    clearvars h hh g jj
    

    disp('3. Extracting 18hr lagged uwnd')
    hh = [];
    for jj = 1 + count:length(surge_sub) 
        
        t18 = datenum(surge_sub(jj, 1) - hours(18));
        g = datenum(t18 - hours(6));
        h = find(Tuwnd > g & Tuwnd <= t18);
        hh = [hh;h];
    end
    ut18_lag = Tuwnd(hh);
    u18 = u4xd10(:,:, hh); %the 30hr lagged uwnd
    clearvars h hh g jj

    
    disp('4. Extracting 12hr lagged uwnd')
    hh = [];
    for jj = 1 + count:length(surge_sub)
        
        t12 = datenum(surge_sub(jj, 1) - hours(12));
        g = datenum(t12 - hours(6));
        h = find(Tuwnd > g & Tuwnd <= t12);
        hh = [hh;h];
    end
    ut12_lag = Tuwnd(hh);
    u12 = u4xd10(:,:, hh); %the 30hr lagged uwnd
    clearvars h hh g jj
    
    
    disp('5. Extracting 6hr lagged uwnd')
    hh = [];
    for jj = 1 + count:length(surge_sub) 
        
        t6 = datenum(surge_sub(jj, 1) - hours(6));
        g = datenum(t6 - hours(6));
        h = find(Tuwnd > g & Tuwnd <= t6);
        hh = [hh;h];
    end
    ut6_lag = Tuwnd(hh);
    u6 = u4xd10(:,:, hh); %the 30hr lagged uwnd
    clearvars h hh g jj
    

    disp('6. Extracting 0hr lagged uwnd')
    hh = [];
    for jj = 1 + count:length(surge_sub) 
        
        t0 = surge_sub(jj, 1);
        g = datenum(t0 - hours(6));
        h = find(Tuwnd > g & Tuwnd <= t0);
        hh = [hh;h];
    end
    ut0_lag = Tuwnd(hh);
    u0 = u4xd10(:,:, hh); %the 0hr lagged uwnd
    
    %% Edit surge according to count
    if count ~= 0
        surge_sub = surge_sub(1 + count:end,:);
    end

	
   %% Save	   
    disp('Saving .mat file')
    cd 'F:\OneDrive - Knights - University of Central Florida\Daten\MLR\Model_2\Extracted'
    mkdir(tg_lst(ii).name); cd(tg_lst(ii).name);
    save('surge_dmax.mat', 'surge_sub', 'lat_t', 'lon_t');% saving surge separately
    clearvars -except  u0 ut0_lag u6 ut6_lag u12 ut12_lag u18 ut18_lag ...
        u24 ut24_lag u30 ut30_lag ii tg_lst base_dir nan_tgs fid 
    save('uwnd_lagged.mat') 
    clearvars -except base_dir ii tg_lst nan_tgs fid surge_sub
end
fclose(fid);     
























