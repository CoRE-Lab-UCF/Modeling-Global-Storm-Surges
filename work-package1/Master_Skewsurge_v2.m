%% Get the list of files
addpath(genpath('C:\Users\mi292519\OneDrive - Knights - University of Central Florida\Daten\Coden'))
cd 'C:\Users\mi292519\OneDrive - Knights - University of Central Florida\Daten\Tide_data\TG_mat_global_unique'
mat_file = dir('*.mat');

%% Run loop for Skew surge analysis 

for ii = 44:44%length(mat_file) % stopped at 169
    ii
    fname = mat_file(ii).name;
    load(fname)
    cd 'C:\Users\mi292519\OneDrive - Knights - University of Central Florida\Daten\Coden'
    [Y,DQ,ts,tide,pred,pred_all,surge,SK,HW,LW,HWp,LWp,HWpa,LWpa,TCn,TCa,TCp] = Skew_surge_v2(Thour,Whour_detr,Lat);
    
    % Compute daily maximum surge (from T_Tide)
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
    
    % Save as .mat file
    folder = 'C:\Users\mi292519\OneDrive - Knights - University of Central Florida\Daten\Tide_data\Skew_surge'
    fname_str = strsplit(mat_file(ii).name, ';');
    baseFileName = sprintf('%s_sk.mat', fname_str{1});
    fullMatFileName = fullfile(folder, baseFileName);
    %clearvars -except 
    save(fullMatFileName);
    clearvars -except ii mat_file 
end

