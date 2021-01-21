%to convert hourly surge to daily max surge with a time stamp     
disp('Computing daily maximum surge');
     surge_hr = [Thour Surge];
     clearvars -except surge_hr
     surge_daily = [];%surge_hr(~isfinite(surge_hr(:,2)),:) = [];
     aa = datevec(surge_hr(:,1)); 
     bb = datetime(aa(:,1:3)); 
     cc = unique(bb); % making a unique list of the days
     count = 0;
     for ss = 1:length(cc)
        ind = find(cc(ss) == bb);
        d = surge_hr(ind,2);
        [e f] = max(d); % Picking the daily max surge
        surge_daily = [surge_daily; [datenum(surge_hr(f + count)) e]];
        count = count + length(ind);
     end
     
     