% Find corresponding match for surge/skew surge

cd 'C:\Users\mi292519\OneDrive - Knights - University of Central Florida\Daten\Tide_data\Skew_surge'
load('astoria,or-572a-usa-uhslc.mat_mean_sk.mat')


%% 
cd 'C:\Users\mi292519\OneDrive - Knights - University of Central Florida\Daten\Tide_data\Skew_surge'
load('astoria,or-572a-usa-uhslc.mat_mean_sk.mat')
ymd_pred = datevec(Tpred); %predictor year, month, date format
ymd_mat = datenum(ymd_pred(:,1:3)); % taking only the ymd format to extract
%daily values of predictors
pp_ind = []; % index of surge_daily where surge and predictor have common dates
for pp = 1:length(Tpred)
    %extract predictor values for respective days of daily surge values
    pp_ind = [pp_ind; find(ymd_mat(pp) == surge_daily(:,1))];
end

surge_new = surge_daily(pp_ind,:); %surge values matching predictor date

clearvars -except Tpred udmax vdmax lat_pred lon_pred surge_new Lat Lon



% Compare timestamp in predictors

load('SST.mat')
clearvars -except Tsst
load('PRMSL.mat')
clearvars -except Tsst Tprmsl
load('GPCP.mat')
clearvars -except Tsst Tprmsl Tgpcp
load('CCMP.mat')
clearvars -except Tsst Tprmsl Tgpcp Twind

a = datevec(Tgpcp); b = datevec(Tprmsl); c = datevec(Tsst); d = datevec(Twind);
Tgpcp(:,2) = datenum(a(:,1:3));
Tprmsl(:,2) = datenum(b(:,1:3));
Tsst(:,2) = datenum(c(:,1:3));
Twind(:,2) = datenum(d(:,1:3));
clearvars a b c d 

% finding min and max dates to limit matrices
a = [Twind(1,2) Tsst(1,2) Tgpcp(1,2) Tprmsl(1,2)];
b = [Twind(end,2)  Tsst(end,2)  Tgpcp(end,2)  Tprmsl(end,2)]; 
first_date = max(a);
last_date = min(b);




%% Predictand + Predictor

% Load surge/skew surge data

cd 'C:\Users\mi292519\OneDrive - Knights - University of Central Florida\Daten\Tide_data\Skew_surge'
load('astoria,or-572a-usa-uhslc.mat_mean_sk.mat')
clearvars -except sk_daily surge_daily

% Refine CCMP data to match surge time series

cd 'C:\Users\mi292519\OneDrive - Knights - University of Central Florida\Daten\MLR'
load('CCMP.mat')
clearvars -except vmax_daily umax_daily Twind surge_daily sk_daily

ymd_pred = datevec(Twind); %predictor year, month, date format
ymd_mat = datenum(ymd_pred(:,1:3)); % taking only the ymd format to extract daily values of predictors

pp_ind = []; % index of surge_daily where surge and predictor have common dates

if length(surge_daily) > length(ymd_mat)
    for pp = 1:length(Twind)
        pp_ind = [pp_ind; find(ymd_mat(pp) == surge_daily(:,1))];
    end
    
    surge_new = surge_daily(pp_ind,:); %surge values matching predictor date
    umax_new = umax_daily(:,:,find(isfinite(pp_ind))); % choosing only predictors without nans
    vmax_new = vmax_daily(:,:, find(isfinite(pp_ind)));

else
    for pp = 1:length(Twind)
        pp_ind = [pp_ind; find(surge_daily(:,1) == ymd_mat(pp))];
    end 
    
    umax_new = umax_daily(:,:,pp_ind); 
    vmax_new = vmax_daily(:,:,pp_ind);
    surge_new = surge_daily(find(isfinite(pp_ind)),:);
end


























