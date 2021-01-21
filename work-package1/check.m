%% Compute daily maximum surge (from T_Tide)
surge_hr = [Thour surge];
surge_hr(~isfinite(surge_hr(:,2)),:) = [];surge_daily = [];
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

%% Compute daily maximum skew surge
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


%% Scatterplot
for jj = 1: length(sk_daily)
    ff = find(sk_daily(jj,1) == surge_daily(:,1));
    if isfinite(ff)
        surge_all(jj,1) = sk_daily(jj,1);
        surge_all(jj,2) = sk_daily(jj,2);
        surge_all(jj,3) = surge_daily(ff,2);
    else
        surge_all(jj,1) = NaN;
        surge_all(jj,2) = NaN;
        surge_all(jj,3) = NaN;
    end
end

figure; plot(surge_all(:,1), surge_all(:,2));
hold on; plot(surge_all(:,1), surge_all(:,3));
datetick('keeplimits');
legend('Daily max Surge - T_Tide', 'Daily max Skew Surge')
titlechar = strsplit(fname, '-');
toptitle = sprintf('%s', titlechar{1});
title(toptitle);

figure; scatter(surge_all(:,2), surge_all(:,3));
xlabel('Daily max skew surge (m)'); ylabel('Daily max Surge T-Tide (m)');
title(toptitle);

%% Scatterplot v2
st_sk = sk_daily(1,1); st_su = surge_daily(1,1); % finding starting date for skew surge and surge
end_sk = sk_daily(end,1); end_su = surge_daily(end,1); % finding end date
t = (max(st_sk, st_su):1:min(end_sk,end_su))'; % creating continuous vector of time 
surge_all = NaN(length(t),3);
surge_all(:,1) = t;
for jj = 1:length(t)
    ind2 = find(surge_daily == surge_all(jj,1));
    ind3 = find(sk_daily == surge_all(jj,1));
    if isempty(ind2)
        surge_all(jj,2) = NaN;
    else
        surge_all(jj,2) = surge_daily(ind2,2);
    end
    
    if isempty(ind3)
        surge_all(jj,3) = NaN;
    else
        surge_all(jj,3) = sk_daily(ind3,2);
    end
end

surge_all2 = surge_all;
aa = find(isnan(surge_all2(:,2)));
bb = find(isnan(surge_all2(:,3)));
cc = [aa;bb]; dd = unique(cc);
surge_all2(dd,:) = [];


figure; plot(surge_all2(:,1), surge_all2(:,2));
hold on; plot(surge_all2(:,1), surge_all2(:,3));
datetick('keeplimits');
legend('Daily max Surge - T_Tide', 'Daily max Skew Surge')
titlechar = strsplit(fname, '-');
toptitle = sprintf('%s', titlechar{1});
title(toptitle);

figure; scatter(surge_all2(:,2), surge_all2(:,3));
hline = refline([1, 0]); hline.Color = 'r';
xlabel('Daily max skew surge (m)'); ylabel('Daily max Surge T-Tide (m)');
title(toptitle);





















