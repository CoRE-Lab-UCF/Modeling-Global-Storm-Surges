% Get the list of files
cd 'F:\OneDrive - Knights - University of Central Florida\Daten\Tide_data\TG_testing'
mat_file = dir('*.mat');


for ii = 2:2%length(mat_file)%length(mat_file)
    ii
    fname = mat_file(ii).name;
    fname
    load(fname)
    cd 'F:\OneDrive - Knights - University of Central Florida\Daten\Coden'
    [Y,DQ,ts,tide,pred,pred_all,surge,SK,HW,LW,HWp,LWp,HWpa,LWpa,TCn,TCa,TCp] = Skew_surge_v4(Thour,Whour_detr,Lat);
    
%     if sum(isfinite(surge)) == 0 % avoid tide gauges that couldn't be analyzed with T_Tide
%         cd 'F:\OneDrive - Knights - University of Central Florida\Daten\Tide_data\Skew_surge_max_v2'; %ALWAYS CHANGE BEFORE RUNNING
%         fprintf(fid, 'ii = %d; Tide_Gauge = %s \n', ii, fname);
%         continue;
%     end

    % Compute daily maximum surge (from T_Tide)
    disp('Computing daily maximum surge');
    surge_hr = [Thour surge];
    surge_daily = [];%surge_hr(~isfinite(surge_hr(:,2)),:) = [];
    a = datevec(surge_hr(:,1)); 
    b = datetime(a(:,1:3)); 
    c = unique(b); % making a unique list of the days
    for ss = 1:length(c)
        ind = find(c(ss) == b);
        d = surge_hr(ind,2);
        e = max(d); % Picking the daily max surge
        surge_daily = [surge_daily; [datenum(c(ss)) e]];
    end
    clearvars a b c d e ind

    % Compute daily maximum skew surge
    disp('Computing daily maximum skew surge');
    sk_tage = SK;
    sk_daily = []; sk_tage(~isfinite(sk_tage(:,1)),:) = [];
    a = datevec(sk_tage(:,1));
    b = datetime(a(:,1:3));
    c = unique(b);
    for tt = 1:length(c)
        ind = find(c(tt) == b);
        d = sk_tage(ind,2);
        e = max(d);
        sk_daily = [sk_daily; [datenum(c(tt)) e]];
    end
    
    %few_yr = [];
    %disp('Checking if there is at least 2 years of data');
    %if length(surge_daily) < 730 || length(sk_daily) < 730
    %    few_yr = [few_yr; ii];
    %    continue;
    %end
        
    % Save as .mat file
    disp('Saving as .mat files')
    folder = 'F:\OneDrive - Knights - University of Central Florida\Daten\Tide_data\TG_testing_surge'
    fname_str = strsplit(mat_file(ii).name, ';');
    baseFileName = sprintf('%s_sk.mat', fname_str{1});
    fullMatFileName = fullfile(folder, baseFileName);
    %clearvars -except 
    save(fullMatFileName);
    clearvars -except ii mat_file fid pool pool_sort pp few_yr
end
% fclose(fid);