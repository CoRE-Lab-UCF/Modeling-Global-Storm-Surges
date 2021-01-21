% To compute pca and stepwise regression 
% Select data
disp('Step #1 - Select data')
cd 'F:\OneDrive - Knights - University of Central Florida\Daten\MLR\PCA_Stepwise_confg_10'
%fid = fopen('Missed_gauges.txt', 'a'); % Create a txt file to write gauges that have problems

basepath =  'F:\OneDrive - Knights - University of Central Florida\Daten\MLR\TG_pct_pcd'
list_tg = dir(basepath); list_tg(1:2) = []; % making a list for the tg folders

pool = 159%[680 78 801 218 854 378]';  %to test a few gauges

for pp = 1:length(pool)%t = 1:3%length(list_tg)
    t = pool(pp)
    cd(fullfile(basepath, list_tg(t).name))
    t 
    disp(list_tg(t).name)
    list_pp = dir('*.mat'); % making a list of the predictand and predictor files
    
    disp('1.11 - Loading wind data')
    load('CCMP.mat'); clearvars -except pp pool basepath list_tg t Twind umax_daily vmax_daily fid lat_t lon_t
    pcd = dir('*_sk.mat'); % loading predictand file, file ends with _sk
    load(pcd.name);
    clearvars -except pp pool basepath list_tg t Twind umax_daily vmax_daily sk_daily surge_daily lat_t lon_t
    
    disp('1.12 - Loading precipitation data')
    load('GPCP.mat'); 
    clearvars -except pp pool basepath list_tg t Twind umax_daily ... 
        vmax_daily sk_daily surge_daily Tgpcp gpcp_daily lat_t lon_t
    
    disp('1.13 - Loading sea level pressure data')
    load('PRMSL.mat'); 
    clearvars -except pp pool basepath list_tg t Twind umax_daily lat_t lon_t ... 
        vmax_daily sk_daily surge_daily Tgpcp gpcp_daily Tprmsl prmsl_daily
    
    disp('1.14 - Loading sea surface temperature data')
    load('SST.mat'); 
    clearvars -except pp pool basepath list_tg t Twind umax_daily lat_t lon_t ... 
        vmax_daily sk_daily surge_daily Tgpcp gpcp_daily Tprmsl prmsl_daily Tsst sst_daily
    
    %Subsetting data 
    disp('1.2 - Subset dates for pct and pcd')
    tw = datevec(Twind); tw = datenum(tw(:,1:3));
    ts = datevec(Tsst); ts = datenum(ts(:,1:3));
    tg = datevec(Tgpcp); tg = datenum(tg(:,1:3));
    tp = datevec(Tprmsl); tp = datenum(tp(:,1:3));
    
    
    a = [tw(1,1) ts(1,1) tg(1,1) tp(1,1) surge_daily(1,1) sk_daily(1,1)]; %finding starting date
    b = [tw(end,1) ts(end,1) tg(end,1) tp(end,1) surge_daily(end,1) sk_daily(end,1)];
    dat = (max(a):min(b))'; % creating continuous vector of time
    
    if min(b) < max(a)
        cd 'F:\OneDrive - Knights - University of Central Florida\Daten\MLR\PCA_Stepwise_confg_10'
        fid = fopen('Missed_gauges.txt', 'a');
        fprintf(fid, 't = %d; Tide_Gauge = %s \n', t, list_tg(t).name);
        continue; % if there is no overlap beteween pcts and pcd, abort!
    end
    
    %Sizes of the matrices
    [u1 u2 u3] = size(umax_daily); [v1 v2 v3] = size(vmax_daily);
    [s1 s2 s3] = size(sst_daily); [g1 g2 g3] = size(gpcp_daily);
    [p1 p2 p3] = size(prmsl_daily);
    
    for dd = 1:length(dat)
        iwnd = find(tw == dat(dd));
        if isempty(iwnd)
            umaxd(u1,u2,dd) = NaN;
            vmaxd(v1,v2,dd) = NaN;
        else
            umaxd(:,:,dd) = umax_daily(:,:,iwnd); vmaxd(:,:,dd) = vmax_daily(:,:,iwnd);
        end
        
        isst = find(ts == dat(dd));
        if isempty(isst)
            sstd(s1,s2,dd) = NaN;
        else 
            sstd(:,:,dd) = sst_daily(:,:,isst);
        end
        
        igpcp = find(tg == dat(dd)); 
        if isempty(igpcp)
            gpcpd(g1,g2,dd) = NaN;
        else
            gpcpd(:,:,dd) = gpcp_daily(:,:,igpcp);
        end
        
        iprmsl = find(tp == dat(dd)); 
        if isempty(iprmsl)
            prmsld(p1,p2,dd) = NaN;
        else
            prmsld(:,:,dd) = prmsl_daily(:,:,iprmsl);
        end
        
        isurge = find(surge_daily(:,1) == dat(dd)); 
        if isempty(isurge)
            surged(dd,:) = [dat(dd) NaN];
        else
            surged(dd,:) = surge_daily(isurge,:);
        end
        
        %iskew = find(sk_daily(:,1) == dat(dd));
        %if isempty(iskew)
         %   skewd(dd,:) = [dat(dd) NaN];
        %else
         %   skewd(dd,:) = sk_daily(iskew,:);
        %end
    end
    clearvars -except pp pool basepath list_tg t Twind u1 u2 u3 v1 v2 v3 s1 s2 s3 g1 g2 g3 ... 
        p1 p2 p3 Tgpcp Tprmsl Tsst umaxd vmaxd sstd gpcpd prmsld surged skewd dat fid lat_t lon_t
    
    %removing nans from predictands and corresponding values from
    %predictors
    sg_nan = find(isnan(surged(:,2))); %finding nans in daily surge data
    %sk_nan = find(isnan(skewd(:,2)));  %finding nans in daily skew surge data
    all_nan = unique(sg_nan);
    %all_nan = unique([sg_nan;sk_nan]); %combine nans
    
    if length(all_nan) == length(dat)
        continue;
    end
    
    clearvars -except pp pool basepath list_tg t Twind u1 u2 u3 v1 v2 v3 s1 s2 s3 g1 g2 g3 ...
    p1 p2 p3 Tgpcp Tprmsl Tsst all_nan umaxd vmaxd sstd gpcpd prmsld surged skewd fid lat_t lon_t
    %skewd(all_nan, :) = []; 
    surged(all_nan, :) = [];
    umaxd(:,:,all_nan) = []; 
    vmaxd(:,:,all_nan) = [];
    Twind(all_nan) = [];
    sstd(:,:,all_nan) = [];
    Tsst(all_nan) = [];
    gpcpd(:,:,all_nan) = [];
    Tgpcp(all_nan) = [];
    prmsld(:,:,all_nan) = [];
    Tprmsl(all_nan) = [];
    [u1 u2 u3] = size(umaxd); [v1 v2 v3] = size(vmaxd);
    [s1 s2 s3] = size(sstd); [g1 g2 g3] = size(gpcpd);
    [p1 p2 p3] = size(prmsld);
    
    
    % Principal Component Analysis (PCA)
    disp('Step #2 - PCA')
    u_per = permute(umaxd, [3 2 1]); u_rsh = reshape(u_per, u3, u1*u2);
    v_per = permute(vmaxd, [3 2 1]); v_rsh = reshape(v_per, v3, v1*v2);
    s_per = permute(sstd, [3 2 1]); s_rsh = reshape(s_per, s3, s1*s2);
    p_per = permute(prmsld, [3 2 1]); p_rsh = reshape(p_per, p3, p1*p2);
    g_per = permute(gpcpd, [3 2 1]); g_rsh = reshape(g_per, g3, g1*g2);
    
    %check nan values
    [ru cu] = find(isnan(u_rsh)); 
    u_rsh2 = u_rsh;
    if length(unique(ru)) == u3 && length(unique(cu)) == u1*u2
        u_rsh2(:, :) = 0; u_r = [];
    elseif length(unique(ru)) < u3 && length(unique(cu)) == u1*u2
        u_r = ru;
    elseif length(unique(ru)) < u3 && length(unique(cu)) < u1*u2
        u_rsh2(:, unique(cu)) = []; u_r = ru;
    else
        u_rsh2(:, unique(cu)) = []; u_r = [];
    end
    
    
    [rv cv] = find(isnan(v_rsh)); 
    v_rsh2 = v_rsh;
    if length(unique(rv)) == v3 && length(unique(cv)) == v1*v2
        v_rsh2(:, :) = 0; v_r = [];
    elseif length(unique(rv)) < v3 && length(unique(cv)) == v1*v2
        v_r = rv;
    elseif length(unique(rv)) < v3 && length(unique(cv)) < v1*v2
        v_rsh2(:, unique(cv)) = []; v_r = rv;
    else
        v_rsh2(:, unique(cv)) = []; v_r = [];
    end
    
    

    [rs cs] = find(isnan(s_rsh)); 
    s_rsh2 = s_rsh;
    if length(unique(rs)) == s3 && length(unique(cs)) == s1*s2
        s_rsh2(:, :) = 0; s_r = [];
    elseif length(unique(rs)) < s3 && length(unique(cs)) == s1*s2
        s_r = rs;
    elseif length(unique(rs)) < s3 && length(unique(cs)) < s1*s2
        s_rsh2(:, unique(cs)) = []; s_r = rs;
    else
        s_rsh2(:, unique(cs)) = []; s_r = [];
    end  

    
    [rp cp] = find(isnan(p_rsh)); 
    p_rsh2 = p_rsh;
    if length(unique(rp)) == p3 && length(unique(cp)) == p1*p2
        p_rsh2(:, :) = 0; p_r = [];
    elseif length(unique(rp)) < p3 && length(unique(cp)) == p1*p2
        p_r = rp;
    elseif length(unique(rp)) < p3 && length(unique(cp)) < p1*p2
        p_rsh2(:, unique(cp)) = []; p_r = rp;
    else
        p_rsh2(:, unique(cp)) = []; p_r = [];
    end
    
    
    [rg cg] = find(isnan(g_rsh)); 
    g_rsh2 = g_rsh;
    if length(unique(rg)) == g3 && length(unique(cg)) == g1*g2
        g_rsh2(:, :) = 0; g_r = [];
    elseif length(unique(rg)) < g3 && length(unique(cg)) == g1*g2
        g_r = rg;
    elseif length(unique(rg)) < g3 && length(unique(cg)) < g1*g2
        g_rsh2(:, unique(cg)) = []; g_r = rg;
    else
        g_rsh2(:, unique(cg)) = []; g_r = [];
    end
    
    nans = unique([u_r; v_r; s_r; p_r; g_r]);
    
    % Removing corresponding rows from pcts and pcd
    %skewd(nans, :) = []; 
    surged(nans, :) = [];
    u_rsh2(nans, :) = []; 
    v_rsh2(nans, :) = [];
    Twind(nans) = [];
    s_rsh2(nans, :) = [];
    Tsst(nans) = [];
    g_rsh2(nans, :) = [];
    Tgpcp(nans) = [];
    p_rsh2(nans, :) = [];
    Tprmsl(nans) = [];
  
    % Compute zscores *for configuration 2* u^2 and v^2
    z_u = zscore(u_rsh2); z_v = zscore(v_rsh2); 
    z_u2 = zscore(u_rsh2.*u_rsh2); z_v2 = zscore(v_rsh2.*v_rsh2); 
    z_u3 = zscore(u_rsh2.*u_rsh2.*u_rsh2); z_v3 = zscore(v_rsh2.*v_rsh2.*v_rsh2);
    %z_s = zscore(s_rsh2);
    z_p = zscore(p_rsh2); %z_g = zscore(g_rsh2);
    %clearvars -except basepath list_tg t Twind Tgpcp Tprmsl Tsst ...
        %umaxd vmaxd sstd gpcpd prmsld surged skewd z_u z_v z_s ...
        %z_p z_g fid u1 u2 u3 v1 v2 v3 s1 s2 s3 g1 g2 g3 p1 p2 p3 lat_t lon_t
      
    %PCA 
    [cof_u,score_u,latent_u,tsquared_u,explained_u] = pca(z_u); 
    [cof_v,score_v,latent_v,tsquared_v,explained_v] = pca(z_v);
    [cof_u2,score_u2,latent_u2,tsquared_u2,explained_u2] = pca(z_u2);
    [cof_v2,score_v2,latent_v2,tsquared_v2,explained_v2] = pca(z_v2);
    [cof_u3,score_u3,latent_u3,tsquared_u3,explained_u3] = pca(z_u3);
    [cof_v3,score_v3,latent_v3,tsquared_v3,explained_v3] = pca(z_v3);
    [cof_p,score_p,latent_p,tsquared_p,explained_p] = pca(z_p);
    %[cof_g,score_g,latent_g,tsquared_g,explained_g] = pca(z_g);
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
 
    % Subsetting PCs that explain at least 90% of the variance
    % uwnd
    ee = 1;
    while sum(explained_u(1:ee)) < 90
        ee = ee + 1;
    end
    u_pc = ee; % number of PCs chosen for uwnd
    pc_uwnd = score_u(:,1:u_pc);
    
    %uwnd^2
    ee = 1;
    while sum(explained_u2(1:ee)) < 90
        ee = ee + 1;
    end
    u2_pc = ee; % number of PCs chosen for uwnd
    pc_uwnd2 = score_u2(:,1:u2_pc);
    
    %uwnd^3
    ee = 1;
    while sum(explained_u3(1:ee)) < 90
        ee = ee + 1;
    end
    u3_pc = ee; % number of PCs chosen for uwnd
    pc_uwnd3 = score_u3(:,1:u3_pc);
   
    %vwnd
    ee = 1;
    while sum(explained_v(1:ee)) < 90
        ee = ee + 1;
    end
    v_pc = ee;
    pc_vwnd = score_v(:,1:v_pc);
    
    %vwnd^2
    ee = 1;
    while sum(explained_v2(1:ee)) < 90
        ee = ee + 1;
    end
    v2_pc = ee; % number of PCs chosen for uwnd
    pc_vwnd2 = score_v2(:,1:v2_pc);
    
    %vwnd^3
    ee = 1;
    while sum(explained_v3(1:ee)) < 90
        ee = ee + 1;
    end
    v3_pc = ee; % number of PCs chosen for uwnd
    pc_vwnd3 = score_v3(:,1:v3_pc);
    
    %prmsl
    ee = 1;
    while sum(explained_p(1:ee)) < 90
        ee = ee + 1;
    end
    p_pc = ee;
    pc_prmsl = score_p(:,1:p_pc);
    

    vars = [pc_uwnd pc_vwnd pc_uwnd2 pc_vwnd2 pc_uwnd3 pc_vwnd3 pc_prmsl];
    y_surge = surged(:,2);
    %y_skew = skewd(:,2);
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

    
    % Stepwise Regression - Surge
    [b,se,pval,inmodel,stats,nextstep,history] = stepwisefit(vars, y_surge);
    
    % Reconstructing Surge after stepwise regression
    vars_new = vars(:,find(inmodel == 1));
    b_new = b(find(inmodel == 1));
    y_recsurge = stats.intercept + vars_new*b_new;
    %clearvars -except basepath list_tg t Twind Tgpcp Tprmsl Tsst ...
        %umaxd vmaxd sstd gpcpd prmsld surged skewd pc_uwnd pc_vwnd ...
        %pc_sst pc_prmsl pc_gpcp vars y_surge y_skew y_recsurge fid lat_t lon_t
    
    % Plotting
    %figure; scatter(y_surge, y_recsurge);
    %xlabel('Observed Surge(m)'); ylabel('Modelled Surge(m)');
    %hline = refline([1, 0]); hline.Color = 'r';
    %toptitle = sprintf('%s', list_tg(t).name);
    %title(toptitle);
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
    
    % Stepwise Regression - Skew Surge
    %[b_sk,se_sk,pval_sk,inmodel_sk,stats_sk,nextstep_sk,history_sk] = stepwisefit(vars, y_skew);
    
    % Reconstructing Skew Surge after stepwise regression
    %vars_sk = vars(:,find(inmodel_sk == 1));
    %b_new_sk = b_sk(find(inmodel_sk == 1));
    %y_recskew = stats_sk.intercept + vars_sk*b_new_sk;
    %clearvars -except basepath list_tg t Twind Tgpcp Tprmsl Tsst lat_t lon_t ...
        %umaxd vmaxd sstd gpcpd prmsld surged skewd pc_uwnd pc_vwnd ...
        %pc_sst pc_prmsl pc_gpcp vars y_surge y_skew y_recsurge y_recskew fid
    % Plotting
    %figure; scatter(y_skew, y_recskew);
    %xlabel('Observed Skew Surge(m)'); ylabel('Modelled Skew Surge(m)');
    %hline = refline([1, 0]); hline.Color = 'r';
    %toptitle = sprintf('%s', list_tg(t).name);
    %title(toptitle);
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
    % Adding lon & lat for tide gauge
    %cd(fullfile(basepath, list_tg(t).name))
    %load('CCMP.mat'); clearvars -except basepath list_tg t Twind Tgpcp Tprmsl Tsst ...
        %umaxd vmaxd sstd gpcpd prmsld surged skewd pc_uwnd pc_vwnd lat_t lon_t ...
        %pc_sst pc_prmsl pc_gpcp vars y_surge y_skew y_recsurge y_recskew lat_t lon_t fid


    % Saving .mat files
    folder = 'F:\OneDrive - Knights - University of Central Florida\Daten\MLR\PCA_Stepwise_confg_10'
    baseFileName = sprintf('%s_pca_stp.mat', list_tg(t).name);
    fullMatFileName = fullfile(folder, baseFileName);
    save(fullMatFileName);
    clearvars -except pp pool basepath list_tg t fid
end
fclose(fid);
    
    
    
    
    
    
    
    
    
    
    
    
    

