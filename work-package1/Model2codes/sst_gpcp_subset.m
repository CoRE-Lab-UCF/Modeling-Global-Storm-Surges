% To subset SST and GPCP predictors to prepare them for Model 2.5 and 3.5 %

%First load SST, GPCP, Surge file
fold = 'F:\OneDrive - Knights - University of Central Florida\Daten\MLR\Model_2\Extracted'
list_tg = dir(fold);
list_tg(1:2) = []; list_tg(1:5) = []; % removing non-folders

for mt = 620:length(list_tg)
    mt
    cd(fullfile(fold, list_tg(mt).name))
    load('GPCP.mat')
    clearvars -except fold list_tg mt Tgpcp gpcp_daily
    
    load('SST.mat')
    clearvars -except fold list_tg mt Tgpcp gpcp_daily Tsst sst_daily
    
    load('surge_dmax.mat')
    clearvars -except fold list_tg mt Tgpcp gpcp_daily Tsst sst_daily surge_sub
    
    g_dv = datevec(Tgpcp);
    ss_dv = datevec(Tsst);
    sg_dv = datevec(surge_sub(:,1));
    
    %Subsetting Precipitation 
    idd = [];
    for jk = 1: length(sg_dv)
        id = find(datenum(g_dv(:,1:3)) == datenum(sg_dv(jk,1:3)));
        if isnan(id)
            idd = NaN;
            idd = [idd; NaN];
        else 
            idd = [idd; id];
        end
    end

    tg_gpcp = Tgpcp(idd);
    gpcp_sub = gpcp_daily(:,:,idd);
    clear jk
    
    % Subsetting SST
    idd2 = [];
    for jk = 1: length(sg_dv)
        id = find(datenum(ss_dv(:,1:3)) == datenum(sg_dv(jk,1:3)));
        if isnan(id)
            idd2 = NaN;
            idd2 = [idd2; NaN];
        else 
            idd2 = [idd2; id];
        end
    end

    ts_sst = Tsst(idd2);
    sst_sub = sst_daily(:,:,idd2);
    
    save('gpcp_sst.mat', 'ts_sst', 'tg_gpcp', 'gpcp_sub', 'sst_sub')

end



