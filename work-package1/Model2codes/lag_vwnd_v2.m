% In order to time-shift vwnd 
base_dir = 'F:\OneDrive - Knights - University of Central Florida\Daten\MLR\Model_2\4Xdaily_10X10_217_TGs';
b2_dir = 'F:\OneDrive - Knights - University of Central Florida\Daten\MLR\Model_2\Extracted'
cd (base_dir)
tg_lst = dir(base_dir);
tg_lst(1:2) = []; 
%cd 'F:\OneDrive - Knights - University of Central Florida\Daten\MLR\Model_2\Extracted'
%fid = fopen('no_surge_vwnd.txt', 'a');

for ii = 764:length(tg_lst)
    ii
    cd(b2_dir)
    if exist(tg_lst(ii).name) == 7
        cd(fullfile(b2_dir, tg_lst(ii).name))
    else
        continue
    end
    
    %Load daily max surge
    load('surge_dmax.mat');
    
    %Load vwnd data
    cd(fullfile(base_dir, tg_lst(ii).name))
    load('vwnd.mat')

    clearvars -except base_dir b2_dir tg_lst ii surge_sub lat_t lon_t new_lat new_lon Tvwnd v4xd10

   
  %% Time-shift predictors
    disp('1. Extracting 30hr lagged vwnd')
    hh = []; 
    for jj = 1:length(surge_sub)
        
        t30 = datenum(surge_sub(jj, 1) - hours(30));
        g = datenum(t30 - hours(6)); 
        h = find(Tvwnd > g & Tvwnd <= t30);
        hh = [hh;h]; %the index for the 30hr lagged wind 
    end
    vt30_lag = Tvwnd(hh);
    v30 = v4xd10(:,:, hh); %the 30hr lagged uwnd
    clearvars h hh g jj
    
  %%
    disp('2. Extracting 24hr lagged vwnd')
    hh = [];
    for jj = 1:length(surge_sub) 
        
        t24 = datenum(surge_sub(jj, 1) - hours(24));
        g = datenum(t24 - hours(6));
        h = find(Tvwnd > g & Tvwnd <= t24);
        hh = [hh;h];
    end
    vt24_lag = Tvwnd(hh);
    v24 = v4xd10(:,:, hh); %the 30hr lagged uwnd
    clearvars h hh g jj
    

    disp('3. Extracting 18hr lagged vwnd')
    hh = [];
    for jj = 1:length(surge_sub) 
        
        t18 = datenum(surge_sub(jj, 1) - hours(18));
        g = datenum(t18 - hours(6));
        h = find(Tvwnd > g & Tvwnd <= t18);
        hh = [hh;h];
    end
    vt18_lag = Tvwnd(hh);
    v18 = v4xd10(:,:, hh); %the 30hr lagged uwnd
    clearvars h hh g jj

    
    disp('4. Extracting 12hr lagged vwnd')
    hh = [];
    for jj = 1:length(surge_sub) 
        
        t12 = datenum(surge_sub(jj, 1) - hours(12));
        g = datenum(t12 - hours(6));
        h = find(Tvwnd > g & Tvwnd <= t12);
        hh = [hh;h];
    end
    vt12_lag = Tvwnd(hh);
    v12 = v4xd10(:,:, hh); %the 30hr lagged uwnd
    clearvars h hh g jj
    
    
    disp('5. Extracting 6hr lagged vwnd')
    hh = [];
    for jj = 1:length(surge_sub) 
        
        t6 = datenum(surge_sub(jj, 1) - hours(6));
        g = datenum(t6 - hours(6));
        h = find(Tvwnd > g & Tvwnd <= t6);
        hh = [hh;h];
    end
    vt6_lag = Tvwnd(hh);
    v6 = v4xd10(:,:, hh); %the 30hr lagged uwnd
    clearvars h hh g jj
    

    disp('6. Extracting 0hr lagged uwnd')
    hh = [];
    for jj = 1:length(surge_sub) 
        
        t0 = surge_sub(jj, 1);
        g = datenum(t0 - hours(6));
        h = find(Tvwnd > g & Tvwnd <= t0);
        hh = [hh;h];
    end
    vt0_lag = Tvwnd(hh);
    v0 = v4xd10(:,:, hh); %the 0hr lagged uwnd
    
    %% Save
    disp('Saving .mat file')
    cd 'F:\OneDrive - Knights - University of Central Florida\Daten\MLR\Model_2\Extracted'
    cd(fullfile('F:\OneDrive - Knights - University of Central Florida\Daten\MLR\Model_2\Extracted', tg_lst(ii).name))
    clearvars -except  v0 vt0_lag v6 vt6_lag v12 vt12_lag v18 vt18_lag ... 
        v24 vt24_lag v30 vt30_lag ii tg_lst base_dir b2_dir nan_tgs fid surge_sub
    save('vwnd_lagged.mat')
    clearvars -except base_dir b2_dir ii tg_lst
end
%fclose(fid);     
     
























