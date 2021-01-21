
% Load surge time series data 
load('C:\Users\MD508867\OneDrive - University of Central Florida\Reserach_03_14_2018\Mike_work\Surge_ringing.mat'); % set the data location

x=Surge;
clearvars Surge
      
xx=x;
xx(isnan(xx)==1)=[]; % remove nan from the data
%cwt(xx,hours(1)); % plot CWT if you want to see the scalogram to isentify
%where the high energy/ variability is stored.
[wt,periods,coi] = cwt(xx,hours(1)); % Estimate WT/ period amd COI

% Localized removal of specific frequency bands 
% CWT shows strong energy concentration from 8 to 34 hours period
% best result obtained when remove frequency from approximately 3.46 to 34 hours scale
% this remove the periodic components almost completely from the series
% which is basically tides
R_P=7:40; % index of specific removing period 3.46 hr to 32.45 hr.(This canbe chnaged for the best result...like of trade off) 
wt_R=wt;
%idx1=find(periods>=10 & periods<=15);
wt_R(R_P(1):R_P(end),:)=0; % change the wavelet coefficient to zero for the selected periods
rec_x=icwt(wt_R); % reconstruct the series

%%%% Plot the series

figure; plot(xx); % original data without NaN
figure; plot(rec_x) % Reconstructed data without NAN

%%% Need to infill the mothers series NaN values in the reconstructed
%%% series as per the index of mother series

%%%%....................................................







