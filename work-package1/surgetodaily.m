base_pt = 'F:\OneDrive - Knights - University of Central Florida\Daten\MLR\TG_pct_pcd_17yrs';
cd(base_pt)
lst = dir(); lst(1:2) = []; 
 for tt = 3:length(lst)
     tt
     cd(fullfile(base_pt, lst(tt).name))
     
     pcd = sprintf('%s_daily.mat', lst(tt).name);
     load(pcd);
     clearvars -except base_pt lat_t lon_t surge_hr Thour tt lst Surge 
     % Compute daily maxsimum surge (from T_Tide)
     disp('Computing daily maximum surge');
     %surge_hr = [Thour Surge];
     nn = find(isnan(surge_hr(:,2)));
     surge_hr(nn,:) = [];
     surge_daily = [];%surge_hr(~isfinite(surge_hr(:,2)),:) = [];
     aa = datevec(surge_hr(:,1)); 
     bb = datetime(aa(:,1:3)); 
     cc = unique(bb); % making a unique list of the days
     ll = 0;
     for ss = 1:length(cc)
        ind = find(cc(ss) == bb);
        d = surge_hr(ind,2);
        [e1 e2] = max(d); % Picking the daily max surge
        surge_daily = [surge_daily; surge_hr(e2+ll, :)];
        ll = ll + length(ind);
     end
     clearvars a b c d e ind
     save_name = sprintf('%s_daily_new.mat', lst(tt).name);
     save(save_name);
     clearvars -except base_pt lst tt 
     cd(base_pt)
 end
 






    
    
    
    

    