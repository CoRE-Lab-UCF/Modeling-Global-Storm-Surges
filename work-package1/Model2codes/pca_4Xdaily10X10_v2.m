% To do PCA on time-lagged predictors
b1 = 'F:\OneDrive - Knights - University of Central Florida\Daten\MLR\Model_2\Extracted'
%b2 = 'F:\OneDrive - Knights - University of Central Florida\Daten\MLR\Model_2\4Xdaily_10X10_217_TGs'

a = dir(b1); b = [a.isdir]; lst1 = a(b); lst1(1:2) = [];
%c = dir(b2); d = [c.isdir]; lst2 = c(d); lst2(1:2) = []; 
clearvars -except b1 b2 lst1 lst2 
% PCA for Model # 2; time-lagged predictors - 10X10 dXdaily

%Load predictors and predictand
for jj = 1:length(lst1)
    cd(fullfile(b1, lst1(jj).name))
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
    
    %Selecting the 18 predictors 
    prct = {'u0'; 'u12'; 'u18'; 'u24'; 'u30'; 'u6'; 'v0'; 'v12'; 'v18'; 'v24'; ...
        'v30'; 'v6'; 's6'; 's0'; 's12'; 's18'; 's24'; 's30'};
    pct = whos; ind = [];
    for nn = 1:length(pct)
        if ismember(pct(nn).name, prct)
            d = 1; ind = [ind; d];
        else
            d = 0; ind = [ind; d];
        end
    end
    pct2 = pct(find(ind == 1), :);
    
    %Permuting and reshaping the 18 predictors
    for cc = 1:length(pct2)
        p_name = pct2(cc).name
        perm_name = strcat(p_name,'_perm')
        p_size = pct2(cc).size
    end
    

            



    
end




























    