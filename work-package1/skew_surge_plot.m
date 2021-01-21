% Create a matrix with skew surge and NTR 
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

% plot time series of NTR and Skew Surge
subplot(1,2,1);plot(surge_all2(:,1), surge_all2(:,2), 'g');
hold on; plot(surge_all2(:,1), surge_all2(:,3), 'b');
plot(surge_all2(:,1), surge_all2(:,2) - surge_all2(:,3), 'r');
datetick('keeplimits');
legend('Daily mean Surge - T_Tide', 'Daily mean Skew Surge', 'diff')
titlechar = strsplit(fname, '-');
toptitle = sprintf('%s', titlechar{1});
title(toptitle);

% plot scatterplot of NTR and Skew surge
subplot(1,2,2); scatter(surge_all2(:,2), surge_all2(:,3));
hline = refline([1, 0]); hline.Color = 'r';
xlabel('Daily mean Surge T-Tide (m)'); ylabel('Daily mean skew surge (m)');
title(toptitle);





















