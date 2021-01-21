%% Get the list of files
addpath(genpath('C:\Users\mi292519\OneDrive - Knights - University of Central Florida\Daten\Coden'))
cd 'C:\Users\mi292519\OneDrive - Knights - University of Central Florida\Daten\Tide_data\TG_mat_global_unique'
mat_file = dir('*.mat');

%% Run analysis for gauges with DWr > 75 
%pool = [120 124 144 151 152 160 168 174 175 188 195 214 215 23 306 314 322 34 385 422 453 498 510 511 51 54 565 588 607 639 640 641 652 663 692 695 69 716 719 725 741 773 775 814 833 866 902];
%pool_sort = sort(pool);
%% Run loop for Skew surge analysis 
cd 'C:\Users\mi292519\OneDrive - Knights - University of Central Florida\Daten\Tide_data\Skew_surge'
fid = fopen('Ausnahmen.txt', 'wt'); % Create a txt file to write gauges that have problems

for ii = 487:length(mat_file)%length(pool_sort) %started with 487
    ii % = pool_sort(pp)
    fname = mat_file(ii).name;
    load(fname)
    cd 'C:\Users\mi292519\OneDrive - Knights - University of Central Florida\Daten\Coden'
    [Y,DQ,ts,tide,pred,pred_all,surge,SK,HW,LW,HWp,LWp,HWpa,LWpa,TCn,TCa,TCp] = Skew_surge_v3(Thour,Whour_detr,Lat);
    
    if isnan(surge) % avoid tide gauges that couldn't be analyzed with T_Tide
        cd 'C:\Users\mi292519\OneDrive - Knights - University of Central Florida\Daten\Tide_data\Skew_surge'; %ALWAYS CHANGE BEFORE RUNNING
        fprintf(fid, 'ii = %d; Tide_Gauge = %s \n', ii, fname);
        continue;
    end
    % Compute daily maximum surge (from T_Tide)
    disp('8. Computing daily mean surge');
    surge_hr = [Thour surge];
    surge_daily = [];%surge_hr(~isfinite(surge_hr(:,2)),:) = [];
    a = datevec(surge_hr(:,1)); 
    b = datetime(a(:,1:3)); 
    c = unique(b); % making a unique list of the days
    for ss = 1:length(c)
        ind = find(c(ss) == b);
        d = surge_hr(ind,2);
        e = mean(d); % Picking the daily max surge
        surge_daily = [surge_daily; [datenum(c(ss)) e]];
    end
    clearvars a b c d e ind

    % Compute daily maximum skew surge
    disp('9. Computing daily mean skew surge');
    sk_tage = SK;
    sk_daily = []; sk_tage(~isfinite(sk_tage(:,1)),:) = [];
    a = datevec(sk_tage(:,1));
    b = datetime(a(:,1:3));
    c = unique(b);
    for tt = 1:length(c)
        ind = find(c(tt) == b);
        d = sk_tage(ind,2);
        e = mean(d);
        sk_daily = [sk_daily; [datenum(c(tt)) e]];
    end
    
    few_yr = [];
    disp('10. Checking if there is at least 2 years of data');
    if length(surge_daily) < 730 && length(sk_daily) < 730
        few_yr = [few_yr; ii];
        continue;
    end
        
    % Save as .mat file
    disp('11. Saving as .mat files')
    folder = 'C:\Users\mi292519\OneDrive - Knights - University of Central Florida\Daten\Tide_data\Skew_surge'
    fname_str = strsplit(mat_file(ii).name, ';');
    baseFileName = sprintf('%s_mean_sk.mat', fname_str{1});
    fullMatFileName = fullfile(folder, baseFileName);
    %clearvars -except 
    save(fullMatFileName);
    clearvars -except ii mat_file fid %pp pool pool_sort
end
fclose(fid);