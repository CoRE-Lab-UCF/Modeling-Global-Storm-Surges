%% Based on script from Thomas Wahl
%% Load Data; mention that this code is based on Thomas Wahl's code
%Monthly accidetal death in the US (Jan 1973 - Dec 1978)
cd 'C:\Users\mi292519\OneDrive - Knights - University of Central Florida\UCF\Projekt.28\Coursework\CWR5999\Homework_1_export\Sea level data';
Data = xlsread('Marseille_France.xlsx');

%% Fit Linear Trend 
% the model is y = ax +b + E (we are usually only interested in a)
L = length(Data);
X = [Data(:,1) ones(L,1)];

para = X\Data(:,2); %ordinary least squares fit
Lin_trend = X*para;


figure; plot(Data(:,1), Data(:,2))
hold on; plot(Data(:,1), Lin_trend)

% Quadratic trend
para_quad = polyfit(Data(:,1), Data(:,2),2);

%% Fit Linear Trend (Method 3)
para3 = regress(Data(:,2),X);

[para3, CI95] = regress(Data(:,2), X);
[para3, CI99] = regress(Data(:,2), X, 0.01);

%% Calculate Linear trend for the two halves of the data

X1 = X(1:0.5*L, :); X2 = X(0.5*L+1:end,:); % dividing the data into two
[para_1, CI95_1] = regress(Data(1:0.5*L, 2), X1); % linear trend and CI95 for both halves
[para_2, CI95_2] = regress(Data(0.5*L+1:end,2), X2);

Lin_trd1 = X1*para_1; Lind_trd2 = X2*para_2;

% Plotting the confidence intervals of the two halves
Lin_trd11 = X1*CI95_1(:,1); Lin_trd12 = X1*CI95_1(:,2); % the first two confidence intervals
Lin_trd21 = X2*CI95_2(:,1); Lin_trd22 = X2*CI95_2(:,2);

figure; plot(Data(:,1), Data(:,2));
hold on; plot(Data(1:0.5*L, 1), Lin_trd11, 'r'); plot(Data(1:0.5*L, 1), Lin_trd12, 'r');

figure; plot(Data(:,1), Data(:,2));
hold on
plot(Data(1:0.5*L,1), Lin_trd11)
plot(Data(1:0.5*L,1), Lin_trd12)
plot(Data(0.5*L+1:end,1), Lin_trd21)
plot(Data(0.5*L+1:end,1), Lin_trd22)

%% Subtract linear trend and plot residuals
Res = Data(:,2) - Lin_trend; % Removing trends from the raw time series
figure; plot(Data(:,1), Res);

%% Sesasonal cycle
mo = reshape(Res, 12, L/12);
bS = mean(mo,2);
st = repmat(bS, L/12,1);

%get amplitude
Amp = (max(bS) - min(bS))/2;

% get month where the seasonal cycle usually peaks
[Value, Index] = max(bS);

figure
plot(Data(:,1), Res, 'color', 'b')
hold on
plot(Data(:,1), st, 'color', 'r', 'linewidth', 0.5)



%% F. Analysis for the first and last 5 years
Res1 = Res(1:5*12,1); Res2 = Res(L-60+1:end); % picking the first and last five years of Residuals

mo1 = reshape(Res1, 12, 5);
bS1 = mean(mo1,2);
st1 = repmat(bS1, 5,1);

mo2 = reshape(Res2, 12, 5);
bS2 = mean(mo2,2);
st2 = repmat(bS2, 5,1);


Amp1 = (max(bS1) - min(bS1))/2;
Amp2 = (max(bS2) - min(bS2))/2;


[Value1, Index1] = max(bS1);
[Value2, Index2] = max(bS2);

%% G. Find Monthly Anomalies
Resd = Res-st; % Subtracting seasonal cycle from detrended time series
figure; plot(Data(:,1), Resd);
legend('Detrended, Seasonal cycle removed time series')
Resd_max = max(Resd); Resd_min = min(Resd);

%% h. Moving Average of detrended data

for ii = 1:(L - 8*12) % window is extending L-8*12
    ii
    MA(ii,1) = mean(Res(ii:ii+8*12, 1));
end

%Alternative method
mv_avg = movmean(Res, 9*12);

figure; plot(Data(:,1), Res)
hold on; plot(Data(4*12 +1:(L)-(4*12),1), MA, 'color', 'r', 'linewidth', 2);
legend('Detrended, seasonality removed time series', '8 year mean average time series');
plot(Data(:,1), mv_avg, 'color', 'g', 'linewidth', 2);


%% j. Plotting de-trended raw data and 8-year moving average 
figure; plot(Data(:,1), Res);









