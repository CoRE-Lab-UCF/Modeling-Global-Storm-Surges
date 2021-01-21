
%% Load surge time series data 
basepath = 'C:\Users\mi292519\OneDrive - Knights - University of Central Florida\Daten\Tide_data\Surge_after_T_Tide';
cd (basepath);

% Get list with file names
list = dir('*.mat');

%% Run loop for wavelet transformation to remove ringing in surge

load('C:\Users\mi292519\OneDrive - Knights - University of Central Florida\Daten\Tide_data\Surge_after_T_Tide\lajolla_scrippspier_-usa-noaa.mat.mat'); % set the data location

x=Surge;
clearvars Surge
      
x(:,2) = find(x); %assigning index to the values in order to capture the index of the NaNs
xx=x;
xx(find(isnan(xx(:,1))), :) = []; % remove nan from the data
%cwt(xx,hours(1)); % plot CWT if you want to see the scalogram to isentify
%where the high energy/ variability is stored.
[wt,periods,coi] = cwt(xx(:,1),hours(1)); % Estimate WT/ period amd COI
figure; cwt(xx(:,1),hours(1));

%% Compute Statistics
[m,n] = size(wt);
for aa = 1:m
    for bb = 1:n
        mag(aa, bb) = sqrt(real(wt(aa,bb))^2 + imag(wt(aa,bb))^2);
    end
end
%figure; histogram(mag)

%% for subseted wt
hr_12 = hours(periods)>= 11 & hours(periods) <= 14; %subsetting the period from 11hr - 13hr
hr_24 = hours(periods)>= 23 & hours(periods) <= 26; %subsetting the period from 23hr to 25hr
wt_12 = wt(find(hr_12 == 1), :);
wt_24 = wt(find(hr_24 == 1), :);

[c,d] = size(wt_12); [e,f] = size(wt_24);
for rr = 1:c
    for ss = 1:d
        mag12(rr, ss) = sqrt(real(wt_12(rr,ss))^2 + imag(wt_12(rr,ss))^2); %computing the modulus of the complex numbers
    end
end

for qq = 1:e
    for pp = 1:f
        mag24(qq, pp) = sqrt(real(wt_24(qq,pp))^2 + imag(wt_24(qq,pp))^2);
    end
end

%figure; histogram(mag12); figure; histogram(mag24);


%% Check outliers
sigma = 5; %standard deviation
cutoff12 = mean(mag12(:)) + sigma*std(mag12(:)); %applying the five std from the mean as a cut-off 
cutoff24 = mean(mag24(:)) + sigma*std(mag24(:));
wt_clr = wt; wt12_new = wt_12; wt24_new = wt_24;
wt12_new(find(mag12 > cutoff12)) = 0; %replacing the wt with 0
wt24_new(find(mag24 > cutoff24)) = 0;
wt_clr(find(hr_12 == 1), :) = wt12_new; %replacing the new wt for the original wt
wt_clr(find(hr_24 == 1), :) = wt24_new;

rec_ts =icwt(wt_clr)'; %reconstructed time series

%% Putting the NaNs back to their original place
rec_ts(:,2) = xx(:,2);
surge_ts = NaN(length(x),1);
surge_ts(rec_ts(:,2)) = rec_ts(:,1);


%% Removing Outliers and setting them to NaN
out_12 = wt_12; out_24 = wt_24;
out_12(find(mag12 > cutoff12)) = NaN; %replacing the wt with 0
out_24(find(mag24 > cutoff24)) = NaN;
outliers = [out_12; out_24];
[b,n] = size(outliers);

check = ones(n,1);
for bb = 1:b
    for nn = 1:n
        if isnan(outliers(bb,nn))
            check(nn,1) = 0;
        end
    end
end
xx_nan = xx;
xx_nan(find(check == 0), 1) = NaN;
xx_nan_ts = NaN(length(x),1);
xx_nan_ts(xx_nan(:,2)) = xx_nan(:,1);
Perc_nan = length(find(isnan(xx_nan)))*100/length(xx); %calculate percentage of NaN values

%% Plotting
figure; plot(Thour, Whour_detr, 'b'); %Raw tide gauge data
hold on; plot(Thour, Tide, 'r');
plot(Thour, x(:,1), 'k')
plot(Thour, surge_ts, 'g')
plot(Thour, xx_nan_ts, 'p')
legend('Raw tide gauge data', 'Tidal fit' ,'Surge(T-Tide)', 'Surge(Wavelet Transform)', 'Surge(Ringing == NaN)');
titlechar = strsplit(tname, '-');
toptitle = sprintf('%s with %d std and %.2f%% of data removed', titlechar{1}, sigma ,Perc_nan);
title(toptitle);
datetick('keeplimits');


%% Save as .mat file

folder = 'C:\Users\mi292519\OneDrive - Knights - University of Central Florida\Daten\Tide_data\Sonstig\WT_testing\Sandiego'
save_name = sprintf('%s.mat', toptitle);
mat_name = fullfile(folder, save_name);
clearvars wt wt_clr mag;
save(mat_name);








