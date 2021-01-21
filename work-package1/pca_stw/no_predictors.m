% To find the number of predictors for every tide gauge after Stepwise
% regression

b_p = 'F:\OneDrive - Knights - University of Central Florida\Daten\MLR\PCA_Stepwise_confg_13'
cd(b_p)
lst = dir('*.mat');

for t_t = 1:length(lst) 
    t_t
    load(lst(t_t).name);
    %selecting
    ind = inmodel;
    u_in = ind(1:length(pc_uwnd(1,:)));
    ind(1:length(pc_uwnd(1,:))) = [];
    v_in = ind(1:length(pc_vwnd(1,:)));
    ind(1:length(pc_vwnd(1,:))) = [];
    u2_in = ind(1:length(pc_uwnd2(1,:)));
    ind(1:length(pc_uwnd2(1,:))) = [];
    v2_in = ind(1:length(pc_vwnd2(1,:)));
    ind(1:length(pc_vwnd2(1,:))) = [];
    u3_in = ind(1:length(pc_uwnd3(1,:)));
    ind(1:length(pc_uwnd3(1,:))) = [];
    v3_in = ind(1:length(pc_vwnd3(1,:)));
    ind(1:length(pc_vwnd3(1,:))) = [];
    p_in = ind(1:length(pc_prmsl(1,:)));
    ind(1:length(pc_prmsl(1,:))) = [];
    s_in = ind(1:length(pc_sst(1,:)));
    ind(1:length(pc_sst(1,:))) = [];
    g_in = ind(1:length(pc_gpcp(1,:)));
    
    % Finding PCs that passed
    u_stp = find(u_in == 1);
    v_stp = find(v_in == 1);
    u2_stp = find(u2_in == 1);
    v2_stp = find(v2_in == 1);
    u3_stp = find(u3_in == 1);
    v3_stp = find(v3_in == 1);
    p_stp = find(p_in == 1);
    s_stp = find(s_in == 1);
    g_stp = find(s_in == 1);
    
    y = [length(u_stp); length(v_stp); length(u2_stp); length(v2_stp); ... 
        length(u3_stp); length(v3_stp); length(p_stp); length(s_stp); length(g_stp)];
    n = length(find(y ~= 0)); % number of predictors selected after stepwise regression
    n_tg(t_t,1) = lon_t;
    n_tg(t_t,2) = lat_t;
    n_tg(t_t,3) = length(find(y ~= 0));
    if isempty(s_stp) && isempty(g_stp) % check if gpcp and sst are relevant
        n_tg(t_t, 4) = 1;
    else
        n_tg(t_t, 4) = 0;
    end
    
    if isempty(u_stp) && isempty(v_stp) % check if u and v are relevant
        n_tg(t_t, 5) = 1;
    else
        n_tg(t_t, 5) = 0;
    end
    
    if isempty(u2_stp) && isempty(v2_stp) % check if u2 and v2 are relevant
        n_tg(t_t, 6) = 1;
    else
        n_tg(t_t, 6) = 0;
    end
   
    if isempty(u3_stp) && isempty(v3_stp) % check if u3 and v3 are relevant
        n_tg(t_t, 7) = 1;
    else
        n_tg(t_t, 7) = 0;
    end
    
    if isempty(p_stp)  % check if slp is relevant
        n_tg(t_t, 8) = 1;
    else
        n_tg(t_t, 8) = 0;
    end
        
    if isempty(s_stp) && isempty(g_stp) && (length(find(y ~= 0)) == 7) % check if everything except sst and gpcp is relevant
        n_tg(t_t, 9) = 1;
    else
        n_tg(t_t, 9) = 0;
    end    
        
        
    clearvars -except b_p lst t_t n_tg
end
 
%% plotting the no of predictors

load coast
figure; geoshow(lat, long, 'DisplayType', 'polygon', 'Facecolor', [0.85 0.85 0.85]);
hold on; scatter(n_tg(:,1), n_tg(:,2), 150, 'filled') % just plotting the available 615 tide gauges

bb = find(n_tg(:,4) == 1); % model with no gpcp and sst
bb(182,:) = []; % remove 'portlouis-c,mauritius-001-glossdm-bodc_pca_stp.mat' because it has fewer data
gg = find(n_tg(:,9) == 1); % model with 7 predictors and no GPCP or SST
ee = find(n_tg(:,3) == 9); % model with all predictors 
ff = find(n_tg(:,5) == 1); % model without u and v
hh = find(n_tg(:,6) == 1); % model without u2 and v2
ii = find(n_tg(:,7) == 1); % model without u3 and v3
jj = find(n_tg(:,8) == 1); % model with no slp

hold on; scatter(n_tg(ee,1), n_tg(ee,2), 100, 'r', 'filled') % all predictors
hold on; scatter(n_tg(bb,1), n_tg(bb,2), 100, 'y', 'filled') % no gpcp no sst
hold on; scatter(n_tg(jj,1), n_tg(jj,2), 30, 'g', 'filled') % no slp
hold on; scatter(n_tg(ii,1), n_tg(ii,2), 30, 's', 'c', 'filled') % no u3 no v3
legend('none', 'Other model setup', 'All Predictors', 'No GPCP & No SST', 'No SLP', 'No VWND3 & No VWND3');
legend('Orientation','horizontal')
















