
%% Load surge time series data 
basepath = 'C:\Users\mi292519\OneDrive - Knights - University of Central Florida\Daten\Tide_data\Surge_after_T_Tide';
cd (basepath);

% Get list with file names
list = dir('*.mat');

%% Run loop for wavelet transformation to remove ringing in surge

load('C:\Users\mi292519\OneDrive - Knights - University of Central Florida\Daten\Tide_data\Surge_after_T_Tide\cuxhaven-germany-bsh.mat.mat'); % set the data location

x=Surge;
clearvars Surge
      
x(:,2) = find(x); %assigning index to the values in order to capture the index of the NaNs
xx=x;
xx(find(isnan(xx(:,1))), :) = []; % remove nan from the data
%cwt(xx,hours(1)); % plot CWT if you want to see the scalogram to isentify
%where the high energy/ variability is stored.
[wt,periods,coi] = cwt(xx(:,1),hours(1)); % Estimate WT/ period amd COI
figure; cwt(xx(:,1),hours(1));

%% for subseted wt

hr_12 = hours(periods)>= 11 & hours(periods) <= 14; %subsetting the period from 11hr - 13hr
hr_24 = hours(periods)>= 23 & hours(periods) <= 25; %subsetting the period from 23hr to 25hr

%% Remove all subseted components of the wt matrix
wt_clr = wt; 
wt_clr(find(hr_12 == 1), :) = 0; %replacing the new wt for the original wt
wt_clr(find(hr_24 == 1), :) = 0;

rec_ts =icwt(wt_clr)'; %reconstructed time series

%% Putting the NaNs back to their original place
rec_ts(:,2) = xx(:,2);
surge_ts = NaN(length(x),1);
surge_ts(rec_ts(:,2)) = rec_ts(:,1);

%% Plotting
figure; plot(Thour, Whour_detr, 'b'); %Original water level
hold on; plot(Thour, Tide, 'r');
plot(Thour, x(:,1), 'k')
plot(Thour, surge_ts, 'g')
legend('Original Water level', 'Tides' ,'T-Tide Surge', 'Wavelet Transform Surge');
titlechar = strsplit(fname, '.');
toptitle = sprintf('Comparison %s', titlechar{1});
title(toptitle);
datetick('keeplimits');

%datestr(cursor_info.Position(1))






