% in order to plot correlation of surge/skew surge with predctors
%usqr = umaxd.*umaxd; 
%ucub = umaxd.*umaxd.*umaxd;

bp = 'F:\OneDrive - Knights - University of Central Florida\Daten\MLR\PCA_Stepwise_confg_13'
cd(bp)
lst = dir('*.mat');

for t_t = 1:length(lst)
    t_t
    load(lst(t_t).name); disp(lst(t_t).name)
    %uwnd
    for ii = 1:u1
        for jj = 1:u2 
            z = size(umaxd(ii, jj, :));
            u_squz = reshape(umaxd(ii, jj, :), z(2:end))'; % just transform it to a vector for corr
            sg_u_corr(ii,jj) = corr(u_squz.*u_squz, surged(:,2), 'Rows', 'complete');
            sk_u_corr(ii,jj) = corr(u_squz, skewd(:,2), 'Rows', 'complete');
        end
    end
    % Surge
    corr_sgmax(t_t,1) = lon_t;
    corr_sgmax(t_t,2) = lat_t;
    corr_sgmax(t_t,3) = max(sg_u_corr(:));
    % Skew surge
    corr_skmax(t_t,1) = lon_t;
    corr_skmax(t_t,2) = lat_t;
    corr_skmax(t_t,3) = max(sk_u_corr(:));

    %vwnd
    for ii = 1:v1
        for jj = 1:v2 
            z = size(vmaxd(ii, jj, :));
            v_squz = reshape(vmaxd(ii, jj, :), z(2:end))'; % just transform it to a vector for corr
            sg_v_corr(ii,jj) = corr(v_squz, surged(:,2), 'Rows', 'complete');
            sk_v_corr(ii,jj) = corr(v_squz, skewd(:,2), 'Rows', 'complete');
        end
    end
    corr_sgmax(t_t,4) = max(sg_v_corr(:));
    corr_skmax(t_t,4) = max(sk_v_corr(:));
    
    %sst
    for ii = 1:s1
        for jj = 1:s2 
            z = size(sstd(ii, jj, :));
            s_squz = reshape(sstd(ii, jj, :), z(2:end))'; % just transform it to a vector for corr
            sg_s_corr(ii,jj) = corr(s_squz, surged(:,2), 'Rows', 'complete');
            sk_s_corr(ii,jj) = corr(s_squz, skewd(:,2), 'Rows', 'complete');
        end
    end
    corr_sgmax(t_t,5) = max(sg_s_corr(:));
    corr_skmax(t_t,5) = max(sk_s_corr(:));
    
    %prmsl
    for ii = 1:p1
        for jj = 1:p2 
            z = size(prmsld(ii, jj, :));
            p_squz = reshape(prmsld(ii, jj, :), z(2:end))'; % just transform it to a vector for corr
            sg_p_corr(ii,jj) = corr(p_squz, surged(:,2), 'Rows', 'complete');
            sk_p_corr(ii,jj) = corr(p_squz, skewd(:,2), 'Rows', 'complete');
        end
    end
    corr_sgmax(t_t,6) = max(sg_p_corr(:));
    corr_skmax(t_t,6) = max(sk_p_corr(:));
    
    %gpcp
    for ii = 1:g1
        for jj = 1:g2 
            z = size(gpcpd(ii, jj, :));
            g_squz = reshape(gpcpd(ii, jj, :), z(2:end))'; % just transform it to a vector for corr
            sg_g_corr(ii,jj) = corr(g_squz, surged(:,2), 'Rows', 'complete');
            sk_g_corr(ii,jj) = corr(g_squz, skewd(:,2), 'Rows', 'complete');
        end
    end
    corr_sgmax(t_t,7) = max(sg_g_corr(:));
    corr_skmax(t_t,7) = max(sk_g_corr(:));
    clearvars -except corr_skmax corr_sgmax t_t lst bp
end












