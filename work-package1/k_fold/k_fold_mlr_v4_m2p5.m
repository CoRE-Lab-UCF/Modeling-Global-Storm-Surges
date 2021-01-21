% Stepwise regression for M2.5

b_p = 'F:\OneDrive - Knights - University of Central Florida\Daten\MLR\Model_2\M2.5\mdl2p5_MLR_Kfold_4daily_10X10_17yrs' %MLR folder
cd 'F:\OneDrive - Knights - University of Central Florida\Daten\MLR\Model_2\M2.5\mdl2p5_PCA_4Xdaily10X10_17yrs' %PCA folder
lst = dir('*.mat');
rng default %to get same randomized results always
for i_i = 331:length(lst)
    cd 'F:\OneDrive - Knights - University of Central Florida\Daten\MLR\Model_2\M2.5\mdl2p5_PCA_4Xdaily10X10_17yrs' %PCA folder
    load(lst(i_i).name)
    clearvars -except i_i baseFileName b_p lst vars y_surge lat_t lon_t
    INDICES = crossvalind('Kfold',y_surge,10); %partitioning the data to k folds

    % start training and testing
    bb = (1:10)';
    stat_r = []; stat_rsq = []; stat_rmse = [];
    for a = 1:10
        c = find(bb ~= a); %the folds that will be used for training
        ind_trn = find(INDICES ~= a);
        %Training
        x_trn = vars(ind_trn,:); %training predictors from PCA
        y_trn = y_surge(ind_trn,:); %training predictand/storm surge 
        [b,se,pval,inmodel,stats,nextstep,history] = stepwisefit(x_trn, y_trn); %applying MLR stepwise regression
        x_trn_new = x_trn(:,find(inmodel == 1));
        b_new = b(find(inmodel == 1));
        y_trn_mdl = stats.intercept + x_trn_new*b_new;
        
        %Testing
        ind_tst = find(INDICES == a);
        x_tst = vars(ind_tst,:); %testing predictors
        y_tst = y_surge(ind_tst,:); %testing predictand
        x_tst_new = x_tst(:,find(inmodel == 1));
        y_tst_mdl = stats.intercept + x_tst_new*b_new;
        
        %Plotting Training MLR results
        close all;
        subplot(2,1,1); ss = scatter(y_trn, y_trn_mdl, '+', 'k');
        xlabel('Observed Surge(m)'); ylabel('Modelled Surge(m)');
        hline = refline([1, 0]); hline.Color = 'r'; set(hline, 'LineWidth', 2);
        s1 = strsplit(baseFileName,'_pca_stp.mat');
        s2 = sprintf('%s.jpeg', char(s1(1)));
        til = sprintf('%s%s%d', char(s1(1)),' - Training Model (MLR) - ', a);
        title(til);
        
        R = corr(y_trn, y_trn_mdl); R_squared = R^2;
        xx = y_trn; yy = y_trn_mdl; zz = yy - xx; zsqr = zz.*zz; zmean = mean(zsqr); sg_rmse = sqrt(zmean);
        text(0.05,0.85, ['R^2 = ' num2str(R_squared)], 'Units', 'normalized','Color', 'red', 'FontSize', 9);
        text(0.05,0.65, ['RMSE = ' num2str(sg_rmse*100) 'cm'], 'Units', 'normalized','Color', 'red', 'FontSize', 9);
        set(gca, 'Box', 'on', 'XMinorTick', 'on', 'YMinorTick', 'on', 'fontname', 'times');
        d = sprintf('%s.jpeg', til); %Title of the JPEG file
        
        
        %Plotting Testing MLR results
        subplot(2,1,2); ss = scatter(y_tst, y_tst_mdl, '+', 'k');
        xlabel('Observed Surge(m)'); ylabel('Modelled Surge(m)');
        hline = refline([1, 0]); hline.Color = 'r'; set(hline, 'LineWidth', 2);
        til = sprintf('%s%s%d', char(s1(1)),' - Testing Model (MLR) - ', a);
        title(til);
        
        R = corr(y_tst, y_tst_mdl); R_squared = R^2;
        xx = y_tst; yy = y_tst_mdl; zz = yy - xx; zsqr = zz.*zz; zmean = mean(zsqr); sg_rmse = sqrt(zmean); %calculate rmse
        text(0.05,0.85, ['R^2 = ' num2str(R_squared)], 'Units', 'normalized','Color', 'red', 'FontSize', 9);
        text(0.05,0.65, ['RMSE = ' num2str(sg_rmse*100) 'cm'], 'Units', 'normalized','Color', 'red', 'FontSize', 9);
        set(gca, 'Box', 'on', 'XMinorTick', 'on', 'YMinorTick', 'on', 'fontname', 'times');
        d = sprintf('%s.jpeg', til); %Title of the JPEG file
        stat_r = [stat_r R]; stat_rsq = [stat_rsq R_squared]; stat_rmse = [stat_rmse sg_rmse]; 
        r_avg = mean(stat_r); rsq_avg = mean(stat_rsq); rmse_avg = mean(stat_rmse);
       
        % saving image
        cd(b_p)
        fold_name = sprintf('%s', lst(i_i).name);
        aaa = exist(fold_name) - 1;
        if aaa ~= 6
            mkdir(lst(i_i).name); 
            cd(lst(i_i).name);
        else 
            cd(lst(i_i).name);
        end
        
        saveas(figure(1),d);
        close all

     
    end
    f1 = strsplit(baseFileName,'_pca_10x10_17yrs.mat');
    f2 = sprintf('%s_mlr_mdl2p5.mat', char(f1(1)));
    save(f2);
    clearvars -except i_i b_p lst    
end