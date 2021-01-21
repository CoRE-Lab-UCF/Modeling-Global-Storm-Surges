% Error statistics - Surges exceeding a specific threshold %

src = 'F:\OneDrive - Knights - University of Central Florida\Daten\MLR\best_model\BestMdl_v2' % source folder
dst = 'F:\OneDrive - Knights - University of Central Florida\Daten\MLR\best_model\Threshold_Exceeding_statistics' % destination

cd(src)
lst_src = dir('*mat')

for ii = 1:length(lst_src)
    cd(src)
    load(lst_src(ii).name)
    clearvars -except lst_src src dst lat_t lon_t y_surge y_rec ii
    q = quantile(y_surge(:,2), [0.7 0.8 0.9 0.95 0.99])';
    for jj = 1:length(q)
        ind{jj} = find(y_surge(:,2) >= q(jj));
        qunt{1,jj} = [y_surge(ind{jj},2) y_rec(ind{jj},2)];
        [rho pval] = corr(qunt{1,jj}(:,1), qunt{1,jj}(:,2));
        qunt{2,jj} = [rho pval]; % correlation and pval
        zz = qunt{1,jj}(:,1) - qunt{1,jj}(:,2); 
        zsqr = zz.*zz;
        zmean = mean(zsqr);
        sg_rmse = sqrt(zmean);
        qunt{3,jj} = sg_rmse; %  rmse of the respective qunatile
        
        % to collect only significant correlations

        if qunt{2,jj}(:,2) < 0.05
            qunt{4, jj} = 1;
            qunt{5, jj} = qunt{2, jj};
        else 
            qunt{4, jj} = 0;
            qunt{5, jj} = NaN;
        end
    end
    

    clearvars -except lst_src src dst lat_t lon_t y_surge y_rec q ii ind qunt
    cd(dst)
    save(lst_src(ii).name)
end

