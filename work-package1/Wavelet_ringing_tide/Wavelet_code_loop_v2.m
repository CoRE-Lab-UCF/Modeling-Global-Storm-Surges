
% Load surge time series data 
cd 'C:\Users\mi292519\OneDrive - Knights - University of Central Florida\Daten\Tide_data\Surge_ringing_NaN'; %ALWAYS CHANGE BEFORE RUNNING
fid = fopen('No_Surge.txt', 'a');

base_path = 'C:\Users\mi292519\OneDrive - Knights - University of Central Florida\Daten\Tide_data\Surge_after_T_Tide';
cd(base_path);
% Get list with file names
list1 = dir('*.mat.mat');

% Run loop for wavelet transformation to remove ringing in surge
for ll = 1:length(list1)
    ll
    cd(base_path);
    tname = list1(ll).name;
    load(tname)
    x=Surge;
    
    if isnan(Surge) == ones(length(Surge),1) %checking if the surge is NaN 
        cd 'C:\Users\mi292519\OneDrive - Knights - University of Central Florida\Daten\Tide_data\Surge_ringing_NaN'; %ALWAYS CHANGE BEFORE RUNNING
        %fid = fopen('No_Surge.txt', 'w');
        fprintf(fid, 'll = %d; tname = %s \n', ll, tname);
        continue
    end
        
    clearvars Surge basepath
    x(:,2) = find(x); %assigning index to the values in order to capture the index of the NaNs
    xx=x;
    xx(find(isnan(xx(:,1))), :) = []; % remove nan from the data
    %cwt(xx,hours(1)); % plot CWT if you want to see the scalogram to isentify
    %where the high energy/ variability is stored.
    [wt,periods,coi] = cwt(xx(:,1),hours(1)); % Estimate WT/ period amd COI
    %figure; cwt(xx(:,1),hours(1));
    
    
    % Subset wt to 12hr and 24hr region
    hr_12 = hours(periods)>= 11 & hours(periods) <= 14; %subsetting the period from 11hr - 13hr
    hr_24 = hours(periods)>= 23 & hours(periods) <= 26; %subsetting the period from 23hr to 25hr
    wt_12 = wt(find(hr_12 == 1), :);
    wt_24 = wt(find(hr_24 == 1), :);
    
    [c,d] = size(wt_12); [e,f] = size(wt_24);
    for qq = 1:c
        for rr = 1:d
            mag12(qq, rr) = sqrt(real(wt_12(qq,rr))^2 + imag(wt_12(qq,rr))^2); %computing the modulus of the complex numbers
        end
    end

    for ss = 1:e
        for tt = 1:f
            mag24(ss, tt) = sqrt(real(wt_24(ss,tt))^2 + imag(wt_24(ss,tt))^2);
        end
    end

    %figure; histogram(mag12); figure; histogram(mag24);
    
    % Check outliers
    sigma = 5; %setting the standard deviation
    cutoff12 = mean(mag12(:)) + sigma*std(mag12(:)); %applying the five std from the mean as a cut-off 
    cutoff24 = mean(mag24(:)) + sigma*std(mag24(:));
    wt_clr = wt; wt12_new = wt_12; wt24_new = wt_24;
    wt12_new(find(mag12 > cutoff12)) = 0; %replacing the wt with 0
    wt24_new(find(mag24 > cutoff24)) = 0;
    wt_clr(find(hr_12 == 1), :) = wt12_new; %replacing the new wt for the original wt
    wt_clr(find(hr_24 == 1), :) = wt24_new;

    rec_ts =icwt(wt_clr)'; %reconstructed time series

    % Putting the NaNs back to their original place
    rec_ts(:,2) = xx(:,2);
    surge_ts = NaN(length(x),1);
    surge_ts(rec_ts(:,2)) = rec_ts(:,1);

    % Removing Outliers and setting them to NaN
    out_12 = wt_12; out_24 = wt_24;
    out_12(find(mag12 > cutoff12)) = NaN; %replacing the wt with 0
    out_24(find(mag24 > cutoff24)) = NaN;
    outliers = [out_12; out_24]; % concatenate the two arrays rowwise
    [b,n] = size(outliers);

    check = ones(n,1);  % the idea is that if we find a NaN in any of the columns
    % that means the surge at that timestep has some ringing and we want to
    % find that time step and remove the surge ts 
    for bb = 1:b
        for nn = 1:n
            if isnan(outliers(bb,nn))
                check(nn,1) = 0;
            end
        end
    end
    xx_nan = xx;
    xx_nan(find(check == 0), 1) = NaN; 
    xx_nan_ts = NaN(length(x),1); % creating a NaN array with the length of the raw tide gauge
    xx_nan_ts(xx_nan(:,2)) = xx_nan(:,1); % putting back the original NaNs to the ts
    Perc_nan = length(find(isnan(xx_nan)))*100/length(xx); %calculate percentage of NaN values

    
    % Plotting
    %figure; plot(Thour, Whour_detr, 'b'); %Raw tide gauge data
    %hold on; plot(Thour, Tide, 'r');
    %plot(Thour, x(:,1), 'k')
    %plot(Thour, surge_ts, 'g')
    %plot(Thour, xx_nan_ts, 'p')
    %legend('Raw tide gauge data', 'Tidal fit' ,'Surge(T-Tide)', 'Surge(Wavelet Transform)', 'Surge(Ringing == NaN)');
    %titlechar = strsplit(fname, '-');
    %toptitle = sprintf('%s with %d std and %.2f%% of data removed', titlechar{1}, sigma ,Perc_nan);
    %title(toptitle);
    %datetick('keeplimits');
    
    % to automatically name the .mat files
    folder = 'C:\Users\mi292519\OneDrive - Knights - University of Central Florida\Daten\Tide_data\Surge_ringing_NaN'
    tname_str = strsplit(list1(ll).name, ';');
    baseFileName = sprintf('%s_wt.mat', tname_str{1});
    %c = strsplit(baseFileName, '_'); %splitting the tname to get the name of the file for saving
    fullMatFileName = fullfile(folder, baseFileName);
    clearvars -except sigma Perc_nan tname base_path list1 ll fullMatFileName surge_ts Thour Whour_detr Tide x fid xx_nan xx_nan_ts Perc_nan;
    save(fullMatFileName);
    clearvars -except base_path list1 ll fid;

end
fclose(fid);