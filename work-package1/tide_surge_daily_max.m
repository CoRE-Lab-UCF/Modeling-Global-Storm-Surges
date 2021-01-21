% To subset Tide and Surge values at the time the daily maximum surge occurs %
% This is to be used for the estimation of total still water afte the        %
% application of the statistical models                                      %

bp = 'F:\OneDrive - Knights - University of Central Florida\Daten\Tide_data\Surge_after_T_Tide'
cd(bp)
lss = dir('*.mat');
for wc = 318:length(lss)
    wc
    load(lss(wc).name)
    surge_hr = [Thour Surge];
    clearvars -except surge_hr Tide bp lss wc
    ti_sg_daily = [];%surge_hr(~isfinite(surge_hr(:,2)),:) = [];
     aa = datevec(surge_hr(:,1)); 
     bb = datetime(aa(:,1:3)); 
     cc = unique(bb); % making a unique list of the days
     count = 0;
      for ss = 1:length(cc)
        ind = find(cc(ss) == bb);
        d = surge_hr(ind,2);
        [e f] = max(d); % Picking the daily max surge
        ti_sg_daily = [ti_sg_daily; [datenum(surge_hr(f + count)) Tide(f + count) e]];
        count = count + length(ind);
      end
     cd 'F:\OneDrive - Knights - University of Central Florida\Daten\Tide_data\Tide_Surge@dailymax'
     save(strcat(lss(wc).name, '.mat'))
     clearvars -except bp lss wc
     cd(bp)
end


 


     
     