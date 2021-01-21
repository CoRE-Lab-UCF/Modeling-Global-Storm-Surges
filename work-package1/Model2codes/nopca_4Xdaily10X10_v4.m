% To do PCA on time-lagged predictors
% Skipping PCA to test the zscores instead of the PCs


b1 = 'F:\OneDrive - Knights - University of Central Florida\Daten\MLR\Model_2\Extracted'
%b2 = 'F:\OneDrive - Knights - University of Central Florida\Daten\MLR\Model_2\4Xdaily_10X10_217_TGs'

a = dir(b1); b = [a.isdir]; lst1 = a(b); lst1(1:2) = [];
%c = dir(b2); d = [c.isdir]; lst2 = c(d); lst2(1:2) = []; 
clearvars -except b1 b2 lst1 lst2 
% PCA for Model # 2; time-lagged predictors - 10X10 dXdaily

%Load predictors and predictand
for jj = 1:length(lst1)
    jj
    cd(fullfile(b1, lst1(jj).name));
    %Load uwnd
    load('uwnd_lagged.mat')
    clear base_dir fid tg_lst ii
    %Load vwnd
    load('vwnd_lagged.mat')
    clear base_dir fid tg_lst ii
    %Load slp
    load('slp_lagged.mat')
    clear base_dir fid tg_lst ii
    %Load daily max surge
    load('surge_dmax.mat')
    clearvars -except b1 jj lst1 s6 s0 s12 s18 s24 s30...
        u0 u12 u18 u24 u30 u6 v0 v12 v18 v24 v30 v6 lat_t lon_t surge_sub
    
    %Permuting and reshaping predictors
    a = size(u0);
    u0_per = permute(u0, [3 2 1]); u0_rsh = reshape(u0_per, a(3), a(1)*a(2));
    a = size(u6);
    u6_per = permute(u6, [3 2 1]); u6_rsh = reshape(u6_per, a(3), a(1)*a(2));
    a = size(u12);
    u12_per = permute(u12, [3 2 1]); u12_rsh = reshape(u12_per, a(3), a(1)*a(2));
    a = size(u18);
    u18_per = permute(u18, [3 2 1]); u18_rsh = reshape(u18_per, a(3), a(1)*a(2));
    a = size(u24);
    u24_per = permute(u24, [3 2 1]); u24_rsh = reshape(u24_per, a(3), a(1)*a(2));
    a = size(u30);
    u30_per = permute(u30, [3 2 1]); u30_rsh = reshape(u30_per, a(3), a(1)*a(2));

    a = size(v0);
    v0_per = permute(v0, [3 2 1]); v0_rsh = reshape(v0_per, a(3), a(1)*a(2));
    a = size(v6);
    v6_per = permute(v6, [3 2 1]); v6_rsh = reshape(v6_per, a(3), a(1)*a(2));
    a = size(v12);
    v12_per = permute(v12, [3 2 1]); v12_rsh = reshape(v12_per, a(3), a(1)*a(2));
    a = size(u18);
    v18_per = permute(v18, [3 2 1]); v18_rsh = reshape(v18_per, a(3), a(1)*a(2));
    a = size(v24);
    v24_per = permute(v24, [3 2 1]); v24_rsh = reshape(v24_per, a(3), a(1)*a(2));
    a = size(v30);
    v30_per = permute(v30, [3 2 1]); v30_rsh = reshape(v30_per, a(3), a(1)*a(2));
    
    a = size(s0);
    s0_per = permute(s0, [3 2 1]); s0_rsh = reshape(s0_per, a(3), a(1)*a(2));
    a = size(s6);
    s6_per = permute(s6, [3 2 1]); s6_rsh = reshape(s6_per, a(3), a(1)*a(2));
    a = size(s12);
    s12_per = permute(s12, [3 2 1]); s12_rsh = reshape(s12_per, a(3), a(1)*a(2));
    a = size(s18);
    s18_per = permute(s18, [3 2 1]); s18_rsh = reshape(s18_per, a(3), a(1)*a(2));
    a = size(s24);
    s24_per = permute(s24, [3 2 1]); s24_rsh = reshape(s24_per, a(3), a(1)*a(2));
    a = size(s30);
    s30_per = permute(s30, [3 2 1]); s30_rsh = reshape(s30_per, a(3), a(1)*a(2));
    
    
    %compute zscores
    zu0 = zscore(u0_rsh);
    zu6 = zscore(u6_rsh);
    zu12 = zscore(u12_rsh);
    zu18 = zscore(u18_rsh);
    zu24 = zscore(u24_rsh);
    zu30 = zscore(u30_rsh);
    
    
    zv0 = zscore(v0_rsh);
    zv6 = zscore(v6_rsh);
    zv12 = zscore(v12_rsh);
    zv18 = zscore(v18_rsh);
    zv24 = zscore(v24_rsh);
    zv30 = zscore(v30_rsh);
    
    
    zs0 = zscore(s0_rsh);
    zs6 = zscore(s6_rsh);
    zs12 = zscore(s12_rsh);
    zs18 = zscore(s18_rsh);
    zs24 = zscore(s24_rsh);
    zs30 = zscore(s30_rsh);
    

    %Prepare matrix of predictors & predictand
    
    vars = [zu0 zu6 zu12 zu18 zu24 ...
        zu30 zv0 zv6 zv12 ...
        zv18 zv24 zv30 zs0 zs6 ...
        zs12 zs18 zs24 zs30];
    
    y_surge = surge_sub(:,2);
    

    %Saving .mat files
    clearvars -except vars y_surge lat_t lon_t b1 lst1 jj
    folder = 'F:\OneDrive - Knights - University of Central Florida\Daten\MLR\Model_2\NOPCA_4Xdaily10X10_17yrs'
    baseFileName = sprintf('%s_pca_10x10_17yrs.mat', lst1(jj).name);
    fullMatFileName = fullfile(folder, baseFileName);
    save(fullMatFileName);
    clearvars -except b1 lst1 jj
    
    

    
end




























    