
% Load surge time series data 
base_path = 'C:\Users\mi292519\OneDrive - Knights - University of Central Florida\Daten\Tide_data\Surge_after_T_Tide';
cd(base_path);

% Get list with file names
list1 = dir('*.mat.mat');

% Run loop for wavelet transformation to remove ringing in surge
for ii = 1:length(list1)
    ii
    cd(base_path);
    fname = list1(ii).name;
    load(fname)
    x=Surge;
    clearvars Surge basepath
    x(:,2) = find(x); %assigning index to the values in order to capture the index of the NaNs
    xx=x;
    xx(find(isnan(xx(:,1))), :) = []; % remove nan from the data
    %cwt(xx,hours(1)); % plot CWT if you want to see the scalogram to isentify
    %where the high energy/ variability is stored.
    [wt,periods,coi] = cwt(xx(:,1),hours(1)); % Estimate WT/ period amd COI
    %figure; cwt(xx(:,1),hours(1));
    
    % Compute Statistics
    %[m,n] = size(wt);
    %for aa = 1:m
        %for bb = 1:n
        %mag(aa, bb) = sqrt(real(wt(aa,bb))^2 + imag(wt(aa,bb))^2);
        %end
    %end
    %figure; histogram(mag)
    
    % Subset wt to 12hr and 24hr region
    hr_12 = hours(periods)>= 11 & hours(periods) <= 14; %subsetting the period from 11hr - 13hr
    hr_24 = hours(periods)>= 23 & hours(periods) <= 25; %subsetting the period from 23hr to 25hr
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
    cutoff12 = mean(mag12(:)) + 5*std(mag12(:)); %applying the five std from the mean as a cut-off 
    cutoff24 = mean(mag24(:)) + 5*std(mag24(:));
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

    % Plotting
    %figure; plot(Thour, Whour_detr, 'b'); %Original water level
    %hold on; plot(Thour, Tide, 'r');
    %plot(Thour, x(:,1), 'k')
    %plot(Thour, surge_ts, 'g')
    %legend('Original Water level', 'Tides' ,'T-Tide Surge', 'Wavelet Transform Surge');
    %title(['Comparison of Surge and Tide for Sandiego Tide gauge']) %change name
    %datetick('keeplimits');
    
    %to automatically name the .mat files
    folder = 'C:\Users\mi292519\OneDrive - Knights - University of Central Florida\Daten\Tide_data\Surge_after_WT'
    fname_str = strsplit(list1(ii).name, '.');
    baseFileName = sprintf('%s_wt.mat', fname_str{1});
    %c = strsplit(baseFileName, '_'); %splitting the fname to get the name of the file for saving
    fullMatFileName = fullfile(folder, baseFileName);
    clearvars -except base_path list1 ii fullMatFileName surge_ts Thour Whour_detr Tide x;
    save(fullMatFileName);
    clearvars -except base_path list1 ii;

end
